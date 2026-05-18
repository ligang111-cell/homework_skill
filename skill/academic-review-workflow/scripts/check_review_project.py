from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


CITE_RE = re.compile(r"\\(?:[A-Za-z]*cite[A-Za-z]*)\{([^}]*)\}")
FIG_LABEL_RE = re.compile(r"\\label\{(fig:[^}]+)\}")
FIG_REF_RE = re.compile(r"\\(?:ref|autoref|cref)\{(fig:[^}]+)\}")
BIB_KEY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MAX_CITATION_RE = re.compile(r"每篇文献最多引用\s*(\d+)\s*次")
MIN_REFERENCE_RE = re.compile(r"参考文献数量：\s*(?:约\s*)?(\d+)")


def read_all_tex(project_root: Path) -> str:
    docs = project_root / "docs"
    if not docs.exists():
        raise FileNotFoundError(f"missing docs directory: {docs}")
    return "\n".join(path.read_text(encoding="utf-8") for path in docs.rglob("*.tex"))


def parse_citations(tex: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for match in CITE_RE.finditer(tex):
        for key in match.group(1).split(","):
            key = key.strip()
            if key and "#" not in key:
                counts[key] += 1
    return counts


def parse_bib_keys(project_root: Path) -> set[str]:
    bib = project_root / "refs" / "bib" / "references.bib"
    if not bib.exists():
        return set()
    return set(BIB_KEY_RE.findall(bib.read_text(encoding="utf-8")))


def parse_index(project_root: Path, bib_keys: set[str]) -> dict[str, Path | None]:
    index = project_root / "refs" / "notes" / "paper_index.md"
    if not index.exists():
        return {}
    text = index.read_text(encoding="utf-8")
    result: dict[str, Path | None] = {}
    for line in text.splitlines():
        if not line.lstrip().startswith("|") or "---" in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        keys = [cell for cell in cells if cell in bib_keys]
        if not keys:
            continue
        link = MARKDOWN_LINK_RE.search(line)
        path = (index.parent / link.group(1).strip()).resolve() if link else None
        for key in keys:
            result[key] = path
    return result


def read_rules(project_root: Path) -> tuple[int, int | None]:
    readme = project_root / "README.md"
    if not readme.exists():
        return 2, None
    text = readme.read_text(encoding="utf-8")
    max_match = MAX_CITATION_RE.search(text)
    min_match = MIN_REFERENCE_RE.search(text)
    max_citations = int(max_match.group(1)) if max_match else 2
    min_references = int(min_match.group(1)) if min_match else None
    return max_citations, min_references


def list_downloaded_pdfs(project_root: Path) -> set[Path]:
    papers = project_root / "refs" / "papers"
    if not papers.exists():
        return set()
    return {path.resolve() for path in papers.glob("*.pdf")}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python check_review_project.py <project_root>")
        return 2

    root = Path(sys.argv[1]).resolve()
    tex = read_all_tex(root)
    citations = parse_citations(tex)
    bib_keys = parse_bib_keys(root)
    index = parse_index(root, bib_keys)
    downloaded_pdfs = list_downloaded_pdfs(root)
    max_citations, min_references = read_rules(root)
    fig_labels = Counter(FIG_LABEL_RE.findall(tex))
    fig_refs = Counter(FIG_REF_RE.findall(tex))

    problems: list[str] = []

    for key, count in sorted(citations.items()):
        if count > max_citations:
            problems.append(f"citation overuse: {key} appears {count} times")
        if key not in bib_keys:
            problems.append(f"missing bib entry: {key}")
        if key not in index:
            problems.append(f"missing paper-index entry: {key}")
        elif index[key] is not None and not index[key].exists():
            problems.append(f"missing downloaded PDF for {key}: {index[key]}")

    linked_pdfs = {path for path in index.values() if path is not None}
    for pdf in sorted(downloaded_pdfs - linked_pdfs):
        problems.append(f"downloaded PDF missing paper-index link: {pdf}")

    for key, path in sorted(index.items()):
        if path is not None and key not in citations:
            problems.append(f"downloaded paper not cited: {key}")

    if min_references is not None and len(citations) < min_references:
        problems.append(
            f"insufficient unique citations: {len(citations)} found, {min_references} required"
        )

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
    print(f"downloaded PDFs: {len(downloaded_pdfs)}")
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
