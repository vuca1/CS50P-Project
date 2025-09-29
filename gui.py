import tkinter as tk

from tkinter import messagebox
from project import KANA_MAP, generate_kana, kana_to_romaji, save_pdf, check_filename


# create window
root = tk.Tk()
root.title(" KANA Practice")
root.geometry("400x300")
root.resizable(False, False)
root.iconbitmap("static/icon.ico")


def clear_window():
    for widget in root.winfo_children():
        widget.destroy() # removes all widgets from window


def settings_window():
    clear_window()

    # frame for alphabet choosing
    frame_alphabet = tk.Frame(root)
    frame_alphabet.pack(padx=5, pady=5)

    # default radio button selection (alphabets)
    alphabet_var = tk.StringVar(value="HIRAGANA")

    tk.Label(frame_alphabet, text="Choose alphabet:", font=("Times-Roman", 12)).grid(row=0, column=0, columnspan=2, pady=5)
    button_hiragana = tk.Radiobutton(frame_alphabet, text="Hiragana",variable=alphabet_var, value="HIRAGANA")
    button_hiragana.grid(row=1, column=0, padx=10, pady=3)
    button_katakana = tk.Radiobutton(frame_alphabet, text="Katakana", variable=alphabet_var, value="KATAKANA")
    button_katakana.grid(row=1, column=1, padx=10, pady=3)

    # frame for configuration
    frame_configure = tk.Frame(root)
    frame_configure.pack(padx=5, pady=5)

    # phrases count
    tk.Label(frame_configure, text="How many phrases:").grid(row=0, column=0, padx=5, pady=5)
    entry_phrases = tk.Entry(frame_configure)
    entry_phrases.grid(row=0, column=1, padx=5, pady=2)
    entry_phrases.focus()

    # characters count
    tk.Label(frame_configure, text="How many characters per phrase:").grid(row=1, column=0, padx=5, pady=5)
    entry_characters = tk.Entry(frame_configure)
    entry_characters.grid(row=1, column=1, padx=5, pady=5)

    # filename for pdf file
    tk.Label(frame_configure, text="Filename for PDF export:").grid(row=2, column=0, padx=5, pady=5)
    entry_filename = tk.Entry(frame_configure)
    entry_filename.grid(row=2, column=1, padx=5, pady=5)

    # frame practice / generate PDF
    frame_option = tk.Frame(root)
    frame_option.pack(padx=5, pady=5)


    def initiate_engine(mode):
        MAX_PHRASES = 60
        MAX_CHARACTERS = 5

        # check valid numbers
        try:
            num_phrases = int(entry_phrases.get())
            num_characters = int(entry_characters.get())
            if num_phrases > MAX_PHRASES or num_phrases < 1:
                raise ValueError
            if num_characters > MAX_CHARACTERS or num_characters < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Positive numbers only! Max phrases: 60 | Max characters: 5")
            return
        
        # when valid:
        kana_dict = KANA_MAP[alphabet_var.get().upper()]

        if mode == 1:
            practice_window(generate_kana(num_characters, kana_dict, num_phrases), kana_dict)
        elif mode == 2:
            # check for correct filename format
            filename = check_filename(entry_filename.get(), "pdf")
            if not filename[0]:
                messagebox.showerror("Invlaid filename", "Invalid filename. Valid format '<filename[a-z . _ -]>.pdf'")
                return
            save_pdf(filename[1], generate_kana(num_characters, kana_dict, num_phrases), kana_dict, num_phrases)
            # TODO: filepath is hardcoded
            messagebox.showinfo("Saved", f"Succesfully generated {filename[1]} file and saved to export/")
        else:
            messagebox.showerror("Error", "Invalid input")
            main_menu


    # practice/pdf button
    button_practice = tk.Button(frame_option, text="Start Practice", command=lambda: initiate_engine(1))
    button_practice.grid(row=0, column=0, padx=5, pady=5)
    button_pdf = tk.Button(frame_option, text="Generate PDF", command=lambda: initiate_engine(2))
    button_pdf.grid(row=0, column=1, padx=5, pady=5)

    # back to menu button
    button_back = tk.Button(root, text="Back", command=main_menu)
    button_back.pack(pady=10)


def practice_window(kana_list, kana_dict, score=0, total=None):
    if total is None:
        total = len(kana_list)

    # exit to menu when answered all
    if len(kana_list) == 0:
        main_menu(f"Congratulations! 🎉 Your score is {score}/{total} 👏")
        return

    clear_window()

    tk.Label(root, text="Convert KANA to Romaji", font=("Times-Roman", 14)).pack(pady=15)

    # frame for convertion
    frame_kana = tk.Frame(root)
    frame_kana.pack(pady=5)

    current_kana = kana_list[0]

    label_kana = tk.Label(frame_kana, text=current_kana, font=("Arial", 18))
    label_kana.grid(row=0, column=0, padx=5, pady=5)
    tk.Label(frame_kana, text=" : ").grid(row=0, column=1, padx=5, pady=5)
    entry_answer = tk.Entry(frame_kana)
    entry_answer.grid(row=0, column=2, padx=5, pady=5)
    entry_answer.focus()

    # label for correct/wrong message
    label_result = tk.Label(root, text="", font=("Arial", 12))
    label_result.pack(pady=10)

    def check_and_next():
        user_input = entry_answer.get().strip().lower()
        correct_answer = kana_to_romaji(current_kana, kana_dict)

        if user_input == correct_answer:
            label_result.config(text="✅ Correct!", fg="green")
            new_score = score + 1
        else:
            label_result.config(text=f"❌ Incorrect | {current_kana} - {correct_answer}", fg="red")
            new_score = score

        # show result and move to next kana phrase
        root.after(1500, lambda: practice_window(kana_list[1:], kana_dict, new_score, total))

    # check answer and go to next one
    button_check = tk.Button(root, text="Check Answer", command=check_and_next)
    button_check.pack(pady=5)

    # when pressing <return> -> call check_and_next() fun
    root.bind("<Return>", lambda event: check_and_next())


def main_menu(info=""):
    clear_window()

    # welcome label
    label_welcome = tk.Label(root, text="Welcome to KANA Practice", font=("Times-Roman", 16))
    label_welcome.pack(pady=20)

    # option buttons
    button_practice = tk.Button(root, text="Begin", command=settings_window)
    button_practice.pack(pady=30)
    button_exit = tk.Button(root, text="Exit", command=root.destroy)
    button_exit.pack(pady=5)

    label_info = tk.Label(root, text=info, font=("Times-Roman", 12))
    label_info.pack(pady=20)


main_menu()

root.mainloop()