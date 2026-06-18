from pathlib import Path

from tools import reopen_prs
from tools.reopen_prs import ClosedPullRequest


def pr(number, *, state="CLOSED", merged_at=None):
    return ClosedPullRequest(
        number=number,
        title=f"PR {number}",
        state=state,
        is_draft=False,
        closed_at="2026-06-15T00:00:00Z",
        merged_at=merged_at,
        base_ref="main",
        head_ref=f"topic-{number}",
        url=f"https://example.test/pull/{number}",
    )


def test_partition_only_reopens_closed_unmerged_prs():
    closed = pr(1)
    merged = pr(2, state="MERGED", merged_at="2026-06-15T00:00:00Z")

    eligible, skipped = reopen_prs.partition_pull_requests([closed, merged])

    assert eligible == [closed]
    assert skipped == [merged]


def test_reopen_continues_after_failure(tmp_path, monkeypatch):
    calls = []

    def fake_run(command, _repo, check=False):
        calls.append(command)
        if command[3] == "2":
            return type(
                "Result",
                (),
                {"returncode": 1, "stdout": "", "stderr": "cannot reopen"},
            )()
        return type(
            "Result", (), {"returncode": 0, "stdout": "ok", "stderr": ""}
        )()

    monkeypatch.setattr(reopen_prs, "_run", fake_run)

    reopened, failures = reopen_prs.reopen_pull_requests(
        tmp_path,
        "owner/repo",
        [pr(1), pr(2), pr(3)],
        comment="reopening",
    )

    assert [item.number for item in reopened] == [1, 3]
    assert [(item.number, message) for item, message in failures] == [
        (2, "cannot reopen")
    ]
    assert calls[0][-2:] == ["--comment", "reopening"]


def test_dry_run_does_not_reopen(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(reopen_prs, "_repo_root", lambda: tmp_path)
    monkeypatch.setattr(
        reopen_prs, "_remote_name", lambda _repo, remote: remote or "origin"
    )
    monkeypatch.setattr(
        reopen_prs,
        "_repository_name",
        lambda _repo, _remote: "owner/repo",
    )
    monkeypatch.setattr(
        reopen_prs,
        "list_closed_pull_requests",
        lambda *_args, **_kwargs: [pr(1)],
    )
    called = []
    monkeypatch.setattr(
        reopen_prs,
        "reopen_pull_requests",
        lambda *_args, **_kwargs: called.append(True),
    )

    assert reopen_prs.main(["origin"]) == 0
    assert called == []
    assert "Dry run only" in capsys.readouterr().out


def test_execute_yes_reopens_without_prompt(tmp_path, monkeypatch):
    monkeypatch.setattr(reopen_prs, "_repo_root", lambda: tmp_path)
    monkeypatch.setattr(
        reopen_prs, "_remote_name", lambda _repo, remote: remote or "origin"
    )
    monkeypatch.setattr(
        reopen_prs,
        "_repository_name",
        lambda _repo, _remote: "owner/repo",
    )
    monkeypatch.setattr(
        reopen_prs,
        "list_closed_pull_requests",
        lambda *_args, **_kwargs: [pr(1)],
    )
    monkeypatch.setattr(
        reopen_prs,
        "_confirm",
        lambda *_args: (_ for _ in ()).throw(AssertionError("prompted")),
    )
    reopened = []
    monkeypatch.setattr(
        reopen_prs,
        "reopen_pull_requests",
        lambda *_args, **_kwargs: (reopened.append(1) or ([pr(1)], [])),
    )

    assert reopen_prs.main(["origin", "--execute", "--yes"]) == 0
    assert reopened == [1]
