#!/usr/bin/env python3
"""
Reframe — Universal Adaptive Resume Builder, Linter & Verification Engine
Deterministically builds, validates, escapes, and compiles 1-page ATS resumes
for ANY user profile, dynamically adapting to career stage, sections, and role framing presets.

Usage:
    python build.py                         # Build using default / first role
    python build.py --role amazon_ba_insc   # Build specific role preset
    python build.py --location "Noida, India" # Override location in header
    python build.py --list-roles            # List all available role presets
    python build.py --audit                 # Run linters without compiling PDF
    python build.py --test                  # Environment health-check
"""

import os
import sys
import json
import re
import math
import shutil
import argparse
import subprocess

# Configure UTF-8 stdout for Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILE_PATH = os.path.join(ROOT_DIR, "master_profile.json")
TEMPLATE_PATH = os.path.join(ROOT_DIR, "base_template.tex")
MAIN_TEX_PATH = os.path.join(ROOT_DIR, "main.tex")
MAIN_PDF_PATH = os.path.join(ROOT_DIR, "main.pdf")
TEX_DIR = os.path.join(ROOT_DIR, "tex_source")
PDF_DIR = os.path.join(ROOT_DIR, "pdf_output")

# Banned words and phrases from AI_INSTRUCTIONS.md
BANNED_AI_WORDS = [
    r"\bleveraging\b", r"\bharnessing\b", r"\butilizing\b",
    r"\bcutting-edge\b", r"\bstate-of-the-art\b", r"\bbest-in-class\b",
    r"\binnovative solutions\b", r"\bimpactful results\b", r"\bexceptional proficiency\b",
    r"\bsynergies\b", r"\bparadigm\b", r"\bholistic approach\b",
    r"\bpassionate about\b", r"\bdedicated to\b",
    r"\bspearheaded innovative\b", r"\bdrove meaningful impact\b",
    r"\bdelivered transformative\b", r"\bcross-functional collaboration to deliver\b",
    r"\bplayed a key role in\b", r"\bwas instrumental in\b"
]

BANNED_WEAK_WORDS = [
    r"\bassisted with\b", r"\bhelped\b", r"\bresponsible for\b",
    r"\bvarious\b", r"\bseveral\b", r"\betc\.\b", r"\band more\b",
    r"\bsuccessfully\b", r"\beffectively\b", r"\befficiently\b",
    r"\bgood understanding of\b", r"\bfamiliar with\b",
    r"\bteam player\b", r"\bdetail-oriented\b", r"\bhard-working\b"
]

BANNED_PRONOUNS = [
    r"\bI\b", r"\bme\b", r"\bmy\b", r"\bwe\b", r"\bour\b", r"\bmyself\b"
]

# Reframed Project Display Names per role
PROJECT_NAME_MAPPINGS = {
    "amazon_sysde_fba": {
        "financial_crimes_risk_analytics": "High-Throughput Transaction Analytics {\\&} Anomaly Engine",
        "gfcc_command_center": "Distributed Systems Health {\\&} Reliability Portal"
    },
    "amazon_ba_insc": {
        "financial_crimes_risk_analytics": "Middle-Mile Logistics {\\&} Anomaly Analytics Dashboard",
        "gfcc_command_center": "Centralized Operations {\\&} SLA Tracking Platform"
    },
    "amazon_fa_foaa": {
        "financial_crimes_risk_analytics": "Financial Ledger {\\&} Reconciliation Analytics Platform",
        "gfcc_command_center": "Financial Controls {\\&} UAT Governance Portal"
    }
}

# Role-specific tailored project tech stacks
PROJECT_STACK_MAPPINGS = {
    "amazon_sysde_fba": {
        "financial_crimes_risk_analytics": "Python, SQL, REST APIs, Relational DB",
        "gfcc_command_center": "React, TypeScript, Cloudflare D1 (SQL), REST APIs"
    }
}

# Role-specific tailored summaries
SUMMARY_MAPPINGS = {
    "amazon_sysde_fba": (
        "B.Tech. Computer Science graduate with hands-on experience in Python systems scripting, SQL database architecture, "
        "and full-stack web applications. Proven ability to build automated validation tools, diagnose software defects, "
        "engineer REST APIs, and support high-reliability systems through structured testing and CI/CD."
    ),
    "amazon_ba_insc": (
        "B.Tech. Computer Science graduate with hands-on experience in SQL data extraction, statistical anomaly modeling "
        "in Python, and automated reporting in Power BI and Excel. Proven ability to translate complex multi-source operational "
        "data into structured business insights, streamline middle-mile workflows, and influence cross-functional decisions."
    ),
    "amazon_fa_foaa": (
        "B.Tech. Computer Science graduate with hands-on expertise in SQL data modeling, advanced Excel (Power Query, DAX, "
        "VBA macros), and financial data reconciliation. Proven ability to analyze complex ledger datasets, execute structured "
        "UAT cycles, engineer variance and flux detection models, and support audit-traceable internal controls."
    )
}

# Domain Category Display Name Map
CATEGORY_NAME_MAP = {
    "languages_querying": "Languages \\& Querying",
    "data_analytics": "Languages \\& Querying",
    "data_analytics_bi": "Data Analytics \\& BI",
    "data_analytics_reporting": "Data Analytics \\& Reporting",
    "compliance_governance": "Compliance \\& Governance",
    "tools_cloud_databases": "Tools, Cloud \\& Databases",
    "tools_platforms": "Tools \\& Platforms",
    "operations_competencies": "Domain \\& Core Competencies",
    "core_competencies": "Domain \\& Core Competencies",
    "financial_core_competencies": "Domain \\& Core Competencies",
    "languages_core_technical": "Languages \\& Core Technical",
    "frameworks_libraries": "Frameworks \\& Libraries",
    "cloud_infrastructure_systems": "Cloud, Systems \\& Infrastructure",
    "systems_core_competencies": "Systems \\& Core Competencies"
}


