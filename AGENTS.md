# Reframe — AI Resume Tailoring System (Universal Agent Rules)

> **This file is auto-loaded by AI coding tools (Gemini, Claude Code, Cursor, Copilot, Windsurf, Cline, Roo Code).**  
> It ensures every AI model reads the mandatory project files before doing any work.

---

## ⚠️ MANDATORY: READ THESE 3 FILES COMPLETELY BEFORE ANY WORK

You are working on **Reframe**, an AI-powered resume tailoring system. Before responding to ANY user request (gap analysis, resume generation, profile editing, or any task), you MUST read these 3 files **in full, line by line, skipping nothing**:

### File 1: `AI_INSTRUCTIONS.md` (Lines 1–522)
**Read the ENTIRE file from line 1 to line 522.** This contains:
- Lines 1–27: Critical Rules Summary (12 non-negotiable rules)
- Lines 28–55: Project Architecture and Template Usage
- Lines 56–75: Onboarding Protocol
- Lines 76–170: Gap Analysis with Basic vs. Preferred qualification split, reverse-verification, project selection strategy, and hard truth assessment
- Lines 171–215: Resume Generation with pre-delivery self-audit, compile-verify, and preset saving
- Lines 216–250: Anti-AI Tone Mandate and Banned Weak Words
- Lines 251–280: Metric Honesty Mandate and Keyword Optimization Rules
- Lines 281–340: Skills Relevance Filter, Polymorphism rules, Content Budget Table, Canvas-Fill Engine
- Lines 341–522: LaTeX escaping (CRITICAL tabular trap), Power Verbs, Company-Specific Frameworks, Golden Standards, Post-Generation Quality Checklist
**DO NOT skip any section. Rules about tone, honesty, content limits, skills filtering, and LaTeX safety are distributed throughout.**

### File 2: `base_template.tex` (Lines 1–133)
**Read the ENTIRE file from line 1 to line 133.** This is the LaTeX preamble and command definitions you MUST copy verbatim. Pay special attention to:
- Lines 58–61: CRITICAL warning about `{\&}` vs `\&` inside tabular commands
- Lines 62–67: `\resumeProjectHeading` definition (uses `tabular*` — `\&` will crash here)
- Lines 50–56: `\resumeSubheading` definition
**You MUST copy this preamble verbatim into `main.tex`. Do NOT modify margins, fonts, spacing, or command definitions.**

### File 3: `master_profile.json` (Lines 1–168)
**Read the ENTIRE file from line 1 to line 168.** This is the candidate's complete profile — education, experience bank, projects bank, skills bank (mastered + yet-to-master), achievements, and framing presets. You need ALL of this to:
- Match skills against JD requirements
- Select which projects/experiences to include
- Find existing framing presets for the target role

---

## CRITICAL RULES QUICK REFERENCE (from AI_INSTRUCTIONS.md)

These 12 rules are explained in detail in `AI_INSTRUCTIONS.md`. Violating any is a failure:

1. **NO FAKE MATCH SCORES** — Use honest tiers (Strong/Moderate/Stretch/Weak) with hard cap rules, NOT percentages
2. **SEPARATE BASIC vs. PREFERRED QUALIFICATIONS** — Basic = auto-reject if failed. Preferred = ranking
3. **REVERSE-VERIFY GAP ANALYSIS** — Re-read the FULL JD line-by-line before presenting
4. **NO AI-SOUNDING LANGUAGE** — Never: "Leveraging", "Cutting-edge", "Innovative solutions", "Synergies"
5. **NO BANNED WEAK WORDS** — Never: "Assisted with", "Responsible for", "Various", "Successfully"
6. **NO FAKE METRICS** — Defensible scope counts ("8,000+ records") or verifiable improvements only
7. **NO KEYWORD STUFFING** — Each JD keyword 1-2x max across the resume
8. **NO PERSONAL PRONOUNS** — Never use I, me, my, we, our
9. **CONTENT BUDGET TABLE** — Count bullets and character lengths BEFORE writing LaTeX
10. **USE `{\&}` INSIDE HEADINGS** — `\&` crashes inside `\resumeProjectHeading` / `\resumeSubheading`
11. **SELF-AUDIT BEFORE OUTPUT** — Check budget, tone, words, pronouns, keywords, syntax
12. **STRICTLY 1 PAGE** — For 0-5 YoE candidates. No exceptions.

---

## WORKFLOW

```
User provides JD
  → Read AI_INSTRUCTIONS.md (lines 1-522)
  → Read base_template.tex (lines 1-133)  
  → Read master_profile.json (lines 1-168)
  → STEP 1: Gap Analysis (with reverse-verification)
  → User approves
  → STEP 2a: Pre-Delivery Self-Audit
  → STEP 2b: Generate & Write main.tex
  → STEP 2c: Compile & Verify 1 page
```
