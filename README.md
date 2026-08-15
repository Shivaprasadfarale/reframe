# 🎯 Reframe — Universal ATS Resume Tailoring Engine

<p align="center">
  <a href="https://github.com/Shivaprasadfarale/reframe/actions/workflows/ci.yml"><img src="https://github.com/Shivaprasadfarale/reframe/actions/workflows/ci.yml/badge.svg" alt="CI Build Status" /></a>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT" />
  <img src="https://img.shields.io/badge/ATS%20Pass%20Rate-90%25%2B-success.svg" alt="ATS Pass Rate" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg" alt="Platform" />
  <img src="https://img.shields.io/badge/LaTeX-Overleaf%20%7C%20Local-orange.svg" alt="LaTeX" />
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome" />
</p>

<p align="center">
  <b>Reframe your real-world experience, projects, and skills to match any Job Description in seconds.</b><br>
  <i>100% ATS-Compliant • Millimeter-Perfect 1-Page LaTeX Geometry • Zero Fake Metrics • 1-Click PDF Generation</i>
</p>

<p align="center">
  ⭐ <b>If you find Reframe helpful, please star this repository! It helps more job seekers discover the tool.</b> ⭐
</p>

---

> 🍏 **Non-Technical or First Time using GitHub/LaTeX?**  
> Read the **[Beginner / Non-Tech Guide (NON_TECH_GUIDE.md)](NON_TECH_GUIDE.md)** for a 100% browser-based, zero-installation walkthrough using Overleaf & ChatGPT!  
>  
> 🧭 **Want to understand the complete career workflow?**  
> Read the **[Complete User Workflow Guide (WORKFLOW_GUIDE.md)](WORKFLOW_GUIDE.md)** to see how the engine adapts for all candidate personas!

---

## 💡 What is Reframe & Why Do You Need It?

### 📉 The Problem:
* **75%+ of resumes are filtered out by ATS (Applicant Tracking Systems)** like Workday, Greenhouse, and Lever before a human recruiter ever sees them because of multi-column tables, icon glyphs, or missing JD keywords.
* **Sending one generic resume to 50 jobs gets a 2% callback rate.**
* **Manually rewriting your resume for every single job takes hours**, and online AI resume builders hallucinate fake metrics that will get you caught in interviews.

### 🚀 The Reframe Solution:
`Reframe` is a portable, intelligent, AI-powered framework that uses a **single private data vault (`master_profile.json`)** to dynamically re-frame your real-world experience to match any job description.
* **Automated Gap Analysis:** Calculates your exact fit score and missing skills *before* writing code.
* **Google XYZ Formula:** Re-frames bullets using industry action verbs and defensible scope metrics (e.g. *8,000+ records*, *30+ requirements*, *20+ defects*).
* **Zero Software Hassle:** Works 100% free via Overleaf Cloud or with 1-click in VS Code / Cursor.

---

## ✨ Key Features

* 🛡️ **100% Machine-Readable ATS Geometry:** Standard single-column layout, plain-text contact headers (zero FontAwesome glyph corruption), and canonical section titles.
* 🔀 **Career-Stage Polymorphism:**
  * **Freshers (0–2 YoE):** Education first, Class XII/X %, 3 bullets per project, 100% canvas fill.
  * **Mid-Level (3–7 YoE):** Experience first, high school omitted, promotion trajectories highlighted.
  * **Seniors (8–15+ YoE):** 2-page rules activated, P&L/budget metrics, $\ge 75\%$ fill on Page 2.
  * **Non-Tech Roles:** Dynamically shifts headings to `Key Initiatives` or `Case Studies` and tracks business KPIs ($ revenue, conversion %, time saved).
  * **Zero-Project Profiles:** Gracefully skips projects and expands work experience with zero awkward whitespace.
* ⚡ **1-Click Cross-Platform Setup:** Automated scripts (`setup.bat` on Windows, `setup.sh` on Mac/Linux) install the LaTeX compiler and verify your environment with 0 manual configuration.
* 🔒 **100% Privacy Lock:** Your real phone number, email, and personal resumes are protected by `.gitignore` and **never uploaded to GitHub**.

