# Guide: Exporting Your 95-Page B.Tech Project Report to Word (.docx) & PDF

This guide provides three simple methods to convert `B_TECH_FINAL_PROJECT_REPORT.md` into the formal, print-ready document required by your university.

---

### Option 1: Convert to Microsoft Word (.docx) using Pandoc (Recommended)

If you have Homebrew installed on your Mac:
```bash
# 1. Install pandoc
brew install pandoc

# 2. Run conversion to generate standard Microsoft Word document
pandoc B_TECH_FINAL_PROJECT_REPORT.md -o ReFynd_BTech_Project_Report.docx

# 3. Open ReFynd_BTech_Project_Report.docx in Microsoft Word or Google Docs
# Apply your department's specific cover page borders, font styles, and header/footers!
```

---

### Option 2: Export to PDF directly in VS Code (Zero CLI installation)

1. Open VS Code in this project repository.
2. In the Extensions sidebar (`Cmd + Shift + X`), search for and install:
   - **Markdown PDF** (by *yzane*) OR
   - **Markdown Preview Enhanced** (by *Yiyi Wang*)
3. Open [`B_TECH_FINAL_PROJECT_REPORT.md`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/B_TECH_FINAL_PROJECT_REPORT.md).
4. Right-click inside the document and select:
   - **`Markdown PDF: Export (pdf)`**
5. The extension compiles all tables, Mermaid diagrams, code listings, and formatted headings into a clean A4 PDF.

---

### Option 3: Import into Google Docs

1. Open [Google Docs](https://docs.google.com).
2. Go to **File -> Open -> Upload**.
3. If converted to `.docx`, drag and drop the Word file.
4. Alternatively, open [`B_TECH_FINAL_PROJECT_REPORT.md`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/B_TECH_FINAL_PROJECT_REPORT.md), select all text (`Cmd + A`), copy, and paste into a new Google Docs document.
5. In Google Docs, verify:
   - Font: Times New Roman (12 pt body, 14 pt subheadings, 16 pt bold chapter headings)
   - Line Spacing: 1.5
   - Margins: Left 1.5", Others 1"
   - Alignment: Justified