def load_profile():
    if not os.path.exists(PROFILE_PATH):
        print(f"❌ Error: {PROFILE_PATH} not found.")
        sys.exit(1)
    with open(PROFILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def escape_latex(text, is_in_tabular=False):
    """
    Deterministically escape LaTeX special characters.
    In tabular environments (project & subheadings), & must be {\\&} to avoid row-break crashes.
    In normal body text, & must be \\&.
    """
    if not text:
        return ""
    
    # Use clean safe placeholder tokens without underscore or percent
    text = text.replace(r"{\&}", "TOKENBRACEDAMP")
    text = text.replace(r"\&", "TOKENESCAPEDAMP")
    text = text.replace(r"\%", "TOKENESCAPEDPCT")
    text = text.replace(r"\_", "TOKENESCAPEDUND")
    text = text.replace(r"\#", "TOKENESCAPEDHSH")
    text = text.replace(r"\$", "TOKENESCAPEDDLR")

    # Escape unescaped characters
    text = text.replace("%", r"\%")
    text = text.replace("_", r"\_")
    text = text.replace("#", r"\#")
    text = text.replace("$", r"\$")

    if is_in_tabular:
        text = text.replace("&", r"{\&}")
        text = text.replace("TOKENESCAPEDAMP", r"{\&}")
        text = text.replace("TOKENBRACEDAMP", r"{\&}")
    else:
        text = text.replace("&", r"\&")
        text = text.replace("TOKENESCAPEDAMP", r"\&")
        text = text.replace("TOKENBRACEDAMP", r"\&")

    text = text.replace("TOKENESCAPEDPCT", r"\%")
    text = text.replace("TOKENESCAPEDUND", r"\_")
    text = text.replace("TOKENESCAPEDHSH", r"\#")
    text = text.replace("TOKENESCAPEDDLR", r"\$")

    return text


def list_available_roles(profile):
    roles = set()
    for exp in profile.get("experience_bank", []):
        roles.update(exp.get("framing_presets", {}).keys())
    for proj in profile.get("projects_bank", []):
        roles.update(proj.get("framing_presets", {}).keys())
    for skill_role in profile.get("skills_bank", {}).get("mastered", {}).keys():
        roles.add(skill_role)
    return sorted(list(roles))


def estimate_physical_lines(text, chars_per_line=120):
    """Estimates how many physical rendered lines a text string will occupy in 10pt Times font."""
    if not text:
        return 0
    length = len(text.strip())
    if length <= 120:
        return 1
    elif length <= 240:
        return 2
    elif length <= 360:
        return 3
    else:
        return math.ceil(length / 120)


def run_audit(data_dict):
    """
    Programmatically audits text content for physical line-counts, character budgets,
    orphan wrap danger zones, banned AI words, personal pronouns, and skill integrity.
    Returns: list of (level, message) tuples where level is 'PASS', 'WARN', or 'FAIL'.
    """
    findings = []
    
    # 1. Summary Audit
    summary = data_dict.get("summary", "")
    summary_len = len(summary)
    summary_lines = estimate_physical_lines(summary)
    
    if 300 <= summary_len <= 400:
        findings.append(("PASS", f"Summary: {summary_len} chars (~{summary_lines} full lines — Optimal 300–400 chars)"))
    elif summary_len < 300:
        findings.append(("WARN", f"Summary: Only {summary_len} chars (<300 chars). May render as under 2.5 lines causing bottom whitespace."))
    else:
        findings.append(("WARN", f"Summary: {summary_len} chars (>400 chars). Risk of spilling over."))

    # Collect all bullets for line & orphan wrap analysis
    all_bullets = []
    for p in data_dict.get("projects", []):
        for idx, b in enumerate(p.get("bullets", [])):
            all_bullets.append((f"Project '{p.get('name')}' Bullet {idx+1}", b, "project"))

    for exp in data_dict.get("experiences", []):
        for idx, b in enumerate(exp.get("bullets", [])):
            all_bullets.append((f"Experience '{exp.get('company')}' Bullet {idx+1}", b, "experience"))

    for idx, item in enumerate(data_dict.get("tail_items", [])):
        all_bullets.append((f"Tail Item {idx+1}", item, "tail"))

    total_content_lines = summary_lines
    for label, text, b_type in all_bullets:
        t_len = len(text)
        p_lines = estimate_physical_lines(text)
        total_content_lines += p_lines

        if b_type in ("project", "experience"):
            # Rigorous Orphan Wrap & Solid 2-Line Depth Check:
            # Line 1 is ~120 chars. Bullets between 130-174 chars leave only 1-3 orphan words on Line 2.
            if t_len < 140:
                findings.append(("FAIL", f"{label}: Only {t_len} chars. Too short/shallow stub (Target 180–235 chars for solid 2 lines)."))
            elif 140 <= t_len <= 174:
                spill = t_len - 120
                findings.append(("FAIL", f"{label}: {t_len} chars is in the ORPHAN WRAP danger zone (140–174 chars). Line 2 has only ~{spill} chars (1–3 orphan words). Expand to 180–235 chars for solid 2 lines."))
            elif 175 <= t_len <= 235:
                spill = t_len - 120
                findings.append(("PASS", f"{label}: {t_len} chars (Solid 2 lines with ~{spill} chars on Line 2 — Zero orphan wrap)"))
            elif 236 <= t_len <= 280:
                findings.append(("WARN", f"{label}: {t_len} chars is long (~2.5 lines). Ensure it does not cause page 2 overflow."))
            else:
                findings.append(("FAIL", f"{label}: {t_len} chars (>280 chars). Exceeds 2-line budget."))
        else:
            # Tail items (Achievements / Leadership)
            if 120 <= t_len <= 170:
                findings.append(("PASS", f"{label}: {t_len} chars (~{p_lines} printed lines — Optimal)"))
            elif t_len < 120:
                findings.append(("WARN", f"{label}: Only {t_len} chars (Below 120 chars)."))
            else:
                findings.append(("WARN", f"{label}: {t_len} chars (Above 170 chars)."))

    # Banned words & pronouns check
    texts_to_scan = [("Summary", summary)] + [(l, t) for l, t, _ in all_bullets]
    for label, text in texts_to_scan:
        for pattern in BANNED_AI_WORDS:
            if re.search(pattern, text, re.IGNORECASE):
                match = re.search(pattern, text, re.IGNORECASE).group(0)
                findings.append(("FAIL", f"{label} contains banned AI phrase: '{match}'"))

        for pattern in BANNED_WEAK_WORDS:
            if re.search(pattern, text, re.IGNORECASE):
                match = re.search(pattern, text, re.IGNORECASE).group(0)
                findings.append(("FAIL", f"{label} contains banned weak word: '{match}'"))

        for pattern in BANNED_PRONOUNS:
            if re.search(pattern, text):
                match = re.search(pattern, text).group(0)
                findings.append(("FAIL", f"{label} contains personal pronoun: '{match}'"))

    # Estimate overall page canvas fill density
    edu_count = len(data_dict.get("education", []))
    section_overhead = 14 + (edu_count * 2)  # Header, section rules, skill rows, education
    estimated_total_page_lines = total_content_lines + section_overhead

    if 46 <= estimated_total_page_lines <= 53:
        findings.append(("PASS", f"Estimated Total Page Density: ~{estimated_total_page_lines} lines (Optimal 46–53 lines for 98–100% canvas fill)"))
    elif estimated_total_page_lines < 46:
        findings.append(("WARN", f"Estimated Total Page Density: ~{estimated_total_page_lines} lines (<46 lines). May leave whitespace at the bottom."))
    else:
        findings.append(("WARN", f"Estimated Total Page Density: ~{estimated_total_page_lines} lines (>53 lines). Risk of 2nd page spillover."))

    return findings


def generate_resume_tex(profile, role_slug=None, custom_location=None):
    """
    Polymorphically generates LaTeX document string adapting to any candidate profile.
    """
    available_roles = list_available_roles(profile)
    if not role_slug:
        role_slug = available_roles[0] if available_roles else "default"
    
    p_info = profile.get("personal_info", {})
    location = custom_location if custom_location else p_info.get("location", "Noida, India")
    name = p_info.get("name", "Shivaprasad Farale")
    phone = p_info.get("phone", "+91-7483195747")
    email = p_info.get("email", "shivaprasadfarale07@gmail.com")
    linkedin = p_info.get("linkedin", "")
    github = p_info.get("github", "")
    portfolio = p_info.get("portfolio", "")

    # Clean display URLs
    linkedin_display = linkedin.replace("https://www.", "").replace("https://", "").rstrip("/")
    github_display = github.replace("https://www.", "").replace("https://", "").rstrip("/")
    portfolio_display = portfolio.replace("https://www.", "").replace("https://", "").rstrip("/")

    # Header components (clean omission without orphan delimiters)
    header_parts = [
        escape_latex(location),
        escape_latex(phone),
        f"\\href{{mailto:{email}}}{{{email}}}"
    ]
    if linkedin:
        header_parts.append(f"\\href{{{linkedin}}}{{{linkedin_display}}}")
    if github:
        header_parts.append(f"\\href{{{github}}}{{{github_display}}}")
    if portfolio:
        header_parts.append(f"\\href{{{portfolio}}}{{{portfolio_display}}}")

    header_latex = " \\ \\ $|$ \\ \\ \n    ".join(header_parts)

    # Summary
    summary_text = profile.get("summary_presets", {}).get(role_slug) or SUMMARY_MAPPINGS.get(role_slug, (
        "B.Tech. Computer Science graduate with hands-on experience in SQL data extraction, statistical anomaly modeling "
        "in Python, and automated reporting in Power BI and Excel. Proven ability to translate complex multi-source operational "
        "data into structured business insights, streamline workflows, and influence cross-functional decisions."
    ))

    # Education Entries
    edu_list = profile.get("education", [])
    edu_entries = []
    for edu in edu_list:
        inst = escape_latex(edu.get("institution", ""), is_in_tabular=True)
        loc = escape_latex(edu.get("location", ""), is_in_tabular=True)
        deg = escape_latex(edu.get("degree", ""), is_in_tabular=True)
        dur = escape_latex(edu.get("duration", ""), is_in_tabular=True)
        edu_entries.append(
            f"  \\resumeSubheading\n"
            f"    {{{inst}}}{{{loc}}}\n"
            f"    {{{deg}}}{{{dur}}}"
        )
    education_latex = "\n".join(edu_entries)

    # Projects (Polymorphic: only include projects matching role_slug or top relevant)
    project_entries = []
    projects_for_audit = []
    name_map = PROJECT_NAME_MAPPINGS.get(role_slug, {})
    stack_map = PROJECT_STACK_MAPPINGS.get(role_slug, {})

    for proj in profile.get("projects_bank", []):
        presets = proj.get("framing_presets", {})
        if role_slug not in presets:
            continue

        bullets = presets[role_slug]
        p_id = proj.get("id", "")
        display_name = name_map.get(p_id, proj.get("name", ""))
        display_stack = stack_map.get(p_id, proj.get("tech_stack", ""))
        p_name = escape_latex(display_name, is_in_tabular=True)
        stack = escape_latex(display_stack, is_in_tabular=True)
        date = escape_latex(proj.get("date", ""), is_in_tabular=True)

        projects_for_audit.append({"name": display_name, "bullets": bullets})

        bullet_items = "\n".join([f"      \\resumeItem{{{escape_latex(b)}}}" for b in bullets])
        project_entries.append(
            f"  \\resumeProjectHeading\n"
            f"    {{\\textbf{{{p_name}}} $|$ \\emph{{{stack}}}}}{{{date}}}\n"
            f"    \\resumeItemListStart\n"
            f"{bullet_items}\n"
            f"    \\resumeItemListEnd"
        )
    
    projects_section_latex = ""
    if project_entries:
        projects_body = "\n\n".join(project_entries)
        projects_section_latex = f"""%---------- TECHNICAL PROJECTS ----------
\\section{{Technical Projects}}
\\resumeSubHeadingListStart
{projects_body}
\\resumeSubHeadingListEnd
"""

    # Experience (Polymorphic: include roles matching role_slug)
    exp_entries = []
    experiences_for_audit = []
    for exp in profile.get("experience_bank", []):
        presets = exp.get("framing_presets", {})
        if role_slug not in presets:
            continue

        bullets = presets[role_slug]
        role = escape_latex(exp.get("role", ""), is_in_tabular=True)
        company = escape_latex(exp.get("company", ""), is_in_tabular=True)
        duration = escape_latex(exp.get("duration", ""), is_in_tabular=True)
        loc = escape_latex(exp.get("location", ""), is_in_tabular=True)

        experiences_for_audit.append({"company": exp.get("company"), "bullets": bullets})

        bullet_items = "\n".join([f"      \\resumeItem{{{escape_latex(b)}}}" for b in bullets])
        exp_entries.append(
            f"  \\resumeSubheading\n"
            f"    {{{role}}}{{{duration}}}\n"
            f"    {{{company}}}{{{loc}}}\n"
            f"    \\resumeItemListStart\n"
            f"{bullet_items}\n"
            f"    \\resumeItemListEnd"
        )

    experience_section_latex = ""
    if exp_entries:
        exp_body = "\n\n".join(exp_entries)
        experience_section_latex = f"""%---------- PROFESSIONAL EXPERIENCE ----------
\\section{{Professional Experience}}
\\resumeSubHeadingListStart
{exp_body}
\\resumeSubHeadingListEnd
"""

    # Skills (Polymorphic category mapping with yet_to_master integration)
    mastered = profile.get("skills_bank", {}).get("mastered", {})
    role_skills = dict(mastered.get(role_slug, {}))
    if not role_skills and mastered:
        role_skills = dict(list(mastered.values())[0])

    # Merge aspirational yet_to_master skills tagged for this specific role
    yet_to_master_list = profile.get("skills_bank", {}).get("yet_to_master", [])
    for ytm in yet_to_master_list:
        if isinstance(ytm, dict):
            ytm_role = ytm.get("added_for_role")
            ytm_skill = ytm.get("skill")
            ytm_cat = ytm.get("category", "systems_core_competencies")
            if (ytm_role == role_slug or not ytm_role) and ytm_skill:
                if ytm_cat in role_skills:
                    if ytm_skill not in role_skills[ytm_cat]:
                        role_skills[ytm_cat] = f"{role_skills[ytm_cat]}, {ytm_skill}"
                else:
                    role_skills[ytm_cat] = ytm_skill

    skill_rows = []
    for cat_key, cat_val in role_skills.items():
        label = CATEGORY_NAME_MAP.get(cat_key)
        if not label:
            label = cat_key.replace("_", " ").title().replace("Bi", "BI").replace("Sql", "SQL").replace("Aws", "AWS")
            label = escape_latex(label)
        escaped_val = escape_latex(cat_val)
        skill_rows.append(f"     \\textbf{{{label}:}}{{ {escaped_val} }} \\\\ \\vspace{{1.5pt}}")

    skills_latex = "\n".join(skill_rows)
    if skills_latex.endswith(r" \\ \vspace{1.5pt}"):
        skills_latex = skills_latex[:-17]

    # Tail Section: Polymorphic (Certifications vs Achievements vs Leadership)
    tail_items = []
    tail_section_title = "Achievements \\& Leadership"

    if "certifications" in profile and profile["certifications"]:
        tail_section_title = "Certifications \\& Key Credentials"
        tail_items = profile["certifications"]
    elif "achievements" in profile and profile["achievements"]:
        tail_section_title = "Achievements \\& Leadership"
        tail_items = profile["achievements"]
    elif "leadership" in profile and profile["leadership"]:
        tail_section_title = "Leadership \\& Initiatives"
        tail_items = profile["leadership"]

    tail_entries = "\n".join([f"  \\resumeItem{{{escape_latex(a)}}}" for a in tail_items])
    tail_section_latex = ""
    if tail_items:
        tail_section_latex = f"""%---------- TAIL SECTION ({tail_section_title}) ----------
\\section{{{tail_section_title}}}
\\resumeItemListStart
{tail_entries}
\\resumeItemListEnd
"""

    # Complete LaTeX Assembly with hardened preamble
    latex_code = f"""\\documentclass[letterpaper,10pt]{{article}}

\\usepackage{{latexsym}}
\\usepackage[empty]{{fullpage}}
\\usepackage{{titlesec}}
\\usepackage{{marvosym}}
\\usepackage[usenames,dvipsnames]{{color}}
\\usepackage{{verbatim}}
\\usepackage{{enumitem}}
\\usepackage[hidelinks]{{hyperref}}
\\usepackage{{fancyhdr}}
\\usepackage[english]{{babel}}
\\usepackage{{tabularx}}
\\usepackage{{mathptmx}}
\\usepackage{{microtype}}

\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyfoot{{}}
\\renewcommand{{\\headrulewidth}}{{0pt}}
\\renewcommand{{\\footrulewidth}}{{0pt}}
\\setlength{{\\footskip}}{{4pt}}

% Margins (Calibrated for strict 1-page fit)
\\addtolength{{\\oddsidemargin}}{{-0.55in}}
\\addtolength{{\\evensidemargin}}{{-0.55in}}
\\addtolength{{\\textwidth}}{{1.1in}}
\\addtolength{{\\topmargin}}{{-0.65in}}
\\addtolength{{\\textheight}}{{1.3in}}

\\urlstyle{{same}}
\\raggedbottom
\\raggedright
\\setlength{{\\tabcolsep}}{{0in}}

% Standardized Section formatting
\\titleformat{{\\section}}{{
  \\vspace{{-2pt}}\\scshape\\raggedright\\large\\bfseries
}}{{}}{{0em}}{{}}[\\color{{black}}\\titlerule \\vspace{{-3pt}}]

\\pdfgentounicode=1

% Clean Reusable Commands
\\newcommand{{\\resumeItem}}[1]{{
  \\item\\small{{#1}}
}}

\\newcommand{{\\resumeSubheading}}[4]{{
  \\vspace{{-1pt}}\\item
    \\begin{{tabular*}}{{1.0\\textwidth}}[t]{{l@{{\\extracolsep{{\\fill}}}}r}}
      \\textbf{{#1}} & #2 \\\\
      \\textit{{\\small#3}} & \\textit{{\\small #4}} \\\\
    \\end{{tabular*}}\\vspace{{-1pt}}
}}

\\newcommand{{\\resumeProjectHeading}}[2]{{
    \\vspace{{-1pt}}\\item
    \\begin{{tabular*}}{{1.0\\textwidth}}{{l@{{\\extracolsep{{\\fill}}}}r}}
      \\small#1 & #2 \\\\
    \\end{{tabular*}}\\vspace{{-1pt}}
}}

\\newcommand{{\\resumeSubHeadingListStart}}{{\\begin{{itemize}}[leftmargin=0.0in, label={{}}, topsep=0pt, partopsep=0pt, parsep=0pt, itemsep=2pt]}}
\\newcommand{{\\resumeSubHeadingListEnd}}{{\\end{{itemize}}\\vspace{{-2pt}}}}
\\newcommand{{\\resumeItemListStart}}{{\\begin{{itemize}}[leftmargin=0.15in, label=\\textbullet, itemsep=1.5pt, topsep=1pt, parsep=0pt, partopsep=0pt]}}
\\newcommand{{\\resumeItemListEnd}}{{\\end{{itemize}}\\vspace{{-2pt}}}}

\\begin{{document}}

%---------- HEADER ----------
\\begin{{center}}
    {{\\Huge \\textbf{{{name}}}}} \\\\ \\vspace{{2pt}}
    \\small 
    {header_latex}
\\end{{center}}
\\vspace{{-12pt}}

%---------- SUMMARY ----------
\\section{{Professional Summary}}
\\resumeSubHeadingListStart
  \\item \\small {summary_text}
\\resumeSubHeadingListEnd

%---------- EDUCATION ----------
\\section{{Education}}
\\resumeSubHeadingListStart
{education_latex}
\\resumeSubHeadingListEnd

{projects_section_latex}
{experience_section_latex}
%---------- TECHNICAL SKILLS ----------
\\section{{Technical Skills}}
\\begin{{itemize}}[leftmargin=0.15in, label={{}}]
    \\small{{\\item{{
{skills_latex}
    }}}}
\\end{{itemize}}
\\vspace{{-4pt}}

{tail_section_latex}
\\end{{document}}
"""

    audit_data = {
        "summary": summary_text,
        "education": edu_list,
        "projects": projects_for_audit,
        "experiences": experiences_for_audit,
        "tail_items": tail_items
    }

    return latex_code, audit_data, role_slug


def compile_latex():
    """Runs pdflatex and returns (success, page_count, output_log)."""
    try:
        res = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "main.tex"],
            cwd=ROOT_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        output = res.stdout
        
        # Check page count
        page_match = re.search(r"Output written on main\.pdf \((\d+) page", output)
        page_count = int(page_match.group(1)) if page_match else -1
        
        success = (res.returncode == 0) and (page_count == 1)
        return success, page_count, output
    except FileNotFoundError:
        return False, -1, "pdflatex not found on PATH. Please install MiKTeX or TeX Live."
    except Exception as e:
        return False, -1, str(e)


