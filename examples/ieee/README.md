# 智能装配与检测

Topic: 动力电池包智能装配与检测
大作业要求，这是最核心的部分，你必须要牢记
选题方向：“智能装配与检测”
要求：结合某一具体产品，分析其装配工艺过程、装配过程中所采用的数字化手段与装备，结合目前机器人技术、人机协作技术、AI 技术、机器视觉、大模型、智能体、知识图谱、具身智能（至少选三种以上）等相关技术在装配过程中的应用，尝试提出一种新的装配模式，并对其基本原理、软硬件系统构成、关键技术及途径、应用前景、该装配模式的优缺点进行论述。
5000 字以上，采用期刊论文的格式，严禁大篇幅引用。

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
  - `bibtex main`
  - `xelatex main.tex`
  - `xelatex main.tex`

Notes:
- LaTeX build artifacts in `docs/` are ignored by git and should not be committed
- The current report title is `动力电池包智能装配与检测`
- Reference PDFs are stored in `refs/papers/` and currently focus on battery pack manufacturing, machine vision, human-robot collaboration, knowledge graphs, and LLM-assisted manufacturing
- Figure positions in the draft are placeholders; final figures should come from the downloaded reference papers
