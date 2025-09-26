import tkinter as tk

from tkinter import messagebox
from project import KANA_MAP, generate_kana, kana_to_romaji, save_pdf


# create window
root = tk.Tk()
root.title("KANA Practice")
root.geometry("400x300")


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

    tk.Label(frame_alphabet, text="Choose alphabet:").grid(row=0, column=0, columnspan=2, pady=5)
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
            messagebox.showerror("Invalid input", "Please enter positive number only!")
            return
        
        # when valid:
        kana_dict = KANA_MAP[alphabet_var.get().upper()]

        if mode == 1:
            practice_window(generate_kana(num_characters, kana_dict, num_phrases), kana_dict)
        elif mode == 2:
            print("pdf gen")
            save_pdf("kana_practive.pdf", generate_kana(num_characters, kana_dict, num_phrases), kana_dict, num_phrases)
            # TODO: filename is hardcoded as well as filepath
            messagebox.showinfo("Saved", "Succesfully generated kana_practice.pdf file")
        else:
            messagebox.showerror("Error", "Something went wrong")
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
        main_menu(f"Your score is {score}/{total}")
        return

    clear_window()

    tk.Label(root, text="Convert KANA to Romaji").pack(pady=5)

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

    def check_and_next():
        user_input = entry_answer.get().strip().lower()
        correct_answer = kana_to_romaji(current_kana, kana_dict)

        if user_input == correct_answer:
            print("correct")
            new_score = score + 1
        else:
            messagebox.showerror("Incorrect answer", f"incorrect | {current_kana} - {correct_answer}")
            new_score = score

        # move to next kana phrase
        practice_window(kana_list[1:], kana_dict, new_score, total)

    button_check = tk.Button(root, text="Check Answer", command=check_and_next)
    button_check.pack(pady=5)


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

    label_info = tk.Label(root, text=info, font=("Times-Roman", 9))
    label_info.pack(pady=20)


main_menu()

root.mainloop()