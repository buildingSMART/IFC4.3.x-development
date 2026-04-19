from __future__ import annotations

import importlib
import importlib.util
import itertools
import json
import mimetypes
import os
import re
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType, SimpleNamespace
from urllib.parse import unquote

from jinja2 import BaseLoader, Environment, FileSystemLoader, select_autoescape

from .config import BuildConfig
from .refiner import BeautifulSoup, HtmlRefiner, ListingCollector
from .search import SearchIndexBuilder


class RenderAbort(Exception):
    def __init__(self, status_code: int):
        super().__init__(f"render aborted with status {status_code}")
        self.status_code = status_code


@dataclass(frozen=True)
class StaticResponse:
    body: bytes
    mimetype: str


def _generated_output_root(config: BuildConfig) -> Path:
    return config.repo_root / "output"


def _generated_file(config: BuildConfig, name: str) -> Path:
    candidate = _generated_output_root(config) / name
    if candidate.exists():
        return candidate
    return config.code_dir / name


class StaticTemplateRenderer:
    CONTENT_NAMES = ["scope", "normative_references", "terms_and_definitions", "concepts"]
    CONTENT_NAMES_2 = ["cover", "foreword", "introduction", "bibliography"]
    NAVIGATION = [
        [
            {"name": "Cover", "url": "/"},
            {"name": "Contents", "url": "/toc.html"},
            {"name": "Foreword", "url": "/content/foreword.htm"},
            {"name": "Introduction", "url": "/content/introduction.htm"},
        ],
        [
            {"number": 1, "name": "Scope", "url": "/content/scope.htm"},
            {"number": 2, "name": "Normative references", "url": "/content/normative_references.htm"},
            {
                "number": 3,
                "name": "Terms, definitions, and abbreviated terms",
                "url": "/content/terms_and_definitions.htm",
            },
            {"number": 4, "name": "Fundamental concepts and assumptions", "url": "/concepts/content.html"},
            {"number": 5, "name": "Core data schemas", "url": "/chapter-5/"},
            {"number": 6, "name": "Shared element data schemas", "url": "/chapter-6/"},
            {"number": 7, "name": "Domain specific data schemas", "url": "/chapter-7/"},
            {"number": 8, "name": "Resource definition data schemas", "url": "/chapter-8/"},
        ],
        [
            {"number": "A", "name": "Computer interpretable listings", "url": "/annex-a.html"},
            {"number": "B", "name": "Alphabetical listings", "url": "/annex-b.html"},
            {"number": "C", "name": "Inheritance listings", "url": "/annex-c.html"},
            {"number": "D", "name": "Diagrams", "url": "/annex-d.html"},
            {"number": "E", "name": "Examples", "url": "/annex-e.html"},
            {"number": "F", "name": "Change logs", "url": "/annex-f.html"},
        ],
        [
            {"name": "Bibliography", "url": "/content/bibliography.htm"},
            {"name": "Index", "url": "/index.htm"},
        ],
    ]
    ANNEX_B_NAVIGATION = [
        {"number": "B.1", "name": "Entities", "url": "/annex-b1.html"},
        {"number": "B.2", "name": "Types", "url": "/annex-b2.html"},
        {"number": "B.3", "name": "Property sets", "url": "/annex-b3.html"},
        {"number": "B.4", "name": "Properties", "url": "/annex-b4.html"},
        {"number": "B.5", "name": "Functions", "url": "/annex-b5.html"},
        {"number": "B.6", "name": "Rules", "url": "/annex-b6.html"},
        {"number": "B.7", "name": "Property Enumerations", "url": "/annex-b7.html"},
    ]

    def __init__(self, config: BuildConfig, server):
        self.config = config
        self.server = server
        self.version = importlib.import_module("version")
        self.examples_repo_root = (config.repo_root.parent / "examples").resolve()
        self.examples_models_root = (self.examples_repo_root / "models").resolve()
        self.listing_payloads = {"references": [], "figures": [], "tables": []}
        self.request = SimpleNamespace(path="/", args={}, form={}, cookies={})
        self.server.request = self.request
        self.server.url_for = self._url_for
        self.server.abort = self._abort
        self.server.base = ""
        self.server.is_iso = False
        self.server.is_package = False
        self.server.X = SimpleNamespace(is_iso=False, is_package=False)

        self.template_environment = Environment(
            loader=FileSystemLoader(str(self.config.code_dir / "templates")),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.template_environment.filters["slugify"] = self.server.slugify
        self.template_string_environment = Environment(
            loader=BaseLoader(),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render_path(self, public_path: str) -> StaticResponse:
        path = self._normalize_public_path(public_path)
        self.request.path = path
        self.request.args = {}
        self.request.form = {}
        self.request.cookies = {}

        if path == "/":
            return self._render_cover()
        if path == "/index.htm":
            return self._render_index()
        if path == "/search.html":
            return self._render_search()
        if path == "/toc.html":
            return self._render_toc()

        if path.startswith("/content/") and path.endswith(".htm"):
            return self._render_content(path[len("/content/") : -4])
        if path.startswith("/lexical/") and path.endswith(".htm"):
            return self._render_resource(path[len("/lexical/") : -4])
        if path.startswith("/property/") and path.endswith(".htm"):
            return self._render_property(path[len("/property/") : -4])

        if path == "/annex-a.html":
            return self._html_response(
                "annex-a.html",
                navigation=self.get_navigation(),
                has_bsdd=(self.config.repo_root / "output" / "bsdd" / "IFC.json").exists(),
                body_class="annex",
            )
        if path == "/annex-a-express.html":
            return self._html_response(
                "annex-a-express.html",
                navigation=self.get_navigation(),
                express=_generated_file(self.config, "IFC.exp").read_text(encoding="utf-8"),
                link=f"{self.server.SCHEMA_NAME}.exp",
                body_class="annex",
            )
        if path == "/annex-a-xsd.html":
            return self._html_response(
                "annex-a-xsd.html",
                navigation=self.get_navigation(),
                link=f"{self.server.SCHEMA_NAME}.xsd",
                body_class="annex",
            )
        if path in {f"/{self.server.SCHEMA_NAME}.exp", f"/{self.server.SCHEMA_NAME}.xsd"}:
            extension = Path(path).suffix
            return self._file_response(_generated_file(self.config, f"IFC{extension}"))
        if path == "/annex-a-psd.zip":
            return self._file_response(_generated_file(self.config, "psd.zip"))

        if path == "/annex-b.html":
            return self._render_annex_b()
        if path == "/annex-b1.html":
            return self._render_annex_b1()
        if path == "/annex-b2.html":
            return self._render_annex_b2()
        if path == "/annex-b3.html":
            return self._render_annex_b3()
        if path == "/annex-b4.html":
            return self._render_annex_b4()
        if path == "/annex-b5.html":
            return self._render_annex_b5()
        if path == "/annex-b6.html":
            return self._render_annex_b6()
        if path == "/annex-b7.html":
            return self._render_annex_b7()

        if path == "/annex-c.html":
            return self._render_annex_c()
        if path == "/annex-d.html":
            return self._render_annex_d()
        match = re.fullmatch(r"/annex_d/(.+)\.html", path)
        if match:
            return self._render_annex_d_diagram_page(unquote(match.group(1)))
        match = re.fullmatch(r"/annex_d/(.+)\.png", path)
        if match:
            return self._file_response(self.config.repo_root / "output" / "ifc4x3_add2.uml" / f"{unquote(match.group(1))}.png")

        if path == "/annex-e.html":
            return self._render_annex_e()
        match = re.fullmatch(r"/annex_e/(.+)\.html", path)
        if match:
            return self._render_annex_e_example_page(unquote(match.group(1)))
        if path == "/annex-f.html":
            return self._render_annex_f()

        if path == "/concepts/content.html":
            return self._render_concept_list()
        match = re.fullmatch(r"/concepts/(.+)/content\.html", path)
        if match:
            return self._render_concept(unquote(match.group(1)))

        match = re.fullmatch(r"/chapter-(\d+)/", path)
        if match:
            return self._render_chapter(match.group(1))

        match = re.fullmatch(r"/listing-(references|figures|tables)\.html", path)
        if match:
            return self._render_listing(match.group(1))

        match = re.fullmatch(r"/([^/]+)/content\.html", path)
        if match:
            return self._render_schema(unquote(match.group(1)))

        if path.startswith("/assets/"):
            return self._file_response(self.config.repo_root / "docs" / "assets" / path[len("/assets/") :])
        if path.startswith("/figures/examples/"):
            return self._file_response(self.config.repo_root / "docs" / "figures" / "examples" / path[len("/figures/examples/") :])
        if path.startswith("/figures/"):
            return self._file_response(self.config.repo_root / "docs" / "figures" / path[len("/figures/") :])
        if path.startswith("/examples/"):
            return self._file_response(self.examples_models_root / path[len("/examples/") :])
        if path.startswith("/svgs/"):
            return self._file_response(self.config.code_dir / "svgs" / path[len("/svgs/") :])

        self._abort(404)

    def _normalize_public_path(self, public_path: str) -> str:
        if not public_path:
            return "/"
        path = unquote(public_path)
        if not path.startswith("/"):
            path = "/" + path
        return path

    def set_listing_payloads(self, payloads: dict[str, list[dict[str, str]]]) -> None:
        self.listing_payloads = {
            "references": list(payloads.get("references", [])),
            "figures": list(payloads.get("figures", [])),
            "tables": list(payloads.get("tables", [])),
        }

    def _abort(self, status_code: int):
        raise RenderAbort(status_code)

    def _url_for(self, endpoint: str, **values) -> str:
        values.pop("_external", None)
        mapping = {
            "resource": lambda: f"/lexical/{values['resource']}.htm",
            "property": lambda: f"/property/{values['prop']}.htm",
            "schema": lambda: f"/{values['name']}/content.html",
            "content": lambda: f"/content/{values['s']}.htm",
            "chapter": lambda: f"/chapter-{values['n']}/",
            "get_example_figure": lambda: f"/figures/examples/{values['fig']}",
            "get_asset": lambda: f"/assets/{values['asset']}",
            "get_example": lambda: f"/examples/{values['example']}",
            "annex_e_example_page": lambda: f"/annex_e/{values['s']}.html",
            "annex_d_diagram_page": lambda: f"/annex_d/{values['s']}.html",
        }
        if endpoint not in mapping:
            raise KeyError(f"unsupported endpoint: {endpoint}")
        return mapping[endpoint]()

    def _file_response(self, path: Path) -> StaticResponse:
        if not path.exists() or not path.is_file():
            self._abort(404)
        content_type, _ = mimetypes.guess_type(str(path))
        return StaticResponse(path.read_bytes(), content_type or "application/octet-stream")

    def _html_response(self, template_name: str, **context) -> StaticResponse:
        html = self._render_template(template_name, **context)
        return StaticResponse(html.encode("utf-8"), "text/html")

    def _render_template(self, template_name: str, **context) -> str:
        template = self.template_environment.get_template(template_name)
        return template.render(self._template_context(**context))

    def _render_string(self, source: str, **context) -> str:
        template = self.template_string_environment.from_string(source)
        return template.render(self._template_context(**context))

    def _template_context(self, **context) -> dict:
        payload = {
            "base": "",
            "is_iso": False,
            "is_package": False,
            "schema_version_string": self.version.schema_version_string,
            "spec_version_string": self.version.spec_version_string,
            "spec_version_string_full": self.version.spec_version_string_full,
            "branch": self.server.REPO_BRANCH,
            "get_language_icon": self.server.translate.get_language_icon,
            "current_lang_slug": self.server.slugify("English (default)"),
            "languages": self.server.translate.list_languages(),
        }
        payload.update(context)
        return payload

    def _repo_relative(self, path: Path) -> str:
        return path.resolve().relative_to(self.config.repo_root).as_posix()

    def _toc_entry(self, text: str, number: str | None = None, url: str | None = None, children=None, mvds=None):
        return self.server.toc_entry(text=text, number=number, url=url, children=children or [], mvds=mvds)

    def chapter_lookup(self, number=None, cat=None):
        def do_lookup(node):
            if isinstance(node, (list, tuple)):
                for value in node:
                    found = do_lookup(value)
                    if found is not None:
                        return found
                return None
            if number is not None and node.get("number") == number:
                return node
            if cat is not None and node["name"].split(" ")[0].lower() == cat:
                return node
            return None

        return do_lookup(self.NAVIGATION)

    def get_navigation(self, resource=None, number=None):
        if resource and not number:
            number = self.server.name_to_number()[resource]

        sections = [[dict(item, subitems=[]) for item in group] for group in self.NAVIGATION]
        numbers: list[str] = []
        if isinstance(number, str):
            numbers = number.split(".")
            if numbers and numbers[0].isdigit():
                number = int(numbers[0])

        for section in sections:
            for item in section:
                item["is_current"] = False
                if item["url"] == self.request.path:
                    item["is_current"] = True
                    continue
                if number and item.get("number") == number:
                    item["is_current"] = True
                    if number in (5, 6, 7, 8) and len(numbers) >= 2:
                        subchapters = [entries for title, entries in self.server.R.hierarchy if title == item["name"]][0]
                        item["subitems"] = [
                            {
                                "url": self._url_for("schema", name=subchapter[0].lower()),
                                "number": f"{number}.{index}",
                                "name": subchapter[0],
                                "is_current": str(index) == numbers[1],
                            }
                            for index, subchapter in enumerate(subchapters, 1)
                        ]
                    continue
                if "annex-b" in self.request.path and item.get("number") == "B":
                    item["is_current"] = True
                    item["subitems"] = [
                        dict(
                            subitem,
                            is_current=("annex-" + subitem["number"]).lower().replace(".", "") in self.request.path,
                        )
                        for subitem in self.ANNEX_B_NAVIGATION
                    ]
        return sections

    def annotate_hierarchy(self, data=None, start=1, number_path=None):
        level_2_headings = ("Schema Definition", "Types", "Entities", "Property Sets", "Quantity Sets", "Functions", "Rules")

        def items(d):
            if len(number_path or []) == 2:
                return [(heading, dict(d).get(heading, [])) for heading in level_2_headings]
            if isinstance(d, dict):
                return d.items()
            return [(entry, []) if isinstance(entry, str) else entry for entry in d]

        def get_url(idx, text):
            if len(number_path) == 0:
                return f"/chapter-{idx}/"
            if len(number_path) == 1:
                return f"/{text.lower()}/content.html"
            if len(number_path) == 2:
                fragment = (".".join([part[0] for part in number_path] + [str(idx)]) + "-" + text).replace(" ", "-")
                return f"/{number_path[1][1].lower()}/content.html#{fragment}"
            if len(number_path) == 3:
                return f"/lexical/{text}.htm"
            return None

        data = self.server.R.hierarchy if data is None else data
        number_path = [] if number_path is None else number_path

        return [
            self._toc_entry(
                text=name,
                number=".".join([part[0] for part in number_path] + [str(index)]),
                url=get_url(index, name),
                children=self.annotate_hierarchy(data=children, number_path=number_path + [(str(index), name)]),
            )
            for index, (name, children) in enumerate(items(data), start)
        ]

    def _make_annex_b_navigation(self):
        return [dict(item) for item in self.ANNEX_B_NAVIGATION]

    def _get_content_html(self, slug: str, require_number: bool = True):
        path = self.config.repo_root / "content" / f"{slug}.md"
        if not path.exists():
            self._abort(404)

        title = None
        number = None
        if require_number:
            if slug in self.CONTENT_NAMES:
                number = self.CONTENT_NAMES.index(slug) + 1
                title = self.NAVIGATION[1][number - 1]["name"]
            elif slug in self.CONTENT_NAMES_2:
                title = slug[:1].upper() + slug[1:]
                number = ""
            else:
                self._abort(404)

        content = path.read_text(encoding="utf-8")
        if content.startswith("!template"):
            content = self._render_string(content[len("!template") :].lstrip(), is_iso=False)

        process_quotes = slug != "terms_and_definitions"
        kwargs = {"number_headings": True, "chapter": (int(number), 1)} if slug == "terms_and_definitions" else {}
        rendered = self._render_string(content, base="", is_iso=False)
        html = self.server.process_markdown("", rendered, process_quotes=process_quotes, **kwargs)
        return path, title, number, html

    def _diagram_names(self) -> list[str]:
        diagram_dir = self.config.repo_root / "output" / "ifc4x3_add2.uml"
        return sorted(path.stem for path in diagram_dir.glob("*.png"))

    def _example_title(self, slug: str) -> str:
        return " ".join(part[:1].upper() + part[1:] for part in slug.split("-"))

    def _build_example_tree(self, return_list_and_tree: bool = False):
        examples = []
        for model in self.examples_models_root.glob("**/*.ifc"):
            readme = model.parent / "README.md"
            if readme.exists():
                examples.append(model.parent.relative_to(self.examples_models_root).as_posix())
        examples = sorted(set(examples))

        root = self._toc_entry("", number="E", children=[])
        for path in examples:
            current = root
            for component in Path(path).parts:
                title = self._example_title(component)
                child = next((entry for entry in current.children if entry.text == title), None)
                if child is None:
                    url = None
                    if component == Path(path).parts[-1]:
                        url = f"/annex_e/{path}.html"
                    child = self._toc_entry(
                        title,
                        url=url,
                        children=[],
                        number=f"{current.number}.{len(current.children) + 1}",
                    )
                    current.children.append(child)
                current = child

        if return_list_and_tree:
            return examples, root
        return root.children

    def _render_cover(self) -> StaticResponse:
        path, _, _, html = self._get_content_html("cover")
        return self._html_response(
            "cover.html",
            navigation=self.get_navigation(),
            content=html,
            path=self._repo_relative(path),
            subs=[],
            body_class="cover",
        )

    def _render_content(self, slug: str) -> StaticResponse:
        path, title, number, html = self._get_content_html(slug)
        return self._html_response(
            "static.html",
            navigation=self.get_navigation(),
            content=html,
            path=self._repo_relative(path),
            title=title,
            number=number,
            body_class=re.sub(r"[^a-z0-9]+", "-", slug.lower()),
        )

    def _render_property(self, prop: str) -> StaticResponse:
        translations = self.server.translate.get_translations(prop)
        safe_prop = "".join(char for char in prop if char.isalnum() or char == "_")
        path = self.config.repo_root / "docs" / "properties" / safe_prop[0].lower() / f"{safe_prop}.md"
        markdown = path.read_text(encoding="utf-8") if path.exists() else ""
        markdown = re.sub(self.server.DOC_ANNOTATION_PATTERN, "", markdown)
        property_sets = [[name] for name, definition in self.server.R.pset_definitions.items() if any(item["name"] == safe_prop for item in definition["properties"])]
        html = self.server.process_markdown(safe_prop, markdown)
        html += self.server.tabulate.tabulate(property_sets, headers=["Referenced in"], tablefmt="html")
        return self._html_response(
            "property.html",
            navigation=self.get_navigation(),
            content=html,
            number="",
            entity=safe_prop,
            translations=translations,
            path=self._repo_relative(path),
        )

    def _render_resource(self, resource: str) -> StaticResponse:
        translations = self.server.translate.get_translations(resource)
        try:
            index = self.server.name_to_number()[resource]
        except KeyError:
            self._abort(404)

        self.server.SectionNumberGenerator.set(index)
        self.server.SectionNumberGenerator.begin_subsection()
        definition_number = self.server.SectionNumberGenerator.generate()

        path = Path(self.server.get_resource_path(resource, abort_on_error=False) or "")
        markdown = path.read_text(encoding="utf-8") if path.exists() else ""
        markdown = re.sub(self.server.DOC_ANNOTATION_PATTERN, "", markdown)

        if "Entities" in path.as_posix():
            builder = self.server.resource_documentation_builder(resource)
            mvds = [
                {"abbr": "".join(self.server.re.findall(r"[A-Z]|(?<=-)[a-z]", name)), "cause": usage[resource]}
                for name, usage in self.server.R.mvd_entity_usage.items()
                if resource in usage
            ]
            is_product_or_type = False
            entity = resource
            while entity:
                entity = self.server.R.entity_supertype.get(entity)
                if entity in ("IfcProduct", "IfcTypeProduct"):
                    is_product_or_type = True
                    break

            return self._html_response(
                "entity.html",
                navigation=self.get_navigation(resource),
                number=index,
                definition_number=definition_number,
                definition=self.server.get_definition(resource, markdown),
                entity=resource,
                path=self._repo_relative(path),
                entity_inheritance=self.server.get_entity_inheritance(resource),
                attributes=self.server.get_attributes(resource, builder),
                formal_propositions=self.server.get_formal_propositions(resource, builder),
                property_sets=self.server.get_property_sets(resource, builder),
                concept_usage=self.server.get_concept_usage(resource, builder, markdown),
                examples=self.server.get_examples(resource),
                adoption=self.server.get_adoption(resource),
                formal_representation=self.server.get_formal_representation(resource),
                references=self.server.get_references(resource),
                changelog=self.server.get_changelog(resource),
                is_deprecated=resource in self.server.R.deprecated_entities,
                is_abstract=resource in self.server.R.abstract_entities,
                mvds=mvds,
                is_product_or_type=is_product_or_type,
                translations=translations,
            )

        if resource in self.server.R.pset_definitions:
            return self._html_response(
                "property.html",
                navigation=self.get_navigation(resource),
                content=self.server.get_definition(resource, markdown),
                number=index,
                definition_number=definition_number,
                entity=resource,
                path=self._repo_relative(path),
                applicability=self.server.get_applicability(resource),
                properties=self.server.get_properties(resource, markdown),
                changelog=self.server.get_changelog(resource),
                translations=translations,
            )

        builder = self.server.resource_documentation_builder(resource)
        return self._html_response(
            "type.html",
            navigation=self.get_navigation(resource),
            content=self.server.get_definition(resource, markdown),
            number=index,
            definition_number=definition_number,
            entity=resource,
            path=self._repo_relative(path),
            type_values=self.server.get_type_values(resource, markdown),
            formal_propositions=self.server.get_formal_propositions(resource, builder),
            formal_representation=self.server.get_formal_representation(resource),
            references=self.server.get_references(resource),
            changelog=self.server.get_changelog(resource),
        )

    def _render_concept_list(self) -> StaticResponse:
        path = self.config.repo_root / "docs" / "templates" / "README.md"
        html = self.server.process_markdown("", path.read_text(encoding="utf-8"))
        return self._html_response(
            "concept_listing.html",
            navigation=self.get_navigation(),
            content=html,
            path=self._repo_relative(path),
            title=self.chapter_lookup(number=4)["name"],
            number=4,
            sections=[
                {"cs": self.server.make_concept([""], exclude_partial=True).children},
                {
                    "title": "Partial Templates",
                    "number": "4.2",
                    "cs": self.server.make_concept(["Partial Templates"]).children,
                },
            ],
        )

    def _render_concept(self, concept_path: str) -> StaticResponse:
        docs_root = self.config.repo_root / "docs" / "templates"
        normalized = concept_path.replace("_", " ")
        number = "4"
        title = self.chapter_lookup(number=4)["name"]
        markdown_root = docs_root

        if normalized:
            parts = normalized.split("/")
            if parts[0] == "Partial Templates":
                number = "4.2"
                parts = parts[1:]
                normalized = "/".join(parts)
                markdown_root = docs_root / "Partial Templates"
                if not parts:
                    title = "Partial Templates"
            else:
                number = "4.1"

            if parts:
                title = parts[-1]
                for parent_path in itertools.accumulate([[part] for part in parts]):
                    choices = sorted(
                        entry
                        for entry in os.listdir(markdown_root.joinpath(*parent_path[:-1]))
                        if (markdown_root.joinpath(*parent_path[:-1], entry)).is_dir() and entry != "Partial Templates"
                    )
                    number += f".{choices.index(parent_path[-1]) + 1}"

        path = markdown_root / normalized / "README.md" if normalized else markdown_root / "README.md"
        diagram = None
        if path.exists():
            markdown = path.read_text(encoding="utf-8")
            if "concept {" in markdown:
                diagram_markdown = self.server.process_graphviz_concept("".join(char for char in normalized if char.isalnum()), markdown[markdown.index("```") :])
                diagram = self.server.process_markdown("", diagram_markdown)
                soup = BeautifulSoup(diagram)
                for svg in soup.find_all("svg"):
                    svg.attrs["width"] = f"{int(svg.attrs['width'][:-2]) // 4 * 3}px"
                    svg.attrs["height"] = f"{int(svg.attrs['height'][:-2]) // 4 * 3}px"
                diagram = str(soup)
                markdown = markdown[: markdown.index("```")]
            html = self.server.process_markdown("", markdown)
        else:
            html = ""

        xmi_concept = title.replace(" ", "")
        tables = ""
        for view_name, concepts in self.server.R.xmi_concepts.items():
            if xmi_concept not in concepts:
                continue
            tables += f"<h3>{self.server.separate_camel(view_name)}</h3>"
            headers, rows = self.server.create_concept_table(view_name, xmi_concept, None)
            if rows:
                tables += self.server.tabulate.tabulate(rows, headers=headers, tablefmt="unsafehtml")

        if not diagram and not BeautifulSoup(html).text.strip() and not tables:
            html = '<p class="search-skip">This section is intentionally left blank. This template merely serves as a grouping of sub templates.</p>'

        return self._html_response(
            "concept.html",
            navigation=self.get_navigation(number=number),
            content=html,
            diagram=diagram,
            tables=tables,
            path=self._repo_relative(path),
            title=title,
            number=number,
        )

    def _render_chapter(self, number: str) -> StaticResponse:
        try:
            chapter_number = int(number)
        except ValueError:
            self._abort(404)

        chapter = self.chapter_lookup(number=chapter_number)
        title = chapter["name"]
        category = title.split(" ")[0].lower()
        path = self.config.repo_root / "docs" / "schemas" / category / "README.md"
        if path.exists():
            soup = BeautifulSoup(self.server.markdown.markdown(path.read_text(encoding="utf-8")))
            heading = soup.find("h1")
            if heading:
                heading.decompose()
            html = str(soup)
        else:
            html = ""

        subchapters = [items for name, items in self.server.R.hierarchy if name == title][0]
        subs = [
            self._toc_entry(text=name, url=f"/{name.lower()}/content.html", number=f"{chapter_number}.{index}")
            for index, (name, _) in enumerate(subchapters, 1)
        ]

        return self._html_response(
            "chapter.html",
            navigation=self.get_navigation(number=chapter_number),
            content=html,
            path=self._repo_relative(path),
            title=title,
            number=chapter_number,
            subs=subs,
        )

    def _render_schema(self, name: str) -> StaticResponse:
        docs_root = self.config.repo_root / "docs" / "schemas"
        matches = [(title, items) for title, items in self.server.R.hierarchy if name in [entry[0].lower() for entry in items]]
        if not matches:
            self._abort(404)

        category_full, schemas = matches[0]
        category = category_full.split(" ")[0].lower()
        title, members = [entry for entry in schemas if entry[0].lower() == name][0]
        chapter = self.chapter_lookup(cat=category)

        n1 = chapter["number"]
        n2 = [schema_name for schema_name, _ in schemas].index(title) + 1
        number = f"{n1}.{n2}"
        path = docs_root / category / title / "README.md"

        self.server.SectionNumberGenerator.set(number)
        self.server.SectionNumberGenerator.begin_subsection()
        definition = None
        definition_number = None
        if path.exists():
            definition_number = self.server.SectionNumberGenerator.generate()
            definition = self.server.process_markdown("", path.read_text(encoding="utf-8"))

        order = ["Types", "Entities", "Property Sets", "Quantity Sets", "Functions", "Rules", "PropertyEnumerations"]
        categories = [
            self._toc_entry(
                text=group,
                number=f"{number}.{index}",
                children=[
                    self._toc_entry(text=resource, number=f"{number}.{index}.{subindex}", url=f"/lexical/{resource}.htm")
                    for subindex, resource in enumerate(members.get(group, []), 1)
                ],
            )
            for index, group in enumerate(order, 2)
        ]

        return self._html_response(
            "subchapter.html",
            navigation=self.get_navigation(number=number),
            definition=definition,
            path=self._repo_relative(path),
            title=title,
            number=number,
            subnumber=definition_number,
            categories=categories,
        )

    def _render_toc(self) -> StaticResponse:
        subs = list(self.NAVIGATION[1][0:4])
        subs.extend(self.annotate_hierarchy(start=5))
        return self._html_response(
            "chapter.html",
            navigation=self.get_navigation(),
            title="Contents",
            subs=subs,
        )

    def _render_annex_b(self) -> StaticResponse:
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=self._make_annex_b_navigation(),
            body_class="annex",
        )

    def _render_annex_b1(self) -> StaticResponse:
        def get_mvd_qualification(resource: str):
            return [
                {
                    "abbr": "".join(self.server.re.findall(r"[A-Z]|(?<=-)[a-z]", name)),
                    "cause": usage.get(resource),
                    "on": resource in usage,
                }
                for name, usage in self.server.R.mvd_entity_usage.items()
            ]

        def get_product_qualification(resource: str):
            entity = resource
            while entity:
                entity = self.server.R.entity_supertype.get(entity)
                if entity in ("IfcProduct", "IfcTypeProduct"):
                    return True
            return False

        items = [
            {
                "number": self.server.name_to_number()[name],
                "url": f"/lexical/{name}.htm",
                "name": name,
                "mvds": get_mvd_qualification(name),
                "is_product_or_type": get_product_qualification(name),
            }
            for name in self.server.entity_names()
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            is_dictionary=True,
            title="Entities",
            body_class="annex",
        )

    def _render_annex_b2(self) -> StaticResponse:
        items = [
            {"number": self.server.name_to_number()[name], "url": f"/lexical/{name}.htm", "name": name}
            for name in self.server.type_names()
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            is_dictionary=True,
            title="Types",
            body_class="annex",
        )

    def _render_annex_b3(self) -> StaticResponse:
        items = [
            {"number": self.server.name_to_number()[name], "url": f"/lexical/{name}.htm", "name": name}
            for name in sorted(self.server.R.pset_definitions.keys())
            if name in self.server.name_to_number()
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            is_dictionary=True,
            title="Property sets",
            body_class="annex",
        )

    def _render_annex_b4(self) -> StaticResponse:
        items = [
            {"number": "", "url": f"/property/{name}.htm", "name": name}
            for name in sorted({prop["name"] for definition in self.server.R.pset_definitions.values() for prop in definition["properties"]})
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            title="Properties",
            body_class="annex",
        )

    def _render_annex_b5(self) -> StaticResponse:
        items = [{"number": "", "url": f"/lexical/{name}.htm", "name": name} for name in self.server.function_names()]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            title="Functions",
            body_class="annex",
        )

    def _render_annex_b6(self) -> StaticResponse:
        items = [{"number": "", "url": f"/lexical/{name}.htm", "name": name} for name in self.server.rule_names()]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            title="Rules",
            body_class="annex",
        )

    def _render_annex_b7(self) -> StaticResponse:
        items = [
            {"number": "", "url": f"/lexical/{name}.htm", "name": name}
            for name in self.server.propertyenumeration_names()
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            title="Property Enumerations",
            body_class="annex",
        )

    def _render_annex_c(self) -> StaticResponse:
        entities = []
        indentation_map = {0: entities}
        path = self.config.code_dir / "inheritance_listing.txt"
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                line = line.rstrip("\n")
                padding = line.count(" ")
                entity = line.strip()
                data = {
                    "number": self.server.name_to_number()[entity],
                    "url": f"/lexical/{entity}.htm",
                    "name": entity,
                    "children": [],
                }
                if padding == 0:
                    entities.append(data)
                else:
                    indentation_map[padding - 1]["children"].append(data)
                indentation_map[padding] = data

        return self._html_response(
            "annex-c.html",
            navigation=self.get_navigation(),
            entities=entities,
            body_class="annex",
        )

    def _render_annex_d(self) -> StaticResponse:
        diagrams = [
            self._toc_entry(name, url=f"/annex_d/{name}.html", number=f"D.{index}")
            for index, name in enumerate(self._diagram_names(), 1)
        ]
        return self._html_response(
            "annex-d.html",
            navigation=self.get_navigation(),
            diagrams=diagrams,
            body_class="annex",
        )

    def _render_annex_d_diagram_page(self, name: str) -> StaticResponse:
        diagrams = self._diagram_names()
        if name not in diagrams:
            self._abort(404)
        return self._html_response(
            "annex-d-item.html",
            navigation=self.get_navigation(),
            name=name,
            number=diagrams.index(name) + 1,
            body_class="annex",
        )

    def _render_annex_e(self) -> StaticResponse:
        return self._html_response(
            "annex-e.html",
            navigation=self.get_navigation(),
            examples=self._build_example_tree(),
            body_class="annex",
        )

    def _render_annex_e_example_page(self, example: str) -> StaticResponse:
        examples, tree = self._build_example_tree(True)
        if example not in examples:
            self._abort(404)

        url_to_number = {}

        def visit(entry):
            if entry.url:
                url_to_number[entry.url] = entry.number
            for child in entry.children:
                visit(child)

        visit(tree)

        example_dir = self.examples_models_root / example
        path = example_dir / "README.md"
        parent_path = example_dir.parent / "README.md"
        html = self.server.process_markdown("", path.read_text(encoding="utf-8"))
        if parent_path.exists():
            html = self.server.process_markdown("", parent_path.read_text(encoding="utf-8")) + html

        candidates = list(example_dir.glob("*.ifc")) + list(example_dir.glob("*.xml"))
        code = candidates[0].read_text(encoding="ascii", errors="ignore")
        code = re.sub(r"(?<=FILE_SCHEMA\(\(')IFC\w+", self.server.SCHEMA_NAME, code)
        code = re.sub(r"(?<=FILE_SCHEMA \(\(')IFC\w+", self.server.SCHEMA_NAME, code)

        image_pattern = re.compile(r".*\.(png|jpg|jpeg)", re.IGNORECASE)
        images = [
            f"/examples/{example}/{candidate.name}"
            for candidate in sorted(example_dir.iterdir())
            if candidate.is_file() and image_pattern.match(candidate.name) and candidate.name.lower() != "thumb.png"
        ]

        return self._html_response(
            "annex-e-item.html",
            navigation=self.get_navigation(),
            content=html,
            path=path.resolve().relative_to(self.examples_repo_root).as_posix(),
            repo="buildingSMART/IFC4.3.x-sample-models",
            branch="main",
            title=self._example_title(Path(example).name),
            code=code,
            images=images,
            number=url_to_number[self.request.path],
            body_class="annex",
        )

    def _render_annex_f(self) -> StaticResponse:
        _, _, _, html = self._get_content_html("changelog", require_number=False)
        changelog_data = json.loads((self.config.code_dir / "changes_by_schema.json").read_text(encoding="utf-8"))
        changelogs = {"sections": []}
        self.server.SectionNumberGenerator.begin_subsection()
        for section in changelog_data:
            section_name = section[0]
            changes = section[1]
            changelogs["sections"].append(
                {
                    "name": section_name,
                    "changes": [
                        {
                            "entity": change[0],
                            "is_addition": "add" in change[1],
                            "is_deletion": "delet" in change[1],
                            "is_modification": "modif" in change[1],
                            "what_changed": change[2],
                            "description": change[3],
                        }
                        for change in changes
                    ],
                }
            )
        self.server.SectionNumberGenerator.end_subsection()
        return self._html_response(
            "annex-f.html",
            definition=html,
            navigation=self.get_navigation(),
            changelogs=changelogs,
            body_class="annex",
        )

    def _render_index(self) -> StaticResponse:
        items = [
            {"number": "", "title": f"Listing of {kind}", "url": f"listing-{kind}.html"}
            for kind in ("references", "figures", "tables")
        ]
        return self._html_response("index.html", navigation=self.get_navigation(), items=items, title="Index")

    def _render_search(self) -> StaticResponse:
        return self._html_response(
            "search.html",
            navigation=self.get_navigation(),
            title="Search",
            body_class="search-page",
        )

    def _render_listing(self, kind: str) -> StaticResponse:
        items = list(self.listing_payloads.get(kind, []))
        if kind == "references":
            grouped = []
            for title, group in itertools.groupby(items, key=lambda item: item["title"]):
                refs = []
                for entry in group:
                    url = entry["url"]
                    if url.startswith("/lexical/") and url.endswith(".htm"):
                        refs.append(url[len("/lexical/") : -4])
                grouped.append(
                    {
                        "number": title,
                        "url": "",
                        "subitems": [{"url": f"/lexical/{resource}.htm", "title": resource} for resource in refs],
                    }
                )
            items = [item for item in grouped if not (len(item["subitems"]) == 1 and item["subitems"][0]["title"] == item["number"])]
        return self._html_response(
            "index.html",
            navigation=self.get_navigation(),
            items=items,
            title=f"Listing of {kind}",
        )


