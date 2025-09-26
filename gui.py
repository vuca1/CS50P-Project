import tkinter as tk

from project import KANA_MAP, generate_kana, kana_to_romaji


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

    # characters count
    tk.Label(frame_configure, text="How many characters per phrase:").grid(row=1, column=0, padx=5, pady=5)
    entry_characters = tk.Entry(frame_configure)
    entry_characters.grid(row=1, column=1, padx=5, pady=5)

    # frame practice / generate PDF
    frame_option = tk.Frame(root)
    frame_option.pack(padx=5, pady=5)

    #print(alphabet_var.get().upper())
    kana_dict = KANA_MAP[alphabet_var.get().upper()]

    # practice/pdf button
    button_practice = tk.Button(frame_option, text="Start Practice", command=lambda: practice_window(generate_kana(int(entry_characters.get()), kana_dict, int(entry_phrases.get())), kana_dict))
    button_practice.grid(row=0, column=0, padx=5, pady=5)
    button_pdf = tk.Button(frame_option, text="Generate PDF", command=lambda: print("PDF beginning"))
    button_pdf.grid(row=0, column=1, padx=5, pady=5)

    # back to menu button
    button_back = tk.Button(root, text="Back", command=main_menu)
    button_back.pack(pady=10)


def practice_window(kana_list, kana_dict, score=0, total=None):
    if total is None:
        total = len(kana_list)

    # exit to menu when answered all
    if len(kana_list) == 0:
        main_menu(f"Your score is {score}/{score}")

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

    def check_and_next():
        user_input = entry_answer.get().strip().lower()
        correct_answer = kana_to_romaji(current_kana, kana_dict)

        if user_input == correct_answer:
            print("correct")
            new_score = score
        else:
            print(f"incorrect | {current_kana} - {correct_answer}")

    button_check = tk.Button(root, text="Check Answer", command=lambda: practice_window(kana_list[1:], kana_dict))
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