# 🚀 Universal User Workflow Guide (For Any Candidate Background)

This guide documents the exact step-by-step experience for **any candidate from any professional background**—whether you are a **Tech Fresher**, **Senior Software Engineer**, **Non-Tech Corporate Leader (HR, Marketing, Operations, Finance)**, **Career Switcher**, or **Student with zero job experience**—who clones this repository and opens it in **VS Code**, **Cursor**, **Antigravity**, or **Trae**.

---

## 🏗️ System Architecture at a Glance

```mermaid
flowchart TD
    A["👤 Any User Clones Repo & Opens VS Code\n(Tech, Non-Tech, Fresher, Senior)"] --> B["⚡ Stage 1: Auto-Configuration\n(Run setup.bat / setup.sh -> Auto-Hide junk, PDF Auto-Routing)"]
    B --> C["📝 Stage 2: 30-Second Interactive AI Onboarding\n(User pastes plain text resume -> AI asks clarifying questions -> saves master_profile.json)"]
    C --> D["🎯 Stage 3: User Pastes ANY Job Description (JD)"]
    D --> E["🛡️ Step 3A: Automated Pre-Resume Gap Analysis\n(Fit Score, Feasibility Check, Matched vs. Missing Skills, Suggestions)"]
    E --> F["✅ User Confirms Tailoring Direction"]
    F --> G{"🔀 Step 3B: AI Selects Adaptive Polymorphic Layout"}
    G -->|"Tech Fresher (0–2 YoE)"| H1["Education-First + 3 Bullets/Project + GitHub"]
    G -->|"Senior Tech (8+ YoE)"| H2["Experience-First + P&L Scope + 2-Page Rule"]
    G -->|"Non-Tech (HR/Ops/Mktg)"| H3["Key Initiatives + Business KPIs (Omit GitHub)"]
    G -->|"Zero Projects Profile"| H4["Expanded Experience + Leadership Section"]
    G -->|"Zero Work History (Student)"| H5["Academic Projects + Hackathon Leadership"]
    H1 & H2 & H3 & H4 & H5 --> I["📄 Generates main.tex & tex_source/<role>.tex"]
    I --> J1["☁️ Overleaf Cloud (Copy-Paste in 3s)"]
    I --> J2["🖥️ Local 1-Click IDE (Saved into pdf_output/)"]
```

---

## 📦 What Any New User Sees Upon Cloning

When a new user runs:
```bash
git clone https://github.com/Shivaprasadfarale/reframe.git
cd reframe
```
and opens the folder in their editor, they see a clean, production-grade workspace:

```
reframe/
├── setup.bat / setup.sh / setup.py # ⚡ 1-Click Automated Environment Installer
├── master_profile.template.json    # 📋 Clean template profile schema (Jane Doe)
├── base_template.tex               # 📐 Universal polymorphic 1-page ATS LaTeX skeleton
├── AI_INSTRUCTIONS.md              # 🧠 Universal system directive for any AI model
├── README.md                       # 📖 Quick start documentation
├── WORKFLOW_GUIDE.md               # 🧭 This complete onboarding guide
├── RESUME_RESEARCH_REPORT.md       # 🔬 Deep-dive 10-chapter research compendium
├── tex_source/                     # 📁 Folder for tailored .tex files (for Overleaf users)
└── pdf_output/                     # 📁 Folder for generated .pdf files (for local PDF users)
```

> [!NOTE]
> **Privacy Guaranteed:** A new user will **NEVER** see your personal phone number, email, or past resumes because `.gitignore` keeps private files safely on the original author's computer.

---

## 🔄 The 4-Stage User Journey for Any Background

---

### STAGE 1: Automatic Workspace Setup (0 Seconds, Zero Config)

The user runs the 1-click installer:
* **Windows:** Double-click `setup.bat` (or run `python setup.py`).
* **Mac / Linux:** Run `./setup.sh` (or `python3 setup.py`).