_EMPTY_LISTING_PAYLOADS = {"references": [], "figures": [], "tables": []}
_WORKER_RENDERERS: dict[BuildConfig, StaticTemplateRenderer] = {}
_WORKER_REFINERS: dict[tuple[BuildConfig, tuple[str, ...]], HtmlRefiner] = {}


def _destination_for(config: BuildConfig, public_path: str) -> Path:
    if public_path == "/":
        return config.output_dir / "index.html"
    stripped = public_path.lstrip("/")
    target = config.output_dir / stripped
    if public_path.endswith("/"):
        return target / "index.html"
    return target


def _load_support_module(config: BuildConfig, module_name: str):
    if str(config.code_dir) not in sys.path:
        sys.path.insert(0, str(config.code_dir))
    if "concept_extractor" not in sys.modules:
        stub = ModuleType("concept_extractor")
        stub.extractor = None
        sys.modules["concept_extractor"] = stub

    if module_name == "render_support":
        module = importlib.import_module("render_support")
    else:
        module = sys.modules.get(module_name)
        if module is None:
            spec = importlib.util.spec_from_file_location(module_name, str(config.code_dir / "render_support.py"))
            if spec is None or spec.loader is None:
                raise RuntimeError("Could not load render support module")
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)

    module.base = ""
    module.is_iso = False
    module.is_package = False
    _patch_support_module(module)
    return module


