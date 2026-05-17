# 科技论文写作

先修改本文件，再开始写作。

## 写作要求

- 主题：xx
- 字数 / 页数：xx
- 参考文献数量：xx
- 近年文献比例：xx
- 题目层级格式：`1.` / `1.1` / `1.1.1`
- “总结与展望”或“结论”部分采用总—分—总结构，中间使用“（1）（2）（3）”分点
- 数学公式要求：公式必须来自教材或论文，并保留来源
- 图片要求：先留占位，作者后续从参考论文中截图并放入 `assets/`
- 引用要求：未下载到 `refs/papers/` 的论文不得引用；每篇文献最多引用 2 次
- 禁止措辞：不要出现“从课程内容看”“课程要求表明”等课程化表述

## 交付前检查

1. 摘要与正文一致
2. 全文主题一致，无无用内容
3. 参考文献满足数量要求
4. 每篇文献最多引用 2 次
5. 每张图必须且只能被引用 1 次
6. 以审稿人视角检查：表达清晰、行文流畅、逻辑完整、层次分明

Structure:
- `docs/` report source files
- `docs/sections/` section-level TeX files
- `refs/papers/` downloaded reference PDFs
- `refs/notes/` per-paper reading notes
- `refs/bib/` BibTeX database
- `outline/` working outline and writing plan
- `assets/` figures used in the report

Build:
- Working file: `docs/main.tex`
- Recommended engine: `xelatex`
- Page margins fixed for the current course-report layout:
  - top: `2.15cm`
  - bottom: `2.15cm`
  - left: `1.95cm`
  - right: `1.95cm`
- Typical build sequence:
  - `cd docs`
  - `xelatex main.tex`
  - `biber main`
  - `xelatex main.tex`
  - `xelatex main.tex`

Notes:

