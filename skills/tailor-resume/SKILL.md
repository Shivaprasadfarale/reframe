---
name: tailor-resume
description: Generates a 100% machine-readable single-page ATS LaTeX resume with anti-AI tone guardrails, content budget enforcement, metric honesty, keyword optimization, and mandatory pre-delivery self-audit.
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
0. PRE-GENERATION: READ base_template.tex FIRST
================================================================================
Before generating any LaTeX code:
1. Read `base_template.tex` and copy the ENTIRE preamble (everything before `\begin{document}`) verbatim.
2. Use ONLY the custom commands defined there (`\resumeItem`, `\resumeSubheading`, `\resumeProjectHeading`, etc.).
3. Do NOT redefine, rename, or add new custom commands.
4. Do NOT modify margins, font, or spacing values.

================================================================================
1. POLYMORPHIC ADAPTATION & HIERARCHY RULES
================================================================================
- Fresher (0–2 YoE): Summary -> Education at top (include Class XII/X % if strong) -> Technical Projects (3 detailed bullets each) -> Experience -> Skills -> Achievements. Guarantee 95%–100% single-page canvas fill.
- Mid-Level (3–7 YoE): Summary -> Experience (3–4 bullets highlighting promotions) -> Key Projects -> Skills -> Education (omit high school).
- Senior / Lead (8–15+ YoE): Executive Summary -> Core Competencies Matrix -> Experience (P&L, budget $, team size metrics) -> Initiatives -> Education. Strictly 2 pages with >= 75% fill on page 2.
- Non-Tech Candidates (HR / Marketing / Operations / Finance): Rename section to \section{Key Initiatives} or \section{Operational Case Studies}. Focus on business KPIs ($ revenue, headcount, % conversion, time saved).
- Zero Projects Profile: Skip project section entirely; expand Experience to 4–5 bullets per role and inject \section{Leadership & Strategic Initiatives}.
- Zero Work History (Students): Rename experience to \section{Academic & Open-Source Projects} with 3–4 detailed technical bullets each.
- Consult `RESUME_RESEARCH_REPORT.md` §11 for domain-specific section titles, ATS focus entities, and target action verbs before choosing section headings.

**Education Triage Order (when content overflows):**
1. First to drop: Class X (Secondary School) — unless percentage > 95%.
2. Second to drop: Class XII — unless percentage > 95%.
3. Never drop: Primary degree (B.Tech / B.S. / etc.).
4. "Strong" threshold: Include Class XII/X only if percentage ≥ 90% (or GPA ≥ 3.7/4.0).

================================================================================
================================================================================
1B. CONTENT OVERFLOW PREVENTION ENGINE (STRICT — HARD LIMITS)
================================================================================
Before writing any LaTeX, calculate your content budget based on this table:

| Layout Scenario               | Summary        | Edu   | Projects                    | Experience                    | Skills | Achievements        |
|-------------------------------|----------------|-------|-----------------------------|-------------------------------|--------|---------------------|
| 2 proj + 2 jobs + 3 edu      | 300–350 chars  | 3     | 3 bullets each (130–170c/ea)| 3+2 bullets (130–150c/ea)     | 4 rows | 3 bullets (120–150c)|
| 2 proj + 2 jobs + 2 edu      | 300–400 chars  | 2     | 3 bullets each (140–180c/ea)| 3+2 bullets (130–160c/ea)     | 4 rows | 3 bullets (120–160c)|
| 2 proj + 1 job + 2 edu       | 320–400 chars  | 2     | 3-4 bullets each (140–180c) | 3 bullets (140–170c/ea)       | 4 rows | 3 bullets (120–160c)|
| 1 proj + 2 jobs + 2 edu      | 320–400 chars  | 2     | 4 bullets (140–180c/ea)     | 3+3 bullets (130–160c/ea)     | 4 rows | 3 bullets (120–160c)|

HARD RULES:
- If you have 2 projects with 3 education entries, use MAX 3 bullets per project at MAX 170 characters each. NEVER use 4 bullets in a 2-project + 3-education layout.
- Every bullet must be at least 120 characters (prefer 130–180 chars, 1.5–2 printed lines). No short stubs.
- Summary must be at least 300 characters (300–400 chars, 60–80 words, rendering as 3 full printed lines). A 1.5-line summary is a failure.

================================================================================
1C. DYNAMIC CANVAS-FILL & WHITESPACE COMPENSATION ENGINE
================================================================================
When a candidate has less content, DO NOT leave blank space at the bottom! Dynamically adapt:
1. **Deepen Project & Experience Bullets (Quality Over Quantity):** Prefer fewer detailed bullets (1.5–2 printed lines each, 130–180 chars) over many short 1-liners.
2. **Enrich Professional Summary:** Expand summary to 300–400 characters (60–80 words, 3 full printed lines) naming target domain, 3–4 core technical skills, and strongest measurable scope.
3. **Anchor with Achievements / Coursework:** 2–3 solid bullets (120–180 chars each).
4. **Visual Uniformity Rule:** All bullets within a section must render at roughly the same visual length (all ~1.5–2 lines). Do NOT mix 1-line and 2-line bullets.
5. **STRICT INVARIANT:** The final output must NEVER cross 1 page!

================================================================================
2. ANTI-AI TONE MANDATE (CRITICAL — RECRUITER DETECTION)
================================================================================
Modern recruiters actively flag AI-generated resumes. Output MUST sound human-written.

**Banned AI-Sounding Phrases (NEVER use):**
- "Leveraging" / "Harnessing" / "Utilizing" → just name the tool or say "using"
- "Cutting-edge" / "State-of-the-art" / "Best-in-class"
- "Innovative solutions" / "Impactful results" / "Exceptional proficiency"
- "Demonstrated expertise in" / "Proven track record of" (in bullet bodies)
- "Synergies" / "Paradigm" / "Holistic approach"
- "Passionate about" / "Dedicated to" / "Committed to"
- "Spearheaded innovative" (overused AI combo)
- "Drove meaningful impact" / "Delivered transformative results"
- "Cross-functional collaboration to deliver" (robotic filler)
- "Played a key role in" / "Was instrumental in"

**Tone Rules:**
1. Be specific, not grandiose. Say WHAT you did with WHAT tool and WHAT the result was.
2. Use plain, direct language. "Built a dashboard" > "Engineered an innovative analytical visualization platform."
3. Every adjective must be earned. Don't call something "robust" unless you explain HOW.
4. Vary sentence structure. Don't start every bullet with the identical [Verb] + [adjective] + [noun] pattern.

================================================================================
2B. BANNED WEAK WORDS & PHRASES
================================================================================
NEVER start bullets with passive or weak words:
- "Assisted with" / "Helped" → Use "Built", "Executed", "Delivered"
- "Responsible for" → State what you actually DID
- "Various" / "Multiple" / "Several" → Use real numbers: "4 teams", "8,000+ records"
- "Etc." / "And more" → List the actual items
- "Successfully" → Remove (redundant)
- "Effectively" / "Efficiently" → Replace with a metric
- "Good understanding of" / "Familiar with" → Demonstrate through a project bullet
- "Passionate about" / "Eager to" → Remove (tells, doesn't show)
- "Team player" / "Detail-oriented" / "Hard-working" → Describe the work concretely

================================================================================
3. METRIC HONESTY MANDATE
================================================================================
Every number MUST be one of:
1. **Defensible Scope Metric** — counts of real things: "8,000+ records", "200+ attendees", "4 teams", "50+ requirements"
2. **Verifiable Improvement** — only if candidate can explain HOW they measured it: "42% latency reduction (via APM before/after)"

FORBIDDEN:
- Round-number percentages with no measurement basis: "improved efficiency by 30%"
- Precise-sounding fake numbers: "43.7% accuracy improvement"
- If you cannot explain HOW a percentage was measured, use a scope metric instead.

================================================================================
4. KEYWORD OPTIMIZATION & SKILLS RELEVANCE FILTER
================================================================================
Per RESUME_RESEARCH_REPORT.md §4.3: "Repeating a keyword 10 times does NOT compound its weight. Modern matching engines register a skill entity exactly once."

1. Each key JD skill/term: 1–2 times maximum across the entire resume.
2. Primary placement: Skills section (where ATS parsers look first).
3. Secondary placement: ONE relevant project/experience bullet.
4. NEVER repeat the same keyword in 3+ separate bullets.
5. Use natural synonyms (e.g., "SQL" in skills, "queried using SQL CTEs" in a bullet).

### SKILLS RELEVANCE FILTER (No Irrelevant Skills):
Include ONLY skills mentioned in or directly implied by the JD:
1. **JD-Listed Skills:** Explicitly named in the JD (SQL, Python, Power BI).
2. **JD-Implied Skills:** Standard prerequisites (e.g. Business Analyst → Requirements Gathering, Documentation, Process Improvement, Defect Triage).
3. **Role-Standard Professional Skills:** Soft/domain skills demonstrating role awareness (Cross-Functional Collaboration, Written & Oral Communication, Data Storytelling).
4. **STRICT BAN on Irrelevant Skills:** Never include unrelated tech skills (e.g., C/C++ or React for a Business Analyst role). Avoids noise and eliminates interview risk.

### YET-TO-MASTER SKILLS PROTOCOL:
When candidate says "add this skill, I'll learn it":
1. Add skill to resume for this JD.
2. Store in `master_profile.json` under `"yet_to_master"` with date and target role.
3. On future JDs, if a skill is in `yet_to_master`, AI MUST ask if candidate has learned it before using it as a mastered skill. Never silently assume mastery.

================================================================================
5. COMPANY-SPECIFIC BULLET FRAMEWORKS
================================================================================
Do NOT apply the same formula to every company:
- **Default (Tech / SWE / Data):** Google XYZ — "Accomplished [X], measured by [Y], by doing [Z]"
- **Amazon roles:** Amazon STAR + Leadership Principles (Ownership, Bias for Action, Deep Dive, Customer Obsession). Check the JD for emphasized LPs.
- **MBB / Consulting:** McKinsey CAR — "Context → Action → Result" with $ financial impact.
- **When JD names company values/principles:** Map 2–3 bullets to those values.

Natural phrasing rules:
- NEVER literally repeat "as measured by" or "by doing" in every bullet.
- Ground numbers in defensible scope metrics.
- Start every bullet with a power action verb from the master taxonomy.

================================================================================
6. STRICT LATEX SYNTAX & CHARACTER ESCAPING MANDATE
================================================================================
To prevent fatal compilation crashes in pdflatex, ALWAYS escape reserved tokens:
- '#' -> '\#' (e.g., C\#, Issue \#42)
- '&' -> '\&' (e.g., AT\&T, SQL \& Python)
- '%' -> '\%' (e.g., 98.16\%, 30\% reduction)
- '_' -> '\_' (e.g., user\_id, api\_endpoint)
- '$' -> '\$' (e.g., \$10k budget)
- '~' -> '\textasciitilde'

⚠️ CRITICAL TABULAR TRAP:
\resumeProjectHeading and \resumeSubheading use tabular* internally.
Inside these commands, \& will CRASH because \\ is interpreted as a row break.
ALWAYS use {\&} (braced ampersand) in project names and job titles.
Use \& normally everywhere else (bullets, skills, section titles).

Context-Aware Escaping:
| Context                                              | Escape &  | Example                            |
|------------------------------------------------------|-----------|------------------------------------|
| Normal text, \resumeItem{}                           | \&        | SQL \& Python                      |
| \section{} titles                                    | \&        | \section{Achievements \& Leadership} |
| \resumeProjectHeading or \resumeSubheading titles    | {\&}      | \textbf{R{\&}D Analytics}          |

Contact header: If GitHub or Portfolio is omitted, remove the delimiter cleanly without orphan '|' characters.

================================================================================
7. DYNAMIC SKILL CATEGORY NAMING
================================================================================
Adapt the 4 skill sub-header names to match the target domain:
- SWE: Languages & Core Technical | Frameworks & Libraries | Tools & Platforms | Core Competencies
- Data/Analytics: Languages & Querying | Data Analytics & BI | Tools & Platforms | Domain & Core Competencies
- Non-Tech: Software & Technical Skills | Analytics & Reporting | Tools & Platforms | Domain Expertise

Place JD top keywords in the very first row of the skills section.

================================================================================
8. GOLDEN FORMATTING STANDARDS
================================================================================
1. Strictly 1 page (0–5 YoE). Geometry \addtolength{\textheight}{1.3in}, itemsep=1.5pt.
2. Clean plain-text contact strip. NO icon font glyphs (\faPhone, \faEnvelope). Use text separators (|) with \href.
3. 100% interview-defensible bullets using the appropriate company framework (XYZ, STAR, or CAR). Zero fake percentages.
4. Domain vocabulary accuracy per RESUME_RESEARCH_REPORT.md §11.
5. Dynamic project & experience reframing with JD action verbs and domain vocabulary.
6. Dynamic skills re-ordering with domain-appropriate category names.
7. Canonical section titles: Professional Summary, Education, Technical Projects (or domain name), Professional Experience, Technical Skills, Achievements & Leadership.
8. Zero personal pronouns: NEVER use I, me, my, we, our. ❌ "Led my team" → ✅ "Led a 4-person team."
9. Single continuous code block output from \documentclass to \end{document}.

================================================================================
9. PRE-DELIVERY SELF-AUDIT (MANDATORY BEFORE OUTPUTTING)
================================================================================
Before outputting the final LaTeX code, perform this internal self-audit:

📏 CONTENT BUDGET CHECK:
- Count total bullets and cross-reference against the Content Budget Table.
- If over budget → trim BEFORE outputting.

📝 CONTENT QUALITY CHECK:
- Re-read every bullet. Flag and fix any containing:
  * Banned AI-sounding phrases
  * Banned weak words
  * Personal pronouns (I, me, my, we, our)
  * Fake percentages without measurement basis
  * Same keyword repeated 3+ times

🔧 LATEX SYNTAX CHECK:
- Every & in project/experience heading titles uses {\&}
- Every %, #, _, $ is properly escaped
- Date format is Month YYYY -- Month YYYY

📊 STRUCTURAL CHECK:
- Section order matches career-stage hierarchy
- Skills section has JD keywords first
- Section headings match domain blueprint

Only output the LaTeX code AFTER all checks pass.

================================================================================
10. SAVING NEW FRAMING PRESETS
================================================================================
After generating the tailored resume, save the new role-specific bullet framings back into `master_profile.json` under each project/experience entry's `framing_presets` object:
- Key: `<company>_<role_slug>` (e.g., `amazon_ba_insc`)
- Value: Array of the reframed bullet strings used in the output.