def _patch_support_module(support) -> None:
    def process_graphviz_concept(name, md):
        graphviz_code = filter(lambda s: s.strip().startswith("concept"), support.re.findall("```(.*?)```", md, support.re.S))

        def replace_edge(match):
            is_direct_attribute = True
            entity = match.group(1).split("_")[0]
            attribute = match.group(2)
            while entity:
                data = support.R.entity_attributes.get(f"{entity}.{attribute}", None)
                if data:
                    is_direct_attribute = data[0] == "forward"
                    break
                entity = support.R.entity_supertype.get(entity)
            endpoint = match.group(3)
            if ":" not in endpoint:
                endpoint += ":" + endpoint.split("_")[0]
            result = f"{match.group(1)}:{match.group(2)}1 -> {endpoint}"
            if not is_direct_attribute:
                result += "[dir=back]"
            return result

        def replace_edge2(match):
            return f"{match.group(1)} -> {match.group(2)}:{match.group(3)}0"

        name_token = "c" + support.hashlib.sha1(name.encode("utf-8")).hexdigest()[:16]

        for c in graphviz_code:
            hash_value = support.hashlib.sha256(c.encode("utf-8")).hexdigest()
            fn = support.os.path.join("svgs", name_token + "_" + hash_value + ".dot")
            c2 = c.replace("concept", "digraph")
            c2 = support.re.sub("(?<=\\w)\\-(?=\\w)", "", c2)

            nodes = set(n.split(":")[0] for n in (support.re.findall("([\\:\\w]+)\\s*\\->", c2) + support.re.findall("\\->\\s*([\\:\\w]+)", c2)))
            node_ports = {n: [] for n in nodes}
            [
                node_ports[n.split(":")[0]].append(n.split(":")[1])
                for n in (support.re.findall("([\\:\\w]+)\\s*\\->", c2) + support.re.findall("\\->\\s*([\\:\\w]+)", c2))
                if len(n.split(":")) > 1
            ]

            c2 = support.re.sub(r"(\w+)\:(\w+)\s*\->\s*([\:\w]+)", replace_edge, c2)
            c2 = support.re.sub(r"([\w\:]+)\s*\->\s*(\w+)\:(\w+)", replace_edge2, c2)

            bindings = {}
            for ent, attr, bind in support.re.findall(r'(\w+)\:(\w+)\[binding="([\w_]+)"\]', c2):
                bindings[(ent, attr)] = bind
            c2 = support.re.sub(r'\w+\:\w+\[binding="[\w_]+"\]', "", c2)

            graph = support.pydot.graph_from_dot_data(c2)[0]

            graph.set_node_defaults(shape="plaintext", width="3")
            graph.set_nodesep("0.1")
            graph.set_splines("polyline")
            graph.set_rankdir("LR")

            for node in nodes:
                if node.startswith("Ifc"):
                    graph.add_node(support.pydot.Node(node, label=support.create_entity_definition(node, bindings, node_ports.get(node, []))))
                elif node.startswith("constraint_"):
                    graph.get_node(node)[0].set_fillcolor("#ffaaaa")
                    graph.get_node(node)[0].set_shape("rect")
                    graph.get_node(node)[0].set_style("filled")
                else:
                    url = {}
                    label = node.replace("_", " ")
                    concept_node = support.make_concept(["Partial Templates"], exclude_partial=False).find(label)
                    if concept_node:
                        url = {"URL": concept_node.url}
                    graph.add_node(support.pydot.Node(node, label=label, fillcolor="#aaffaa", shape="rect", style="filled", **url))

            graph.obj_dict["nodes"]["node"][0]["sequence"] = -1

            with open(fn, "w", encoding="utf-8") as handle:
                handle.write(graph.to_string())
            md = md.replace("```%s```" % c, "![](/svgs/%s_%s.svg)" % (name_token, hash_value))

            support.subprocess.call([support.shutil.which("dot") or "dot", "-O", "-Tsvg", "-Gbgcolor=#ffffff00", fn])

        return md

    support.process_graphviz_concept = process_graphviz_concept