def main():
    parser = argparse.ArgumentParser(description="Reframe Universal Adaptive Resume Builder & Auditor")
    parser.add_argument("--role", help="Role preset key to build (e.g. amazon_ba_insc)")
    parser.add_argument("--location", help="Override contact location in header")
    parser.add_argument("--audit", action="store_true", help="Run audit checks only without compiling")
    parser.add_argument("--list-roles", action="store_true", help="List available role framing presets")
    parser.add_argument("--test", action="store_true", help="Run self-test compilation")
    args = parser.parse_args()

    profile = load_profile()

    if args.list_roles:
        roles = list_available_roles(profile)
        print("\n📋 Available Role Framing Presets in master_profile.json:")
        for r in roles:
            print(f"  • {r}")
        print()
        return

    os.makedirs(TEX_DIR, exist_ok=True)
    os.makedirs(PDF_DIR, exist_ok=True)

    latex_code, audit_data, role_slug = generate_resume_tex(profile, args.role, args.location)
    findings = run_audit(audit_data)

    # Display Audit Report
    print("=" * 70)
    print(f"       🛡️  REFRAME UNIVERSAL RESUME AUDIT & BUILD REPORT (Role: {role_slug})")
    print("=" * 70)

    has_failures = False
    for level, msg in findings:
        if level == "PASS":
            print(f"  [PASS] {msg}")
        elif level == "WARN":
            print(f"  ⚠️ [WARN] {msg}")
        elif level == "FAIL":
            has_failures = True
            print(f"  ❌ [FAIL] {msg}")

    print("-" * 70)

    if args.audit:
        if has_failures:
            print("❌ Audit completed with failures.")
            sys.exit(1)
        else:
            print("✅ Audit completed successfully! All checks passed.")
            return

    # Write main.tex and archive tex
    with open(MAIN_TEX_PATH, "w", encoding="utf-8") as f:
        f.write(latex_code)

    named_tex = os.path.join(TEX_DIR, f"{role_slug}.tex")
    with open(named_tex, "w", encoding="utf-8") as f:
        f.write(latex_code)

    print("📝 Wrote main.tex and saved source to tex_source/")

    # Compile PDF
    print("⚙️  Compiling with pdflatex...")
    success, pages, log = compile_latex()

    if success:
        named_pdf = os.path.join(PDF_DIR, f"{role_slug}.pdf")
        if os.path.exists(MAIN_PDF_PATH):
            shutil.copy(MAIN_PDF_PATH, named_pdf)
        print(f"✅ Compilation Succeeded! Exactly {pages} page generated.")
        print(f"🖨️  Saved production PDF to: pdf_output/{role_slug}.pdf")
        print("=" * 70)
    else:
        if pages > 1:
            print(f"❌ FAILED: Output produced {pages} pages (Must be strictly 1 page).")
            print("   Action: Trim 1-2 bullet lengths or remove lowest-priority coursework/achievement.")
        else:
            print("❌ FAILED: Compilation error from pdflatex.")
            lines = log.split("\n")
            err_lines = [l for l in lines if l.startswith("!") or "Error" in l]
            for el in err_lines[:5]:
                print(f"   {el}")
        print("=" * 70)
        sys.exit(1)


if __name__ == "__main__":
    main()