**What happens automatically:**
* 🛡️ **Zero Clutter:** VS Code automatically hides all compiler junk files (`.aux`, `.log`, `.out`, `.synctex.gz`) from the sidebar.
* 🚀 **PDF Auto-Routing:** The compiler is pre-instructed to output all generated PDFs directly into `pdf_output/`.
* ⚡ **Perl Error Bypassed:** Pre-configured to use standard native `pdflatex`—requiring zero Perl installations.
* 📋 **Master Profile Created:** Copies `master_profile.template.json` to `master_profile.json` if running for the first time.

---

### STAGE 2: 30-Second Profile Onboarding (With Interactive AI Interview)

The user only ever has to configure **one file**: their `master_profile.json`.

1. The user opens their AI chat (in Cursor, ChatGPT, Claude, Antigravity, or Copilot) and sends:
   ```text
   Here is my current resume in plain text:
   [COPY-PASTE ALL TEXT FROM YOUR EXISTING RESUME]

   Read master_profile.template.json and initialize my master_profile.json!
   ```

> [!TIP]
> **💡 Pro-Tip on Input Quality: Plain Text > PDF / Image Uploads!**  
> While modern AI models can accept uploaded PDF files or screenshots of resumes, **copy-pasting plain text directly from your resume is 100% recommended**.  
> * **Why?** PDF text extractors and image OCR frequently scramble multi-column layouts, misread dates, or merge unrelated bullet points. Plain text provides the AI with clean, unambiguous data, guaranteeing 100% accurate profile initialization.

2. **The AI's Interactive Clarification Step (What Happens Automatically):**
   * The AI parses your details.
   * If any high-value optional fields are missing (e.g. GitHub link for a developer, Portfolio, Location, or Academic percentages), the AI will **ask you a quick clarification question**:
     > *"I noticed your resume didn't include a GitHub profile link, Portfolio URL, or Class 12th percentage. Would you like to provide any of these now before I finalize your `master_profile.json`?"*
   * If you provide them, it adds them. If you say *"skip"*, it cleanly leaves them empty (which our template handles dynamically without orphan `|` delimiters).
   * It formats multiple role-framing presets per job/project and saves your **`master_profile.json`**.
   * **This is a one-time setup.**

---

### STAGE 3: Tailoring for Any Job (The Daily Workflow)

Whenever the user finds a job listing on LinkedIn, Indeed, or a company career site:

1. **User sends to AI:**
   ```text
   Tailor my resume for this job description:
   [COPY-PASTE THE JOB DESCRIPTION TEXT]
   ```

2. **Step 3A — Automated Pre-Resume Gap Analysis:**
   Before generating any code, the AI performs an analytical check:
   * **Fit Score:** (e.g. *82% Match — Strong Analytical & Functional Testing Alignment*).
   * **Feasibility Check:** Warns the user if applying outside their field without prerequisites.
   * **Matched Skills:** Hard competencies they already have that match the JD.
   * **Missing Gaps:** Priority JD keywords missing from their profile.
   * **Project Bridge Suggestions:** Recommendations on how to adapt existing projects or what 1 mini-project to build.

3. **Step 3B — Polymorphic LaTeX Generation:**
   Upon user confirmation, the AI dynamically applies the appropriate **Polymorphic Adaptation Matrix** based on the user's background:

---

