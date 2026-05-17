from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


CITE_RE = re.compile(r"\\(?:[A-Za-z]*cite[A-Za-z]*)\{([^}]*)\}")
FIG_LABEL_RE = re.compile(r"\\label\{(fig:[^}]+)\}")
FIG_REF_RE = re.compile(r"\\(?:ref|autoref|cref)\{(fig:[^}]+)\}")
BIB_KEY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)", re.MULTILINE)
INDEX_ROW_RE = re.compile(r"\|\s*\d+\s*\|\s*([^|]+?)\s*\|.*?\|\s*\[[^\]]+\]\(([^)]+)\)\s*\|")


def read_all_tex(project_root: Path) -> str:
    docs = project_root / "docs"
    return "\n".join(path.read_text(encoding="utf-8") for path in docs.rglob("*.tex"))


def parse_citations(tex: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for match in CITE_RE.finditer(tex):
        for key in match.group(1).split(","):
            key = key.strip()
            if key:
                counts[key] += 1
    return counts


def parse_bib_keys(project_root: Path) -> set[str]:
    bib = project_root / "refs" / "bib" / "references.bib"
    if not bib.exists():
        return set()
    return set(BIB_KEY_RE.findall(bib.read_text(encoding="utf-8")))


def parse_index(project_root: Path) -> dict[str, Path]:
    index = project_root / "refs" / "notes" / "paper_index.md"
    if not index.exists():
        return {}
    text = index.read_text(encoding="utf-8")
    result: dict[str, Path] = {}
    for key, rel_path in INDEX_ROW_RE.findall(text):
        result[key.strip()] = (index.parent / rel_path.strip()).resolve()
    return result


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python check_review_project.py <project_root>")
        return 2

    root = Path(sys.argv[1]).resolve()
    tex = read_all_tex(root)
    citations = parse_citations(tex)
    bib_keys = parse_bib_keys(root)
    index = parse_index(root)
    fig_labels = Counter(FIG_LABEL_RE.findall(tex))
    fig_refs = Counter(FIG_REF_RE.findall(tex))

    problems: list[str] = []

    for key, count in sorted(citations.items()):
        if count > 2:
            problems.append(f"citation overuse: {key} appears {count} times")
        if key not in bib_keys:
            problems.append(f"missing bib entry: {key}")
        if key not in index:
            problems.append(f"missing paper-index entry: {key}")
        elif not index[key].exists():
            problems.append(f"missing downloaded PDF for {key}: {index[key]}")

    for label, count in sorted(fig_labels.items()):
        if count != 1:
            problems.append(f"duplicate figure label: {label} defined {count} times")
        ref_count = fig_refs.get(label, 0)
        if ref_count != 1:
            problems.append(f"figure reference count: {label} referenced {ref_count} times")

    for ref, count in sorted(fig_refs.items()):
        if ref not in fig_labels:
            problems.append(f"unresolved figure reference: {ref} referenced {count} times")

    print(f"project: {root}")
    print(f"unique citations: {len(citations)}")
    print(f"figure labels: {len(fig_labels)}")
    if problems:
        print("status: FAIL")
        for item in problems:
            print(f"- {item}")
        return 1

    print("status: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