---

## 🚦 File Traffic Light: What to Touch vs. What to Leave Alone

```
reframe/
├── 🟢 FILES YOU WORK WITH:
│   ├── master_profile.json         <-- Your single source of truth (private to you)
│   ├── main.tex                    <-- Your active resume (view with Ctrl+Alt+V)
│   ├── 📁 pdf_output/              <-- Ready-to-submit PDF resumes are saved here
│   └── 📁 tex_source/              <-- Role-specific .tex files (for Overleaf users)
│
├── 🟡 AUTOMATION & ONBOARDING:
│   ├── setup.bat / setup.sh        <-- 1-Click environment setup script for your OS
│   ├── master_profile.template.json<-- Starter schema template (Jane Doe)
│   ├── NON_TECH_GUIDE.md           <-- Click-by-click beginner guide (No software needed)
│   ├── WORKFLOW_GUIDE.md           <-- Comprehensive step-by-step user journey
│   └── RESUME_RESEARCH_REPORT.md   <-- 10-chapter ATS & recruiter eye-tracking compendium
│
└── 🔴 SYSTEM CORE (DO NOT EDIT):
    ├── base_template.tex           <-- Universal ATS LaTeX skeleton
    ├── AI_INSTRUCTIONS.md          <-- Master prompt directive for any AI model
    └── .vscode/settings.json       <-- Auto-hide compiler clutter & auto-routing rules
```

---

## ⚡ 60-Second Quick Start (3 Simple Steps)

### Step 1: Clone & Run 1-Click Setup (or Download ZIP)
```bash
git clone https://github.com/Shivaprasadfarale/reframe.git
cd reframe
```
*(Non-tech users can click the green **Code $\rightarrow$ Download ZIP** button instead of Git!)*

Run the automated environment installer for your OS:
* **Windows (1-Click):** Double-click `setup.bat` (or run `python setup.py` in terminal)
* **Mac / Linux (1-Click):** Run `./setup.sh` (or `python3 setup.py` in terminal)

---

### Step 2: Initialize Your Master Profile (One-Time Setup)
Open your favorite AI assistant (**Cursor, ChatGPT, Claude, Antigravity, Copilot, or DeepSeek**) and copy-paste this prompt:

```text
Here is my current resume in plain text:
----------------------------------------
[PASTE ALL TEXT FROM YOUR EXISTING RESUME HERE]
----------------------------------------

Please read master_profile.template.json and initialize my private master_profile.json with all my details, experiences, projects, and skills!
```

> [!TIP]
> **💡 Pro-Tip: Always Paste Plain Text over PDF / Image Uploads!**  
> While modern AIs accept PDFs and screenshots, **copy-pasting plain text directly from your resume is 100% recommended**. PDF parsers and OCR frequently scramble multi-column layouts, misread dates, or corrupt bullet formatting. Plain text guarantees 100% flawless extraction by the AI.

---

### Step 3: Tailor for Any Job Anytime!
Whenever you find a job on LinkedIn, Indeed, or a company career page, paste this to your AI:

```text
Tailor my resume for this job description:
------------------------------------------
[PASTE THE JOB DESCRIPTION TEXT HERE]
------------------------------------------
```

**What the AI does automatically:**
1. 🛡️ **Step 1 — Pre-Resume Gap Analysis:** Calculates your fit score, shows matched skills vs. missing gaps, and recommends project bridges.
2. 📄 **Step 2 — Polymorphic LaTeX Generation:** Upon your confirmation, writes the tailored resume to `main.tex` and saves an archive copy in `tex_source/<role>.tex` and `pdf_output/<role>.pdf`!

---

## 🖨️ How to Generate Your PDF (Choose Your Method)

