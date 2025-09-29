# KANA Practice

#### Video Demo:  [LINK](https://youtu.be/wTlnjrO-ikk?si=DBun59V6WuJLm4UQ) (https://youtu.be/wTlnjrO-ikk?si=DBun59V6WuJLm4UQ) # TODO

#### Description:

**KANA Practice** is a Python-based educational tool designed to help users learn and practice Japanese **Hiragana** and **Katakana** alphabets.  
The program generates random sequences of KANA characters, challenges the user to write the corresponding romanized (**Romaji**) version, and optionally exports exercises as **PDF files**.  

This project demonstrates concepts learned in **CS50P**, including:  
- Functions, loops, conditionals, and exception handling  
- File handling and command-line arguments  
- Use of external libraries  
- Regular expressions for validation  
- Unit testing with `pytest`  

The program can be used in both the **terminal** and a simple **GUI (Tkinter)** interface.  

---

## Main Features

- **Terminal Interface** – Practice KANA directly in the terminal with Romaji input prompts.  
- **Graphical Interface (GUI)** – Tkinter-based GUI with buttons, entry fields, and feedback.  
- **Randomized Exercises** – Generate custom sets of phrases for practice.  
- **PDF Export** – Save exercises to PDF with proper Japanese fonts and optional background templates.  
- **Filename Validation** – Regex-based validation ensures safe and correct file names.  
- **Unit Testing** – `test_project.py` includes tests for phrase checking, KANA generation, Romaji conversion, and more.  
- **ASCII Headers** – Styled headers in terminal mode using `pyfiglet`.  

---

## File Structure

project/<br>
├── export/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Exported PDF exercises<br>
├── static/<br>
│ ├── NotoSansJP-Regular.ttf&nbsp;&nbsp;&nbsp;&nbsp;# Japanese font for PDFs<br>
│ ├── template_grad.png&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# PDF template (gradient header)<br>
│ └── template.png&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# PDF template (standard header)<br>
├── project.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Main Python script<br>
├── gui.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Optional GUI script (Tkinter)<br>
├── test_project.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Unit tests with pytest<br>
├── requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Project dependencies<br>
└── README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Documentation<br>

---

## Instructions
- **Terminal Version:** Run `python project.py` from the project folder. Follow the on-screen instructions to practice KANA in the terminal.
- **GUI Version:** Run `python gui.py` from the project folder. A KANA Practice window will appear, allowing you to practice via a graphical interface.

---

## Design Decisions

- **PDF Layout** – Exercises are split into pages/columns with answer lines at the bottom.  
- **Template Options** – Users can choose between gradient or standard title templates.  
- **Error Handling** – Covers file operations, font loading, and invalid inputs.  
- **Flexible Practice** – Kana phrases are randomized for better learning variety.  

---

## Lessons Learned

This project strengthened my skills in:  
- Python fundamentals (functions, loops, conditionals, exceptions)  
- External libraries (`reportlab`, `pyfiglet`, `tkinter`)  
- Regex input validation  
- Command-line argument handling  
- Unit testing with `pytest`  
- Designing a practical user-interactive application  

---

## Future Improvements

- **Extended GUI** – Add more user controls and statistics tracking.  
- **Web Version** – Make exercises available online for wider access.  
- **Vocabulary Mode** – Practice real Japanese words instead of random kana.  
- **More Export Formats** – Add CSV, TXT, or interactive formats.  

---

## Conclusion

**KANA Practice** combines programming concepts from CS50P into a practical, educational tool for learning Japanese kana.  
It highlights PDF generation, GUI development, and program design, while being both useful and fun to use.  

Special thanks to **CS50P**, **ReportLab**, **PyFiglet**, and **ChatGPT** for guidance and resources during development.  
