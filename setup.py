#!/usr/bin/env python3
"""
Reframe - Automated Cross-Platform Environment Setup
Detects OS (Windows, macOS, Linux), verifies/installs LaTeX dependencies,
initializes profile files, and runs a pre-flight test compilation.
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
        print("\n[1/3] Initializing your local master_profile.json...")
        if os.path.exists(template_path):
            shutil.copy(template_path, master_path)
            print("  [+] Created master_profile.json from starter template!")
        else:
            print("  [!] Template not found, skipping.")
    else:
        print("\n[1/3] Existing master_profile.json detected. Keeping your data intact.")

def verify_or_install_latex():
    print("\n[2/3] Checking LaTeX Compiler (pdflatex)...")
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
    print("\n[3/3] Running Pre-Flight Compilation Test...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    main_tex = os.path.join(base_dir, "main.tex")
    pdf_out_dir = os.path.join(base_dir, "pdf_output")
    os.makedirs(pdf_out_dir, exist_ok=True)

    if not os.path.exists(main_tex):
        print("  [i] main.tex not present yet. Skipping build test.")
        return

    if check_command("pdflatex"):
        try:
            cmd = ["pdflatex", "-interaction=nonstopmode", f"-output-directory={pdf_out_dir}", main_tex]
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if res.returncode == 0:
                print("  [+] Pre-flight test compilation SUCCEEDED! main.pdf generated in pdf_output/.")
            else:
                print("  [!] Test compilation completed. Check LaTeX logs if errors occurred.")
        except Exception as e:
            print(f"  [!] Could not run build test: {e}")
    else:
        print("  [i] pdflatex not yet in current shell PATH. Please restart your IDE/terminal.")

def main():
    print_header()
    setup_profile()
    verify_or_install_latex()
    test_compilation()
    print("\n" + "=" * 65)
    print("  [+] Setup Complete! Open main.tex and press Ctrl+Alt+V to start.")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
