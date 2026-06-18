"""Bulk-reopen closed, unmerged pull requests for a GitHub remote."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

try:
    from .git_ifc import (
        WorkflowError,
        _remote_name,
        _repository_name,
        _run,
    )
    from .xmi_merge import _repo_root
except ImportError:  # Executed directly instead of as a package.
    from git_ifc import (  # type: ignore[no-redef]
        WorkflowError,
        _remote_name,
        _repository_name,
        _run,
    )
    from xmi_merge import _repo_root  # type: ignore[no-redef]

PR_JSON_FIELDS = (
    "number,title,state,isDraft,closedAt,mergedAt,"
    "baseRefName,headRefName,url"
)


@dataclass(frozen=True)
class ClosedPullRequest:
    number: int
    title: str
    state: str
    is_draft: bool
    closed_at: str | None
    merged_at: str | None
    base_ref: str
    head_ref: str
    url: str

    @property
    def can_reopen(self) -> bool:
        return self.state == "CLOSED" and self.merged_at is None

    @classmethod
    def from_gh(cls, value: dict[str, Any]) -> ClosedPullRequest:
        return cls(
            number=int(value["number"]),
            title=str(value["title"]),
            state=str(value["state"]),
            is_draft=bool(value["isDraft"]),
            closed_at=value.get("closedAt"),
            merged_at=value.get("mergedAt"),
            base_ref=str(value["baseRefName"]),
            head_ref=str(value["headRefName"]),
            url=str(value["url"]),
        )


def list_closed_pull_requests(
    repo_root: Path,
    repository: str,
    *,
    base: str | None = None,
    limit: int = 1000,
) -> list[ClosedPullRequest]:
    command = [
        "gh",
        "pr",
        "list",
        "--repo",
        repository,
        "--state",
        "closed",
        "--limit",
        str(limit),
        "--json",
        PR_JSON_FIELDS,
    ]
    if base:
        command.extend(["--base", base])
    process = _run(command, repo_root)
    return [
        ClosedPullRequest.from_gh(value)
        for value in json.loads(process.stdout)
    ]


def partition_pull_requests(
    pull_requests: Sequence[ClosedPullRequest],
) -> tuple[list[ClosedPullRequest], list[ClosedPullRequest]]:
    eligible = [pr for pr in pull_requests if pr.can_reopen]
    skipped = [pr for pr in pull_requests if not pr.can_reopen]
    return eligible, skipped


def _print_plan(
    repository: str,
    remote: str,
    eligible: Sequence[ClosedPullRequest],
    skipped: Sequence[ClosedPullRequest],
) -> None:
    print(f"Repository: {repository} (remote {remote})")
    print(f"Closed, unmerged PRs to reopen: {len(eligible)}")
    for pr in eligible:
        draft = " [draft]" if pr.is_draft else ""
        print(
            f"  #{pr.number} {pr.head_ref} -> {pr.base_ref}: "
            f"{pr.title}{draft}"
        )
    if skipped:
        print(f"Merged PRs skipped: {len(skipped)}")
        for pr in skipped:
            print(f"  #{pr.number} {pr.title}")


def _confirm(repository: str, count: int) -> bool:
    if not sys.stdin.isatty():
        raise WorkflowError(
            "refusing non-interactive execution without --yes"
        )
    answer = input(
        f"Reopen {count} pull request(s) in {repository}? [y/N] "
    ).strip()
    return answer.casefold() in {"y", "yes"}


def reopen_pull_requests(
    repo_root: Path,
    repository: str,
    pull_requests: Sequence[ClosedPullRequest],
    *,
    comment: str | None = None,
) -> tuple[list[ClosedPullRequest], list[tuple[ClosedPullRequest, str]]]:
    reopened: list[ClosedPullRequest] = []
    failures: list[tuple[ClosedPullRequest, str]] = []
    for pr in pull_requests:
        command = [
            "gh",
            "pr",
            "reopen",
            str(pr.number),
            "--repo",
            repository,
        ]
        if comment:
            command.extend(["--comment", comment])
        process = _run(command, repo_root, check=False)
        if process.returncode:
            message = (process.stderr or process.stdout).strip()
            failures.append((pr, message or "gh pr reopen failed"))
            print(f"FAILED #{pr.number}: {failures[-1][1]}", file=sys.stderr)
            continue
        reopened.append(pr)
        print(f"Reopened #{pr.number}: {pr.title}")
    return reopened, failures


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "remote",
        nargs="?",
        help="Git remote, default: ifc.remote or origin",
    )
    parser.add_argument("--base", help="Only reopen PRs targeting this branch")
    parser.add_argument("--limit", type=int, default=1000)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Perform the reopen operations; otherwise show a dry run",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip the interactive confirmation; requires --execute",
    )
    parser.add_argument(
        "--comment",
        help="Comment added by GitHub when reopening each PR",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = build_parser().parse_args(argv)
        if args.yes and not args.execute:
            raise WorkflowError("--yes requires --execute")
        repo_root = _repo_root()
        remote = _remote_name(repo_root, args.remote)
        repository = _repository_name(repo_root, remote)
        pull_requests = list_closed_pull_requests(
            repo_root,
            repository,
            base=args.base,
            limit=args.limit,
        )
        eligible, skipped = partition_pull_requests(pull_requests)
        _print_plan(repository, remote, eligible, skipped)

        if not args.execute:
            print("Dry run only. Add --execute to reopen the eligible PRs.")
            return 0
        if not eligible:
            print("No closed, unmerged pull requests are eligible to reopen.")
            return 0
        if not args.yes and not _confirm(repository, len(eligible)):
            print("Cancelled.")
            return 1

        reopened, failures = reopen_pull_requests(
            repo_root,
            repository,
            eligible,
            comment=args.comment,
        )
        print(
            f"Completed: {len(reopened)} reopened, "
            f"{len(failures)} failed, {len(skipped)} merged PRs skipped."
        )
        return 1 if failures else 0
    except WorkflowError as exc:
        print(f"reopen-prs: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
