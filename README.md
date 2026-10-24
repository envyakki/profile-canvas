<div align="center">

# 🎨 Profile Canvas

**Automated visual contribution canvas & git scripting engine for GitHub profiles.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Git](https://img.shields.io/badge/Git-Fast--Import-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-00F5D4?style=for-the-badge)](LICENSE)

<br/>

`profile-canvas` is a lightweight, zero-dependency Python tool that calculates 7x52 calendar coordinates and programs custom pixel lettering, typography, and shapes directly onto GitHub's contribution heatmap.

</div>

---

### ✨ Features
* **Zero Dependencies:** Written in standard Python with native Git bindings.
* **Pixel Font Engine:** Built-in 7-row dot matrix typography for clean readability across 52 weeks.
* **Fast-Import Pipeline:** Generates 2,000+ precision-backdated commits in under a second using `git fast-import`.
* **Dynamic Intensity Mapping:** Adjusts commit frequency to hit exact GitHub heatmap color quartiles (Level 1 dark green to Level 4 vibrant neon).
* **Terminal Preview:** Real-time ANSI colored ASCII visualization before pushing to remote.

---

### 🚀 Quickstart

```bash
# Clone the repository
git clone https://github.com/envyakki/profile-canvas.git
cd profile-canvas

# Preview text in terminal
python canvas.py --text "AKKI" --preview
```

---

### 💻 CLI Usage

```text
usage: canvas.py [-h] [--text TEXT] [--preview] [--intensity INTENSITY]

Profile Canvas: GitHub Contribution Graph Pixel Typography Engine

options:
  -h, --help            show this help message and exit
  --text TEXT           Text to render on graph (default: AKKI)
  --preview             Display ANSI colored terminal preview
  --intensity INTENSITY Number of commits per active pixel (default: 15)
```

---

### 📂 Architecture

```text
profile-canvas/
├── canvas.py          # Main CLI engine & git pipeline
├── fonts.py           # 7x5 monospace pixel typography & shape matrices
├── requirements.txt   # Dependencies (zero-bloat)
├── LICENSE            # MIT License
└── README.md          # Documentation
```

---

### 👤 Author
Crafted by **[@envyakki](https://github.com/envyakki)**.
