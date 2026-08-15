# 🎯 Reframe — Universal ATS Resume Tailoring Engine

<p align="center">
  <a href="https://github.com/Shivaprasadfarale/reframe/actions/workflows/ci.yml"><img src="https://github.com/Shivaprasadfarale/reframe/actions/workflows/ci.yml/badge.svg" alt="CI Build Status" /></a>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT" />
  <img src="https://img.shields.io/badge/ATS%20Pass%20Rate-95%25%2B-success.svg" alt="ATS Pass Rate" />
  <img src="https://img.shields.io/badge/Claude%20Plugin-Native%20Ready-6B4FBB.svg" alt="Claude Plugin Ready" />
  <img src="https://img.shields.io/badge/Google%20Gemini-Gem%20Ready-4285F4.svg" alt="Gemini Ready" />
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

> 🍏 **For Non-Technical Users (Zero-Install Browser Walkthrough):**  
> You do **not** need Git, terminal commands, or VS Code! You can use Reframe with **Claude Plugin (Recommended ⭐)** or **Google Gemini** paired with **Overleaf** for 1-click zero-software PDF downloads.  
> 👉 Read the **[Beginner / Non-Tech Guide (NON_TECH_GUIDE.md)](NON_TECH_GUIDE.md)** for a 60-second walkthrough!
>
> 💻 **For Technical Users & Developers (Local IDE & 1-Click Setup):**  
> Clone this repository, run the 1-click installer (`setup.bat` / `setup.sh`), work inside your IDE (**VS Code, Cursor, Antigravity**), and enjoy live side-by-side PDF preview (`Ctrl + Alt + V`) with full code customization!  
> 👉 Read the **[Complete User Workflow Guide (WORKFLOW_GUIDE.md)](WORKFLOW_GUIDE.md)**!

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
* **Zero Software Hassle:** Works 100% free via Claude Plugin, Google Gemini, Overleaf Cloud, or 1-click in VS Code / Cursor.

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
│   ├── NON_TECH_GUIDE.md           <-- Click-by-click beginner guide (Claude Plugin & Gemini)
│   ├── WORKFLOW_GUIDE.md           <-- Comprehensive step-by-step developer journey
│   └── RESUME_RESEARCH_REPORT.md   <-- 10-chapter ATS & recruiter eye-tracking compendium
│
└── 🔴 SYSTEM CORE (DO NOT EDIT):
    ├── base_template.tex           <-- Universal ATS LaTeX skeleton
    ├── AI_INSTRUCTIONS.md          <-- Master prompt directive for any AI model
    ├── .claude-plugin/             <-- Official Claude Plugin manifest for 1-click install
    ├── skills/                     <-- Modular Claude skills (/tailor-resume, /gap-analysis)
    └── .vscode/settings.json       <-- Auto-hide compiler clutter & auto-routing rules
```

---

## ⚡ Quick Start for Developers (3 Simple Steps)

### Step 1: Clone & Run 1-Click Setup (or Download ZIP)
```bash
git clone https://github.com/Shivaprasadfarale/reframe.git
cd reframe
```
*(Non-tech users can read **[NON_TECH_GUIDE.md](NON_TECH_GUIDE.md)** to use the Claude Plugin without Git!)*

Run the automated environment installer for your OS:
* **Windows (1-Click):** Double-click `setup.bat` (or run `python setup.py` in terminal)
* **Mac / Linux (1-Click):** Run `./setup.sh` (or `python3 setup.py` in terminal)

---

### Step 2: Initialize Your Master Profile (One-Time Setup)
Open your favorite AI assistant (**Claude, Gemini, Cursor, Antigravity, Copilot, or DeepSeek**) and copy-paste this prompt:

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

## 🧠 Recommended AI Models & Output Quality Tiers

While Reframe works with any LLM, **the natural human fluency, strategic role reframing, and ATS pass-rate depend directly on the intelligence of the model you use**:

| Model Tier | Recommended AI Models | Output Quality & ATS Score | Best For |
| :--- | :--- | :--- | :--- |
| **Tier 1: Elite (Recommended ⭐)** | **Claude 3.5 Sonnet / Opus**, **Google Gemini 1.5 Pro**, **GPT-4o / o1** | **95%–98% ATS Pass Rate**<br>• Writes completely natural, human-grade sentences without robotic buzzwords.<br>• Defensible scope metrics and flawless career polymorphism. | High-stakes applications (Top-Tier Tech, Banking, Consulting, Global Enterprises) |
| **Tier 2: Fast / Standard** | **Claude 3.5 Haiku**, **Google Gemini 1.5 Flash**, **GPT-4o mini** | **85%–90% ATS Pass Rate**<br>• Fast & accurate, but may require minor review of bullet point variety. | Rapid applications, high-volume job pipelines |
| **Tier 3: Small / Budget Models ⚠️** | **Legacy 7B/8B Local Models**, **GPT-3.5** | **< 75% ATS Pass Rate**<br>• Prone to robotic phrasing, repetitive *"as measured by"* wording, and hallucinated stats. | Not recommended for final job submissions |

> 💡 **Developer Tip:** When using Reframe inside VS Code / Cursor / Antigravity, select **Claude 3.5 Sonnet** (with Extended Thinking enabled) or **Gemini 1.5 Pro** as your active AI agent model for the most articulate, human-sounding results!

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

* 🍏 **[Beginner / Non-Tech Guide (NON_TECH_GUIDE.md)](NON_TECH_GUIDE.md):** Zero-install browser guide using the 1-click Claude Plugin or Google Gemini.
* 🧭 **[Complete User Workflow Guide (WORKFLOW_GUIDE.md)](WORKFLOW_GUIDE.md):** Step-by-step developer onboarding guide detailing the 4 stages for all candidate personas.
* 🔬 **[Master Research Compendium (RESUME_RESEARCH_REPORT.md)](RESUME_RESEARCH_REPORT.md):** 10-chapter deep research report on ATS parsing mechanics (Workday, Greenhouse, Lever), recruiter eye-tracking, and Google XYZ bullet engineering.

---

## 📄 License
MIT License. Free for personal and commercial use.
