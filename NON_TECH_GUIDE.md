# 🟢 The Absolute Beginner's Guide to Reframe (Zero-Tech Required)

> **Don't know what Git, LaTeX, or VS Code is? No problem!**  
> This guide was written specifically for non-technical job seekers (Marketing, HR, Finance, Operations, Healthcare, Students) who want a world-class ATS resume **without installing complicated developer software**.

---

## 🧭 Choose Your Path (Pick What Feels Easiest):

```
┌─────────────────────────────────────────────────────────────┬─────────────────────────────────────────────────────────┐
│               ☁️ PATH 1: ZERO-INSTALL (EASIEST)             │             🖥️ PATH 2: DOWNLOAD ZIP (LOCAL)            │
├─────────────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────┤
│ • 100% runs in your web browser (Chrome, Safari, Edge).    │ • Runs on your computer.                                │
│ • No Git, no terminal, no software downloads.              │ • No Git required (Just click "Download ZIP").          │
│ • Uses free ChatGPT/Claude + Overleaf.com.                 │ • 1-click double-click setup.                           │
│ • Works on Windows, Mac, iPad, or Chromebook!              │ • Perfect if you want to preview PDFs inside VS Code.   │
└─────────────────────────────────────────────────────────────┴─────────────────────────────────────────────────────────┘
```

---

# ☁️ PATH 1: The 100% Browser Method (Zero Software to Install)

You can tailor and download your PDF resume completely inside your web browser in **3 simple steps**:

### Step 1: Open Your AI Chat
Open [ChatGPT (chatgpt.com)](https://chatgpt.com), [Claude (claude.ai)](https://claude.ai), or [DeepSeek](https://chat.deepseek.com).

Copy and paste this message:

```text
You are an expert ATS Resume Coach. I am going to give you my current resume and a job description. 

Please analyze the job description against my background, give me a quick fit score, and then generate a 100% ATS-compliant single-page LaTeX resume.

Here is my current resume:
[PASTE YOUR RESUME TEXT HERE]

Here is the Job Description:
[PASTE THE JOB DESCRIPTION TEXT HERE]
```

---

### Step 2: Copy the Generated LaTeX Code
The AI will give you a block of code starting with `\documentclass` and ending with `\end{document}`.  
Click the **"Copy Code"** button at the top right of the code block.

---

### Step 3: Paste into Overleaf & Download PDF
1. Go to **[Overleaf.com](https://www.overleaf.com)** (it's a free online Google-Docs-like editor for LaTeX).
2. Click **"Register"** (or Log in with Google).
3. Click the green button: **"New Project" $\rightarrow$ "Blank Project"**.
4. Give it a name (e.g. `My_Tailored_Resume`).
5. Select all the default text on the screen, delete it, and **paste your copied code from the AI**.
6. Click the green **"Recompile"** button.
7. Click the **"Download PDF"** icon (next to the Recompile button).

🎉 **You're done! Your tailored, ATS-compliant PDF resume is saved to your computer.**

---

# 🖥️ PATH 2: The "Download ZIP" Method (Using VS Code Without Git)

If you want to use the automated workspace on your computer without touching terminal commands:

### Step 1: Download the Project
1. Go to the GitHub repository: **[https://github.com/Shivaprasadfarale/reframe](https://github.com/Shivaprasadfarale/reframe)**
2. Click the green **"<> Code"** button near the top right.
3. Click **"Download ZIP"**.
4. Right-click the downloaded `.zip` file on your computer and select **"Extract All..."** (Unzip it).

---

### Step 2: 1-Click Setup
* **Windows Users:** Open the unzipped folder and double-click **`setup.bat`**.
* **Mac Users:** Open the unzipped folder, double-click **`setup.sh`**.

*(The script will automatically detect and install the compiler for you in the background!)*

---

### Step 3: Open in VS Code
1. Download and open **[VS Code (code.visualstudio.com)](https://code.visualstudio.com/)** (Free).
2. In VS Code, go to **File $\rightarrow$ Open Folder...** and select your unzipped `reframe` folder.
3. Click the **Extensions icon (🧩)** on the left sidebar (or press `Ctrl + Shift + X`).
4. Search for **`LaTeX Workshop`** (by James-Yu) and click **Install**.

---

### Step 4: Live PDF Preview
1. Click on **`main.tex`** in the left file list.
2. Press **`Ctrl + Alt + V`** (Mac: `Cmd + Option + V`).
3. Your live PDF resume will open in a side-by-side tab!
4. The final PDF is automatically saved in your **`pdf_output/`** folder ready for job applications!

---

## ❓ Non-Tech FAQ

<details>
<summary><b>Q: What does "ATS" mean?</b></summary>
<b>ATS (Applicant Tracking System)</b> is the automated software (like Workday, Taleo, or Greenhouse) that companies use to screen resumes before a human recruiter reads them. If a resume has complex multi-column tables, text boxes, or graphics, ATS software often crashes or misreads your data. Reframe generates clean, single-column LaTeX code that reads with 100% accuracy on every ATS.
</details>

<details>
<summary><b>Q: Do I have to pay for Overleaf or VS Code?</b></summary>
<b>No!</b> Everything used in this project (Overleaf, VS Code, MiKTeX, and the Reframe framework) is <b>100% free and open-source</b>.
</details>

<details>
<summary><b>Q: Can I edit a word directly if I spot a typo?</b></summary>
<b>Yes!</b> You can edit the text directly inside Overleaf or VS Code just like Microsoft Word, then click Recompile to update your PDF.
</details>

---

## 📄 Need More Help?
If you get stuck or have questions, feel free to open a question on our **[GitHub Issues Page](https://github.com/Shivaprasadfarale/reframe/issues)**!
