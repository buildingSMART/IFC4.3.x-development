import functools

import ifcopenshell
import ifcopenshell.mvd as mvd
from ifcopenshell.express import parse as express_parse

from collections import defaultdict

W = ifcopenshell.ifcopenshell_wrapper


def run(schema_fn, mvdxml_fn, concept_subset=None):

    entities = set()
    types = set()
    causes = defaultdict(set)

    def collect_entities(cause, rule, parent):
        if rule.tag == "EntityRule":
            entities.add(rule.attribute)
            causes[rule.attribute].add(cause)

    """
    visited_templates = set()

    concept_roots = list(mvd.concept_root.parse(mvdxml_fn))
    for cr in concept_roots:
        if concept_subset is not None and cr.name not in concept_subset:
            continue
        entities.add(cr.entity)
        causes[cr.entity].add('root')
        for c in cr.concepts():
            ref = c.concept_node.getElementsByTagNameNS("*","Template")[0].attributes['ref'].value
            if ref in visited_templates:
                continue
            visited_templates.add(ref)
            tmpl = c.template()
            entities.add(tmpl.entity)
            tmpl.traverse(functools.partial(collect_entities, c.name))
    """

    dom = mvd.parse(mvdxml_fn)

    class collector:
        def template(self, id, visited):
            for node in dom.getElementsByTagNameNS("*", "ConceptTemplate"):
                if node.attributes["uuid"].value == id:
                    t = mvd.template(self, node)
                    t.parse(visited=visited)
                    return t

    templs = list(
        map(
            functools.partial(mvd.template, collector()),
            filter(
                lambda root: root.attributes.get("applicableEntity"),
                dom.getElementsByTagNameNS("*", "ConceptTemplate"),
            ),
        )
    )

    for t in templs:
        if t.name.replace(" ", "") in concept_subset:
            t.root = t.root.cloneNode(deep=True)
            try:
                t.root.removeChild(t.root.getElementsByTagName("SubTemplates")[0])
            except IndexError as e:
                pass
            t.parse()
            t.traverse(functools.partial(collect_entities, t.name))

    builder = express_parse(schema_fn)
    ifcopenshell.register_schema(builder)
    S = ifcopenshell.ifcopenshell_wrapper.schema_by_name(builder.schema_name)

    def yield_supertypes(en):
        yield en.name()
        if en.supertype():
            yield from yield_supertypes(en.supertype())

    entities, pass1 = set(), sorted(entities)

    for en in pass1:
        decl = S.declaration_by_name(en)
        if isinstance(decl, W.entity):
            for st in yield_supertypes(decl):
                entities.add(st)
                if st != en:
                    causes[st].add(en)

    def visit_typedecl(ty, cause=None):
        if isinstance(ty, W.named_type):
            visit_typedecl(ty.declared_type(), cause=cause)
        elif isinstance(ty, W.type_declaration):
            types.add(ty.name())
            causes[ty.name()].add(cause)
        elif isinstance(ty, W.aggregation_type):
            visit_typedecl(ty.type_of_element(), cause=cause)
        elif isinstance(ty, W.entity):
            visit_entity(ty, cause=cause)
        elif isinstance(ty, W.enumeration_type):
            types.add(ty.name())
            causes[ty.name()].add(cause)
        elif isinstance(ty, W.simple_type):
            pass
        elif isinstance(ty, W.select_type):
            # @nb this is important, select types do *not* result
            # in broadening the mvd scope. Templates need explicitly
            # incorporate selected subtypes for them to be in scope.

            # causes[ty.name()].add(cause)
            # for dd in ty.select_list():
            #     visit_typedecl(dd, cause=ty.name())
            pass
        else:
            breakpoint()

    visited = set()

    def visit_entity(en, cause=None):
        if en.name() in visited:
            return
        visited.add(en.name())
        entities.add(en.name())
        causes[en.name()].add(cause)
        # print(en.name())
        for attr in en.attributes():
            # print(attr.name())
            visit_typedecl(attr.type_of_attribute(), f"{en.name()}.{attr.name()}")

    for en in list(entities):
        decl = S.declaration_by_name(en)
        visit_entity(decl)

    # for en in sorted(entities):
    #     print(en)

    return {k: sorted(filter(None, v)) for k, v in causes.items()}


if __name__ == "__main__":
    import sys
    import json

    schema_fn, mvdxml_fn = sys.argv[1:]

    with open("xmi_mvd_concepts.json", "r") as f:
        mvds = json.load(f)

    usage = {}
    for nm, concepts in mvds.items():
        usage[nm] = run(schema_fn, mvdxml_fn, concepts)

    with open("mvd_entity_usage.json", "w") as f:
        json.dump(usage, f, indent=1)