### ☁️ Method 1: Overleaf Cloud (Zero-Install)
1. Open the generated file in **`tex_source/<role_name>.tex`** (or `main.tex`).
2. Copy the code and paste it into [Overleaf.com](https://www.overleaf.com).
3. Click **Recompile** and download your PDF. Zero software installation required!

---

### 🖥️ Method 2: Local 1-Click in IDE (VS Code / Cursor / Antigravity)
1. Open `main.tex` in your editor.
2. Press **`Ctrl + Alt + V`** (Mac: `Cmd + Option + V`) to open the live PDF viewer tab.
3. The ready-to-submit PDF is automatically created in **`pdf_output/<role_name>.pdf`** and `pdf_output/main.pdf`.

---

## ⚠️ 4 Common Mistakes to Avoid

1. ❌ **Uploading Images/Scans:** Always copy-paste **plain text** from your resume and job description to prevent OCR text scrambling.
2. ❌ **Manually Editing the LaTeX Layout:** Do not edit the formatting commands in `base_template.tex`—they are engineered to strict millimeter-level ATS margins. If you need a wording tweak, ask your AI: *"Make bullet 2 in Project 1 shorter"*.
3. ❌ **Putting Unmeasured Percentages:** Never let an AI write generic fluff like *"improved performance by 50%"*. Ground metrics in defensible scope (*"analyzed 8,000+ records"*, *"captured 30+ requirements"*, *"resolved 20+ defects"*).
4. ❌ **Skipping the Pre-Resume Gap Analysis:** Always read the AI's Step 1 report before generating LaTeX. If a high-priority skill is missing, you can mention an existing project to bridge the gap!

---

## 💬 Community, Suggestions & Bug Reports

Have a question, encountered an issue, or want to suggest a new resume template or feature?

* 🐛 **Report a Bug / Ask a Question:** Open an issue on the **[GitHub Issues Tab](https://github.com/Shivaprasadfarale/reframe/issues)**.
* 💡 **Feature Requests & Suggestions:** If you have ideas to make Reframe even better, feel free to open an issue with the tag `enhancement`!
* 🔀 **Contributing:** Pull requests are always welcome! Feel free to submit templates or installer improvements.

---

## ❓ Frequently Asked Questions (FAQ)

<details>
<summary><b>1. Will my personal information ever be leaked to GitHub?</b></summary>
<b>NO.</b> <code>.gitignore</code> is pre-configured to permanently block <code>master_profile.json</code>, <code>main.tex</code>, <code>tex_source/</code>, and <code>pdf_output/</code>. When you push to GitHub, only the clean templates are uploaded.
</details>

<details>
<summary><b>2. Can I use this for non-tech roles (Marketing, HR, Finance, Operations)?</b></summary>
<b>YES.</b> The AI dynamically renames <code>Technical Projects</code> to <code>Key Initiatives</code> or <code>Strategic Case Studies</code> and shifts the focus to business KPIs ($ revenue, conversion %, retention, time saved).
</details>

<details>
<summary><b>3. Do I need to install LaTeX if I only use Overleaf?</b></summary>
<b>NO.</b> If you use Overleaf, you don't need MiKTeX or any local software. Just copy the generated code from <code>tex_source/<role>.tex</code> and paste it into Overleaf.com!
</details>

<details>
<summary><b>4. How do I update my profile when I get a new job or build a new project?</b></summary>
Simply open your AI chat and say: <i>"I just built a new project called [Name] using [Stack] that does [Description]. Add it to my master_profile.json!"</i> The AI will automatically format it with multiple framing presets.
</details>

---

## 📚 Deep Documentation & Research

* 🍏 **[Beginner / Non-Tech Guide (NON_TECH_GUIDE.md)](NON_TECH_GUIDE.md):** 100% browser-based, zero-installation guide using Overleaf.
* 🧭 **[Complete User Workflow Guide (WORKFLOW_GUIDE.md)](WORKFLOW_GUIDE.md):** Step-by-step onboarding guide detailing the 4 stages for all candidate personas.
* 🔬 **[Master Research Compendium (RESUME_RESEARCH_REPORT.md)](RESUME_RESEARCH_REPORT.md):** 10-chapter deep research report on ATS parsing mechanics (Workday, Greenhouse, Lever), recruiter eye-tracking, and Google XYZ bullet engineering.

---

## 📄 License
MIT License. Free for personal and commercial use.
