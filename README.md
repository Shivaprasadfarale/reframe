# 🎯 Reframe — Universal ATS Resume Tailoring Engine

> **Reframe your real-world experience, projects, and skills to match any Job Description in seconds.**

`Reframe` is a portable, intelligent, AI-powered resume tailoring framework built to guarantee **100% ATS readability, dynamic career-stage polymorphism (Fresher to Senior 2-Page), strict single-page/two-page formatting, interview-defensible metrics, and instant PDF compilation** (via Overleaf or Local IDE).

---

## 📂 Clean Project Architecture

```
reframe/
│
├── master_profile.template.json  # Starter profile template for new users
├── master_profile.json           # [PRIVATE] Your single source of truth (ignored in git)
├── base_template.tex             # Universal polymorphic 1-page ATS LaTeX skeleton
├── AI_INSTRUCTIONS.md            # Universal system instructions for any AI model
├── README.md                     # Documentation & quick start guide
├── WORKFLOW_GUIDE.md             # Complete user onboarding & stage-by-stage guide
├── RESUME_RESEARCH_REPORT.md     # Deep-dive 10-chapter research compendium
├── main.tex                      # Active workspace LaTeX resume (updated on each new JD)
│
├── 📁 tex_source/                # Dedicated role-specific .tex files (saved here)
│   └── <company_role>.tex
│
└── 📁 pdf_output/                # Dedicated role-specific .pdf files (generated here)
    └── <company_role>.pdf
```

---

## 🌟 Universal Polymorphic Adaptation

This system dynamically adapts to **any candidate, any domain, and any career level**:

| Candidate Type | How the Engine Automatically Adapts |
| :--- | :--- |
| **Fresher (0–2 YoE)** | Positions Education at the top, includes academic percentages (Class XII/X), expands Projects to 3 detailed bullets, and anchors the bottom with Leadership/Achievements to guarantee a **100% full single page**. |
| **Mid-Level (3–7 YoE)** | Moves Education to the bottom, omits high school, expands work experience to 3–4 bullets, and highlights promotion trajectories. |
| **Senior / Lead (8–15+ YoE)** | Activates **2-page layout rules**, adds Executive Summary and Competencies Matrix, quantifies P&L and budget scope ($), and guarantees **$\ge 75\%$ fill on Page 2**. |
| **Tech / SWE / Data** | Formats `\section{Technical Projects}` with stack tags (`React, TypeScript, SQL`) and links GitHub/Portfolio in the header. |
| **Non-Tech (HR / Marketing / Ops)** | Dynamically renames sections to `\section{Key Initiatives}` or `\section{Operational Case Studies}` and tracks business KPIs ($ revenue, conversion %, time saved). |
| **No Projects Profile** | Expands `Professional Experience` and injects `\section{Leadership & Strategic Initiatives}` so zero blank space is left. |

---

## ⚡ Quick Start Guide (3 Simple Steps)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/reframe.git
cd reframe
```

### Step 2: Initialize Your Master Profile
You only need to configure **one file**: `master_profile.json`.

* **Option A (Super Easy — AI Automated):** Open your AI chat (ChatGPT, Claude, Cursor, Antigravity) and paste:
  > *"Here is my existing resume: [paste your resume text/PDF]. Read `master_profile.template.json` and initialize my `master_profile.json`!"*
* **Option B (Manual):** Copy `master_profile.template.json` to `master_profile.json` and fill in your details.

### Step 3: Tailor for Any Job Anytime!
Whenever you find a job on LinkedIn, Indeed, or company portals:
> *"Tailor my resume for this job description: [paste JD text]"*

The AI will:
1. 🛡️ Run a **Pre-Resume Gap Analysis** (Fit score, matched skills vs. missing gaps, project recommendations).
2. 📄 Generate your customized LaTeX code into `main.tex` and save an archive copy in **`tex_source/`** and **`pdf_output/`**!

---

## 🖨️ How to Get Your Resume (Choose Your Method)

### ☁️ Method 1: Overleaf Users (Copy LaTeX Code)
1. Open the generated file in **`tex_source/<role_name>.tex`** (or `main.tex`).
2. Copy the code and paste it into [Overleaf.com](https://www.overleaf.com).
3. Click **Recompile** and download your PDF. Zero software installation required!

---

### 🖥️ Method 2: Local PDF Users (1-Click in IDE)
1. **Prerequisites:** 
   * Install [MiKTeX](https://miktex.org/download) (Windows) or [MacTeX](https://www.tug.org/mactex/) (Mac).
   * Install the **LaTeX Workshop** extension in VS Code / Cursor.
2. Open `main.tex` in your editor.
3. Press **`Ctrl + Alt + V`** (Mac: `Cmd + Option + V`) to open the live PDF viewer tab.
4. The ready-to-submit PDF is automatically created in **`pdf_output/<role_name>.pdf`** and `pdf_output/main.pdf`.

---

## 📚 Deep Documentation & Research

* 🧭 **[User Workflow Guide (WORKFLOW_GUIDE.md)](WORKFLOW_GUIDE.md):** Complete step-by-step onboarding guide detailing the 4 stages for all candidate personas.
* 🔬 **[Master Research Compendium (RESUME_RESEARCH_REPORT.md)](RESUME_RESEARCH_REPORT.md):** 10-chapter deep research report on ATS parsing mechanics (Workday, Greenhouse, Lever), recruiter eye-tracking, and Google XYZ bullet engineering.

---

## 🛠️ Troubleshooting & Common Issues (And How to Fix Them)

### 1. `latexmk did not succeed: Perl not found` (Windows)
* **Why it happens:** By default, LaTeX Workshop tries to use `latexmk`, which requires Perl on Windows.
* **The Fix:** We have already configured [`.vscode/settings.json`](.vscode/settings.json) to use native `pdflatex` directly instead of `latexmk`.

---

### 2. Multiple MiKTeX Popups asking to "Install Package X"
* **Why it happens:** On Windows, MiKTeX defaults to *"Ask me first"* before downloading fonts/packages.
* **The Fix:**
  1. Open **MiKTeX Console** from your Windows Start Menu.
  2. Go to **Settings** in the left sidebar.
  3. Under *"You can choose whether missing packages are to be installed on-the-fly"*, select **"Always" (or "Yes")**.
  4. Click **Apply**. Now MiKTeX installs packages silently with **zero popups**.

---

### 3. Font Error: `bchb8r not found` / Missing Font Metrics
* **Why it happens:** Custom fonts like Charter require external Type-1 font metric map files that may be missing on local TeX setups.
* **The Fix:** Our template uses `\usepackage{mathptmx}` (Standard Times Roman), which is **100% built into LaTeX natively** across Windows, Mac, and Linux.

---

### 4. Special Character Crashes (`#`, `&`, `%`, `_`, `$`)
* **Why it happens:** In LaTeX, these are reserved tokens.
* **The Fix:** Our system automatically escapes them (`\#`, `\&`, `\%`, `\_`, `\$`, `\textasciitilde`), preventing compiler crashes.

---

## 🔒 Privacy & Open Source Safety

* **Your personal data is protected:** `.gitignore` is pre-configured to ignore `master_profile.json`, `main.tex`, `tex_source/`, and `pdf_output/`.
* When you push to GitHub, only the clean `master_profile.template.json` and universal `base_template.tex` are published—your real phone number, email, and personal resume archives **stay private on your machine**.

---

## 📄 License
MIT License. Free for personal and commercial use.