## 🔀 The Polymorphic Adaptation Matrix (How the System Adapts to 6 Distinct User Personas)

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             HOW THE ENGINE ADAPTS TO DIFFERENT BACKGROUNDS                                 │
├─────────────────────────────┬─────────────────────────────┬────────────────────────────────────────────────┤
│ Candidate Background        │ Structural Transformation   │ Bullet & Metric Strategy                       │
├─────────────────────────────┼─────────────────────────────┼────────────────────────────────────────────────┤
│ 1. Tech Fresher             │ • Education near top        │ • 3 detailed bullets per project               │
│    (0–2 YoE / Student)      │ • Includes Class XII/X %    │ • Google XYZ formula (dataset & record scale)  │
│                             │ • \section{Technical Proj}  │ • Anchored with 3 Achievements to fill 1 page  │
├─────────────────────────────┼─────────────────────────────┼────────────────────────────────────────────────┤
│ 2. Senior Tech Engineer     │ • Experience near top       │ • 3–4 bullets per role emphasizing throughput, │
│    (8–15+ YoE)              │ • Omit High School Class X  │   system latency, microservices, and scale     │
│                             │ • Activates 2-Page Layout   │ • Quantifies team mentorship & architecture    │
├─────────────────────────────┼─────────────────────────────┼────────────────────────────────────────────────┤
│ 3. Non-Tech Corporate       │ • Section becomes:          │ • Focuses on business KPIs: $ budget managed,  │
│    (HR, Marketing, Ops)     │   \section{Key Initiatives} │   headcount, retention %, CAC/ROAS, time saved │
│                             │ • Omit GitHub cleanly       │ • Traceable stakeholder ownership              │
├─────────────────────────────┼─────────────────────────────┼────────────────────────────────────────────────┤
│ 4. Finance, Risk & Audit    │ • \section{Technical Proj}  │ • Emphasizes Traceability (RTM), BRDs, audit   │
│    (e.g., Amex GFCC)        │   or \section{Governance}   │   trails, Excel DAX/Power Query, SQL CTEs      │
├─────────────────────────────┼─────────────────────────────┼────────────────────────────────────────────────┤
│ 5. Seasoned Professional    │ • Omit Project Section      │ • Expands Experience to 4–5 bullets per job    │
│    with ZERO Projects       │ • Add: \section{Leadership} │ • Injects strategic program deliverables       │
├─────────────────────────────┼─────────────────────────────┼────────────────────────────────────────────────┤
│ 6. Fresher with ZERO        │ • Experience becomes:       │ • 3–4 detailed technical bullets per project   │
│    Work Experience          │   \section{Academic Proj}   │ • Injects Hackathons & Open-Source Leadership  │
└─────────────────────────────┴─────────────────────────────┴────────────────────────────────────────────────┘
```

---

### STAGE 4: Generating the Final PDF (2 Fast Options)

The user chooses whichever method fits their preference:

#### Option A: Local 1-Click in IDE (VS Code / Cursor / Antigravity)
1. Open `main.tex` (or `tex_source/<role_name>.tex`).
2. Press **`Ctrl + Alt + V`** (Mac: `Cmd + Option + V`).
3. The live PDF preview opens side-by-side, and the clean PDF is automatically saved into **`pdf_output/<role_name>.pdf`**!

#### Option B: Overleaf Cloud (Zero-Install)
1. Open `tex_source/<role_name>.tex` and copy the code.
2. Paste into [Overleaf.com](https://www.overleaf.com) and click **Recompile**.
3. Download your PDF.

---

## 📈 Long-Term Career Lifecycle Management (How to Evolve Your Profile)

As your career progresses over the next 2 to 5 years, you never have to re-write your resume from scratch:

* **When you complete a new project:**  
  Tell your AI: *"I built a new project [Name] with [Stack] that [Accomplishment]. Add it to my projects bank in master_profile.json."*
* **When you get a new job / promotion:**  
  Tell your AI: *"I was promoted to [Title] at [Company]. My key accomplishments are [A, B, C]. Add this role to my experience bank in master_profile.json."*
* **When you learn a new certification / skill:**  
  Tell your AI: *"Add AWS Solutions Architect and Terraform to my master_profile.json skills bank."*

Your `master_profile.json` serves as your **permanent career vault**, growing richer with every project and accomplishment you achieve!

---

## 🧠 The 5 Golden Rules of Prompting Your AI

1. **Always provide plain text for both your resume and the JD.**
2. **Never skip the Step 1 Gap Analysis.**
3. **If a bullet seems too long or overflows to page 2, simply tell the AI:**  
   > *"Shorten the bullets in Project 1 by 1 line to ensure a strict 1-page fit."*
4. **Never let an AI invent fake companies or fake degrees.** Use real experiences and let the AI frame them accurately.
5. **Keep your local files private.** `.gitignore` protects you, so you can tailor dozens of resumes without worrying about pushing private data to GitHub.
