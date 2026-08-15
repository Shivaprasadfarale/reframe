# 🤝 Contributing to Reframe

Thank you for your interest in contributing to **Reframe**! We welcome contributions from developers, recruiters, resume writers, and career coaches of all skill levels.

---

## 🌟 How You Can Help

1. **Add New Role Framing Presets:**  
   Expand `master_profile.template.json` with realistic starter presets for specialized fields (e.g. Cloud DevOps, Product Management, Cybersecurity, UI/UX, BioTech, Corporate Law).
2. **Improve LaTeX Compatibility & Fonts:**  
   Help refine `base_template.tex` for obscure LaTeX distributions or edge-case compiler setups.
3. **Enhance the Setup Scripts:**  
   Improve `setup.py`, `setup.bat`, or `setup.sh` for additional Linux package managers (`pacman`, `dnf`, `zypper`, `nix`).
4. **Report Bugs & Edge Cases:**  
   Find an ATS parser issue or a LaTeX character escaping crash? Open an [Issue](https://github.com/Shivaprasadfarale/reframe/issues)!

---

## 🛠️ Development Workflow

1. **Fork the Repository:**  
   Click the **Fork** button at the top right of the GitHub page.
2. **Clone your fork locally:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/reframe.git
   cd reframe
   ```
3. **Create a new branch:**
   ```bash
   git checkout -b feat/my-cool-improvement
   ```
4. **Make your changes & test:**
   * If modifying `base_template.tex`, test compilation using `pdflatex` to ensure 0 errors and a clean 1-page fit.
   * If modifying `setup.py`, run `python setup.py` to verify.
5. **Commit & Push:**
   ```bash
   git commit -m "feat: Add Healthcare & Nursing role presets"
   git push origin feat/my-cool-improvement
   ```
6. **Open a Pull Request:**  
   Submit your PR with a clear description of the improvement!

---

## 📜 Code of Conduct

* Be respectful and inclusive to all contributors.
* Focus on constructive feedback and helping fellow job seekers succeed!
