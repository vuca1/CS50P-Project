# KANA Practice

#### Video Demo: <URL HERE>

#### Description:

**KANA Practice** is a Python-based educational tool designed to help users learn and practice Japanese Hiragana and Katakana alphabets. The program generates random sequences of KANA characters, challenges the user to write the corresponding romanized (Romaji) version, and optionally exports exercises as PDF files. This project combines multiple aspects of Python programming, providing both a functional learning tool and a showcase of programming skills learned in CS50P.  

---

### Main Features

- **Python Logic:** The project makes extensive use of functions, loops, conditionals, and exception handling to manage program flow, user input, and file operations.
- **External Libraries:**  
  - `reportlab` for generating PDF exercises with proper Japanese fonts and template backgrounds.  
  - `pyfiglet` to create ASCII-style headers for terminal interface, making it more visually appealing.
- **Regular Expressions:** Used to validate filenames for PDF export, ensuring proper input format.
- **Command-Line Arguments:** Allows users to optionally provide a filename to save exercises directly as a PDF.
- **PDF Generation:** Dynamically creates PDFs containing KANA practice exercises, with customizable columns and pages, and optional background templates.
- **Unit Testing:** Includes a separate test file (`test_project.py`) for validating core functionalities and ensuring program reliability.

---

### File Structure

project/<br>
├── export/&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Exported PDF exercises<br>
├── static/<br>
│ ├── NotoSansJP-Regular.ttf&ensp;&ensp;# Japanese font used in PDFs<br>
│ ├── template_grad.png&ensp;&ensp;&ensp;&ensp;&ensp;# PDF template with gradient title<br>
│ └── template.png&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# PDF template with regular title<br>
├── project.py&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Main Python script<br>
├── README.md&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Project documentation<br>
├── requirements.txt&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Dependencies for the project<br>
└── test_project.py&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Unit tests for project.py<br>


---

### Design Decisions

Several design choices were made to enhance usability and maintainability:  

- **PDF Layout:** Exercises are divided into pages and columns, ensuring readability even with many phrases. Each page includes answer lines at the bottom.  
- **Background Templates:** Users can choose between a regular and a gradient template to make exported PDFs more visually appealing.  
- **Error Handling:** Implemented for file operations, font loading, and user input validation, ensuring the program runs smoothly even when unexpected input occurs.  
- **Random Phrase Generation:** Generates randomized sequences of Kana characters, simulating real practice exercises while keeping the program simple and flexible.  

---

### Lessons Learned

Through this project, I strengthened my understanding and practical experience with:  

- Core Python constructs: functions, loops, conditionals, and exception handling.  
- External library usage and integration (`reportlab`, `pyfiglet`).  
- Regular expressions for input validation.  
- Command-line argument handling and basic file management.  
- Designing a practical, user-interactive program with optional PDF output.  

---

### Future Improvements

- **GUI Application:** Convert the terminal interface into a graphical user interface for improved usability.  
- **Web Application:** Expand accessibility and make exercises available online.  
- **Vocabulary Integration:** Extend the program to use real Japanese words and phrases, not just random Kana sequences.  
- **Additional Export Formats:** Add options to export exercises in CSV, TXT, or interactive formats.  

---

### Conclusion

**KANA Practice** is a versatile project that allowed me to apply many Python concepts in a practical setting while creating a useful educational tool. I am proud of the PDF generation functionality and the seamless user experience in both terminal and export modes.  

Special thanks to **CS50P** for providing the framework and motivation to complete this project, to **ReportLab** and **PyFiglet** for their libraries that made PDF generation and ASCII art possible, and to **ChatGPT** for guidance and suggestions during the project development process.
