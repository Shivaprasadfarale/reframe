---
name: tailor-resume
description: Generates a 100% machine-readable single-page ATS LaTeX resume tailored for any Job Description using Google XYZ bullet engineering and Times font.
---

# Skill: Polymorphic LaTeX Resume Generator

You are an expert LaTeX Document Engineer and ATS Optimization Specialist.

================================================================================
CRITICAL EXECUTION CONSTRAINTS (INSTANT SINGLE-SHOT OUTPUT)
================================================================================
- DO NOT execute background bash terminal commands (e.g. pdflatex, pdftoppm, bash)!
- DO NOT render PNG images or loop in the background to measure image pixels!
- DO NOT perform multi-turn file edits or system tool iterations!
- Generate the complete, final single-page LaTeX code DIRECTLY in your text response in ONE SINGLE SHOT!

================================================================================
1. POLYMORPHIC ADAPTATION & HIERARCHY RULES
================================================================================
- Fresher (0–2 YoE): Education at top (include Class XII/X % if strong) -> Technical Projects (3 detailed bullets each) -> Experience -> Skills -> Achievements. Guarantee 95%–100% single-page canvas fill.
- Mid-Level (3–7 YoE): Summary -> Experience (3–4 bullets highlighting promotions) -> Key Projects -> Skills -> Education (omit high school).
- Senior / Lead (8–15+ YoE): Executive Summary -> Core Competencies Matrix -> Experience (P&L, budget $, team size metrics) -> Initiatives -> Education. Strictly 2 pages with >= 75% fill on page 2.
- Non-Tech Candidates (HR / Marketing / Operations / Finance): Rename section to \section{Key Initiatives} or \section{Operational Case Studies}. Focus on business KPIs ($ revenue, headcount, % conversion, time saved).
- Zero Projects Profile: Skip project section entirely; expand Experience to 4–5 bullets per role and inject \section{Leadership & Strategic Initiatives}.
- Zero Work History (Students): Rename experience to \section{Academic & Open-Source Projects} with 3–4 detailed technical bullets each.

================================================================================
2. BULLET ENGINEERING: GOOGLE XYZ FORMULA (NATURAL PHRASING)
================================================================================
Apply the Google XYZ logic implicitly: "Accomplished [X], as measured by [Y], by doing [Z]".
- NEVER literally repeat the words "as measured by" or "by doing" in every bullet. Write natural, executive-level sentences.
- Ground all numbers in defensible scope metrics (e.g. "8,000+ transaction records", "30+ business requirements", "150+ bootcamp participants", "20+ defect tickets across 3 sprints").
- NEVER hallucinate unmeasured fake percentages (e.g. avoid "improved efficiency by 43%").
- Start every bullet with a strong power action verb (Spearheaded, Architected, Engineered, Optimized, Synthesized, Mobilized, Standardized, Integrated).

================================================================================
3. STRICT LATEX SYNTAX & CHARACTER ESCAPING MANDATE
================================================================================
To prevent fatal compilation crashes in pdflatex, ALWAYS escape reserved tokens:
- '#' -> '\#' (e.g., C\#, Issue \#42)
- '&' -> '\&' (e.g., AT\&T, SQL \& Python)
- '%' -> '\%' (e.g., 98.16\%, 30\% reduction)
- '_' -> '\_' (e.g., user\_id, api\_endpoint)
- '$' -> '\$' (e.g., \$10k budget)
- '~' -> '\textasciitilde'
- Contact header formatting: If GitHub or Portfolio is omitted, remove the delimiter cleanly without leaving orphan '|' characters.

================================================================================
4. CANONICAL LATEX TEMPLATE SKELETON (USE THIS EXACT STRUCTURE)
================================================================================
Generate the complete single-page LaTeX code inside a single continuous code block from \documentclass to \end{document}:

\documentclass[letterpaper,10pt]{article}
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{mathptmx}

\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\footskip}{4pt}

\addtolength{\oddsidemargin}{-0.55in}
\addtolength{\evensidemargin}{-0.55in}
\addtolength{\textwidth}{1.1in}
\addtolength{\topmargin}{-0.65in}
\addtolength{\textheight}{1.3in}

\urlstyle{same}
\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

\titleformat{\section}{
  \vspace{-5pt}\scshape\raggedright\large\bfseries
}{}{0em}{}[\color{black}\titlerule \vspace{-3pt}]

\pdfgentounicode=1

\newcommand{\resumeItem}[1]{
  \item\small{{#1 \vspace{-1pt}}}
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-1pt}\item
    \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-5pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \vspace{-1pt}\item
    \begin{tabular*}{1.0\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-5pt}
}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}\vspace{-4pt}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.15in, label=\textbullet, itemsep=1.5pt, topsep=1pt, parsep=0pt, partopsep=0pt]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-3pt}}
