#!/usr/bin/env python3
"""
Reframe - Automated Cross-Platform Environment Setup
Detects OS (Windows, macOS, Linux), verifies/installs LaTeX dependencies,
initializes profile files, configures AI IDE integration, and runs a
pre-flight test compilation.
"""

import os
import sys
import shutil
import platform
import subprocess

# Ensure UTF-8 output encoding on legacy Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

# ---------------------------------------------------------------------------
# IDE RULE FILE TEMPLATES
# Each template is the content that gets written to the IDE-specific location.
# They all say the same thing: "Read these 3 files before doing anything."
# ---------------------------------------------------------------------------

CORE_RULES = """# Reframe — Mandatory Context for AI Resume Tailoring

## BEFORE ANY WORK — Read These 3 Files Completely (Every Line):
1. Read `AI_INSTRUCTIONS.md` from line 1 to line 522 (ALL sections — do NOT skim or stop early)
2. Read `base_template.tex` from line 1 to line 133 (LaTeX preamble you MUST copy verbatim)
3. Read `master_profile.json` from line 1 to line 168 (candidate's complete profile data — mastered + yet-to-master skills)

## 12 Critical Rules (Explained in AI_INSTRUCTIONS.md):
1. NO fake match scores — use honest tiers (Strong/Moderate/Stretch/Weak), NOT percentages
2. SEPARATE Basic (auto-reject) vs. Preferred (ranking) qualifications
3. REVERSE-VERIFY gap analysis — re-read the FULL JD before presenting
4. NO AI-sounding language ("Leveraging", "Cutting-edge", "Innovative solutions", "Synergies")
5. NO banned weak words ("Assisted with", "Responsible for", "Various", "Successfully")
6. NO fake metrics — defensible scope counts or verifiable improvements only
7. NO keyword stuffing — each JD keyword 1-2x max across the resume
8. NO personal pronouns (I, me, my, we, our)
9. CONTENT BUDGET TABLE — count bullets and character lengths BEFORE writing LaTeX
10. USE {\\&} inside \\resumeProjectHeading and \\resumeSubheading (\\& crashes in tabular*)
11. SELF-AUDIT before output — check budget, tone, words, pronouns, keywords, syntax
12. STRICTLY 1 PAGE for 0-5 YoE candidates. No exceptions.
"""

# Template for Cursor (.mdc format requires YAML frontmatter)
CURSOR_TEMPLATE = """---
description: Reframe AI Resume Tailoring — mandatory context and rules
globs:
alwaysApply: true
---
""" + CORE_RULES

# Template for all other IDEs (plain markdown)
PLAIN_TEMPLATE = CORE_RULES

IDE_OPTIONS = {
    "1": {
        "name": "Cursor",
        "path": os.path.join(".cursor", "rules", "resume-project.mdc"),
        "content": CURSOR_TEMPLATE,
    },
    "2": {
        "name": "GitHub Copilot (VS Code)",
        "path": os.path.join(".github", "copilot-instructions.md"),
        "content": PLAIN_TEMPLATE,
    },
    "3": {
        "name": "Windsurf",
        "path": ".windsurfrules",
        "content": PLAIN_TEMPLATE,
    },
    "4": {
        "name": "Claude Code",
        "path": "CLAUDE.md",
        "content": PLAIN_TEMPLATE,
    },
    "5": {
        "name": "Cline (VS Code Extension)",
        "path": os.path.join(".clinerules", "resume-project.md"),
        "content": PLAIN_TEMPLATE,
    },
    "6": {
        "name": "Roo Code (VS Code Extension)",
        "path": os.path.join(".roo", "rules", "resume-project.md"),
        "content": PLAIN_TEMPLATE,
    },
    "7": {
        "name": "Antigravity / Gemini",
        "path": os.path.join(".agents", "rules", "resume-project.md"),
        "content": PLAIN_TEMPLATE,
    },
    "8": {
        "name": "ChatGPT / Other (no IDE integration)",
        "path": None,
        "content": None,
    },
}


def print_header():
    print("=" * 65)
    print("  [*] Reframe -- Automated Environment Setup & Pre-Flight Check")
    print("=" * 65)


def check_command(cmd):
    return shutil.which(cmd) is not None


def setup_profile():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    master_path = os.path.join(base_dir, "master_profile.json")
    template_path = os.path.join(base_dir, "master_profile.template.json")

    if not os.path.exists(master_path):
        print("\n[1/4] Initializing your local master_profile.json...")
        if os.path.exists(template_path):
            shutil.copy(template_path, master_path)
            print("  [+] Created master_profile.json from starter template!")
        else:
            print("  [!] Template not found, skipping.")
    else:
        print("\n[1/4] Existing master_profile.json detected. Keeping your data intact.")