def _worker_renderer(config: BuildConfig) -> StaticTemplateRenderer:
    renderer = _WORKER_RENDERERS.get(config)
    if renderer is None:
        module_name = f"_html_generator_server_worker_{os.getpid()}"
        renderer = StaticTemplateRenderer(config, _load_support_module(config, module_name))
        _WORKER_RENDERERS[config] = renderer
    return renderer


def _worker_refiner(config: BuildConfig, resource_names: tuple[str, ...]) -> HtmlRefiner:
    key = (config, resource_names)
    refiner = _WORKER_REFINERS.get(key)
    if refiner is None:
        refiner = HtmlRefiner(resource_names=resource_names)
        _WORKER_REFINERS[key] = refiner
    return refiner


def _render_html_path_task(
    config: BuildConfig,
    public_path: str,
    resource_names: tuple[str, ...],
    listing_payloads: dict[str, list[dict[str, str]]] | None,
):
    os.chdir(config.code_dir)

    renderer = _worker_renderer(config)
    renderer.set_listing_payloads(listing_payloads or _EMPTY_LISTING_PAYLOADS)

    response = renderer.render_path(public_path)
    html = response.body.decode("utf-8")

    refiner = _worker_refiner(config, resource_names)
    result = refiner.refine(public_path, html)

    destination = _destination_for(config, public_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(result.html, encoding="utf-8")

    return result


class StaticSiteBuilder:
    def __init__(self, config: BuildConfig):
        self.config = config
        self._catalog = None
        self.collector = ListingCollector()
        self.errors: list[tuple[str, int]] = []

    def build(self) -> dict[str, int]:
        self.config.output_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(self.config.code_dir)
        self.errors = []
        self.collector = ListingCollector()

        print(1)

        self._prepare_translations(self.catalog)
        self._prepare_generated_assets()
        resource_names = tuple(sorted(self._resource_names(self.catalog)))

        print(2)

        self._copy_static_support_files()
        self._render_html_paths(self._content_paths(), collect=True, resource_names=resource_names)

        print(3)

        payloads = self.collector.payloads()
        self._write_listing_json(payloads)
        self._render_html_paths(self._listing_paths(), collect=False, listing_payloads=payloads, resource_names=resource_names)
        self._render_html_paths(self._utility_paths(), collect=False, resource_names=resource_names)

        print(4)

        self._copy_generated_svgs()
        self._build_search_index()

        return {
            "written": len([path for path in self.config.output_dir.rglob("*") if path.is_file()]),
            "errors": len(self.errors),
        }

    @property
    def catalog(self):
        if self._catalog is None:
            self._catalog = _load_support_module(self.config, "render_support")
        return self._catalog

    def _prepare_translations(self, support) -> None:
        compiled_dir = Path(support.translate.TRANSLATIONS_BUILD_DIR)
        if compiled_dir.exists() and any(compiled_dir.rglob("*.mo")):
            return
        support.translate.build_cache(jobs=1, pool="thread")

    def _prepare_generated_assets(self) -> None:
        (self.config.code_dir / "svgs").mkdir(parents=True, exist_ok=True)

        psd_zip = self.config.repo_root / "output" / "psd.zip"
        if psd_zip.exists() or (self.config.code_dir / "psd.zip").exists():
            return

        psd_zip.parent.mkdir(parents=True, exist_ok=True)

        for source_dir in (
            self.config.repo_root / "output" / "psd",
            self.config.code_dir / "psd_new",
            self.config.code_dir / "psd_old",
        ):
            if not source_dir.is_dir():
                continue
            archive = shutil.make_archive(
                str(psd_zip.with_suffix("")),
                "zip",
                root_dir=source_dir,
            )
            if Path(archive) != psd_zip:
                Path(archive).replace(psd_zip)
            break

    def _resource_names(self, support) -> set[str]:
        names = set(support.name_to_number().keys())
        names.update(support.R.entity_definitions.keys())
        names.update(support.R.pset_definitions.keys())
        names.update(support.R.type_values.keys())
        return names

    def _content_paths(self) -> list[str]:
        seeds = [
            "/",
            "/toc.html",
            "/content/foreword.htm",
            "/content/introduction.htm",
            "/content/scope.htm",
            "/content/normative_references.htm",
            "/content/terms_and_definitions.htm",
            "/content/bibliography.htm",
            "/concepts/content.html",
            "/chapter-5/",
            "/chapter-6/",
            "/chapter-7/",
            "/chapter-8/",
            "/annex-a.html",
            "/annex-a-express.html",
            "/annex-a-xsd.html",
            "/annex-b.html",
            "/annex-b1.html",
            "/annex-b2.html",
            "/annex-b3.html",
            "/annex-b4.html",
            "/annex-b5.html",
            "/annex-b6.html",
            "/annex-b7.html",
            "/annex-c.html",
            "/annex-d.html",
            "/annex-e.html",
            "/annex-f.html",
        ]
        seeds.extend(self._sample_paths(self._schema_paths()))
        seeds.extend(self._sample_paths(self._resource_paths()))
        seeds.extend(self._sample_paths(self._property_paths()))
        seeds.extend(self._sample_paths(self._concept_paths()))
        seeds.extend(self._sample_paths(self._example_paths()))
        seeds.extend(self._sample_paths(self._diagram_page_paths()))

        seen = set()
        ordered = []
        for path in seeds:
            if path not in seen:
                ordered.append(path)
                seen.add(path)
        return ordered

    def _sample_paths(self, paths: list[str]) -> list[str]:
        if self.config.sample_percent >= 100.0 or len(paths) <= 1:
            return paths

        target_count = max(1, int(round(len(paths) * (self.config.sample_percent / 100.0))))
        if target_count >= len(paths):
            return paths

        indices = sorted({min(int(i * len(paths) / target_count), len(paths) - 1) for i in range(target_count)})
        return [paths[index] for index in indices]

    def _listing_paths(self) -> list[str]:
        return ["/index.htm", "/listing-references.html", "/listing-figures.html", "/listing-tables.html"]

    def _utility_paths(self) -> list[str]:
        return ["/search.html"]

    def _schema_paths(self) -> list[str]:
        return [
            f"/{schema_name.lower()}/content.html"
            for _, schemas in self.catalog.R.hierarchy
            for schema_name, _ in schemas
        ]

    def _resource_paths(self) -> list[str]:
        return [f"/lexical/{name}.htm" for name in sorted(self.catalog.name_to_number().keys())]

    def _property_paths(self) -> list[str]:
        property_names = sorted(
            {
                prop["name"]
                for definition in self.catalog.R.pset_definitions.values()
                for prop in definition["properties"]
            }
        )
        return [f"/property/{name}.htm" for name in property_names]

    def _concept_paths(self) -> list[str]:
        templates_root = self.config.repo_root / "docs" / "templates"
        paths = []
        for readme in sorted(templates_root.glob("**/README.md")):
            if readme.parent == templates_root:
                continue
            relative = readme.parent.relative_to(templates_root).as_posix().replace(" ", "_")
            paths.append(f"/concepts/{relative}/content.html")
        return paths

    def _example_paths(self) -> list[str]:
        examples_root = self.config.repo_root.parent / "examples" / "models"
        paths = []
        if not examples_root.exists():
            return paths
        for model in sorted(examples_root.glob("**/*.ifc")):
            if (model.parent / "README.md").exists():
                relative = model.parent.relative_to(examples_root).as_posix()
                paths.append(f"/annex_e/{relative}.html")
        return sorted(set(paths))

    def _diagram_page_paths(self) -> list[str]:
        diagram_root = self.config.repo_root / "output" / "ifc4x3_add2.uml"
        if not diagram_root.exists():
            return []
        return [f"/annex_d/{path.stem}.html" for path in sorted(diagram_root.glob("*.png"))]

    def _search_source_paths(self) -> list[str]:
        excluded = {"/toc.html", "/search.html"}
        return [
            public_path
            for public_path in self._content_paths()
            if public_path not in excluded and not public_path.startswith("/annex")
        ]

    def _render_html_paths(
        self,
        public_paths: list[str],
        *,
        collect: bool,
        resource_names: tuple[str, ...],
        listing_payloads: dict[str, list[dict[str, str]]] | None = None,
    ) -> None:
        if self.config.profile:
            for public_path in public_paths:
                try:
                    result = _render_html_path_task(self.config, public_path, resource_names, listing_payloads)
                except RenderAbort as exc:
                    self.errors.append((public_path, exc.status_code))
                    continue
                if collect:
                    self.collector.merge(result)
            return

        with ProcessPoolExecutor(max_workers=self.config.threads) as executor:
            futures = {
                executor.submit(_render_html_path_task, self.config, public_path, resource_names, listing_payloads): public_path
                for public_path in public_paths
            }
            for future in as_completed(futures):
                public_path = futures[future]
                try:
                    result = future.result()
                except RenderAbort as exc:
                    self.errors.append((public_path, exc.status_code))
                    continue
                if collect:
                    self.collector.merge(result)

    def _write_listing_json(self, payloads: dict[str, list[dict[str, str]]]) -> None:
        for kind, payload in payloads.items():
            path = self.config.code_dir / f"listing_{kind}.json"
            path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _build_search_index(self) -> None:
        search_builder = SearchIndexBuilder(self.config.output_dir)
        search_builder.write(
            self._search_source_paths(),
            self.config.output_dir / "assets" / "search" / "search-index.json",
        )

    def _copy_static_support_files(self) -> None:
        self._copy_tree(self.config.repo_root / "docs" / "assets", self.config.output_dir / "assets")
        self._copy_tree(self.config.repo_root / "docs" / "figures", self.config.output_dir / "figures")
        self._copy_tree(self.config.repo_root.parent / "examples" / "models", self.config.output_dir / "examples")
        self._copy_tree(self.config.repo_root / "output" / "bsdd", self.config.output_dir / "bsdd")

        self._copy_file(_generated_file(self.config, "IFC.exp"), self.config.output_dir / f"{self.catalog.SCHEMA_NAME}.exp")
        self._copy_file(_generated_file(self.config, "IFC.xsd"), self.config.output_dir / f"{self.catalog.SCHEMA_NAME}.xsd")
        self._copy_file(_generated_file(self.config, "psd.zip"), self.config.output_dir / "annex-a-psd.zip")

        diagram_root = self.config.repo_root / "output" / "ifc4x3_add2.uml"
        annex_d_root = self.config.output_dir / "annex_d"
        if diagram_root.exists():
            annex_d_root.mkdir(parents=True, exist_ok=True)
            for path in diagram_root.glob("*.png"):
                self._copy_file(path, annex_d_root / path.name)

    def _copy_generated_svgs(self) -> None:
        self._copy_tree(self.config.code_dir / "svgs", self.config.output_dir / "svgs")

    def _copy_tree(self, source: Path, destination: Path) -> None:
        if source.exists():
            shutil.copytree(source, destination, dirs_exist_ok=True)

    def _copy_file(self, source: Path, destination: Path) -> None:
        if not source.exists():
            return
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