def setup_ide_integration():
    """Ask user which AI IDE they use and generate the appropriate rule file."""
    base_dir = os.path.dirname(os.path.abspath(__file__))

    print("\n[2/4] Which AI coding tool are you using?")
    print("  (This creates a small config file that tells the AI to read")
    print("   your project's instruction files before every task.)\n")

    for key, info in IDE_OPTIONS.items():
        print(f"  {key}. {info['name']}")

    print()
    choice = input("  Enter choice (1-8): ").strip()

    if choice not in IDE_OPTIONS:
        print("  [!] Invalid choice. Skipping IDE integration.")
        print("  [i] You can re-run setup.py anytime to configure this.")
        return

    selected = IDE_OPTIONS[choice]

    if selected["path"] is None:
        # ChatGPT / Other — no file to create
        print(f"\n  [i] Selected: {selected['name']}")
        print("  [i] No IDE integration file needed.")
        print("  [i] When using ChatGPT or other web-based AI tools:")
        print("      1. Copy the contents of AI_INSTRUCTIONS.md")
        print("      2. Paste it as Custom Instructions or System Prompt")
        print("      3. Then paste your master_profile.json as context")
        return

    file_path = os.path.join(base_dir, selected["path"])

    # Create parent directories if needed
    parent_dir = os.path.dirname(file_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    # Write the rule file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(selected["content"])

    print(f"\n  [+] Created {selected['path']} for {selected['name']}!")
    print(f"  [i] This file tells {selected['name']} to read AI_INSTRUCTIONS.md,")
    print("      base_template.tex, and master_profile.json before every task.")
    print("  [i] This file is .gitignored and won't clutter the repository.")


def verify_or_install_latex():
    print("\n[3/4] Checking LaTeX Compiler (pdflatex)...")
    if check_command("pdflatex"):
        print("  [+] pdflatex is installed and accessible in system PATH!")
        return True

    current_os = platform.system()
    print(f"  [!] pdflatex not found on {current_os}. Attempting automated installation...")

    if current_os == "Windows":
        if check_command("winget"):
            print("  [*] Running: winget install MiKTeX.MiKTeX ...")
            try:
                subprocess.run(["winget", "install", "MiKTeX.MiKTeX", "--silent", "--accept-source-agreements", "--accept-package-agreements"], check=True)
                print("  [+] MiKTeX installed successfully! Please restart your terminal/IDE.")
                return True
            except Exception as e:
                print(f"  [-] Winget installation failed: {e}")
        else:
            print("  [i] Please download and install MiKTeX manually from: https://miktex.org/download")
            return False

    elif current_os == "Darwin": # macOS
        if check_command("brew"):
            print("  [*] Running: brew install --cask basictex ...")
            try:
                subprocess.run(["brew", "install", "--cask", "basictex"], check=True)
                print("  [+] BasicTeX installed successfully! Please restart your terminal.")
                return True
            except Exception as e:
                print(f"  [-] Homebrew installation failed: {e}")
        else:
            print("  [i] Please install Homebrew or download MacTeX from: https://www.tug.org/mactex/")
            return False

    elif current_os == "Linux":
        if check_command("apt-get"):
            print("  [*] Running: sudo apt-get install -y texlive-latex-base texlive-fonts-recommended ...")
            try:
                subprocess.run(["sudo", "apt-get", "update"], check=True)
                subprocess.run(["sudo", "apt-get", "install", "-y", "texlive-latex-base", "texlive-fonts-recommended", "texlive-latex-extra"], check=True)
                print("  [+] TeX Live installed successfully!")
                return True
            except Exception as e:
                print(f"  [-] Apt installation failed: {e}")
        else:
            print("  [i] Please install texlive using your Linux package manager (pacman, dnf, zypper).")
            return False

    return False


def test_compilation():
    print("\n[4/4] Running Pre-Flight Compilation Test...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    build_script = os.path.join(base_dir, "build.py")

    if os.path.exists(build_script) and check_command("pdflatex"):
        try:
            res = subprocess.run([sys.executable, build_script], cwd=base_dir, text=True)
            if res.returncode == 0:
                print("  [+] Pre-flight test compilation SUCCEEDED! Production 1-page PDF verified.")
            else:
                print("  [!] Pre-flight build test completed with warnings/errors.")
        except Exception as e:
            print(f"  [!] Could not run build test: {e}")
    elif check_command("pdflatex"):
        print("  [+] pdflatex detected and ready.")
    else:
        print("  [i] pdflatex not yet in current shell PATH. Please restart your IDE/terminal.")


def main():
    print_header()
    setup_profile()
    setup_ide_integration()
    verify_or_install_latex()
    test_compilation()
    print("\n" + "=" * 65)
    print("  [+] Setup Complete! Open main.tex and press Ctrl+Alt+V to start.")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    main()
