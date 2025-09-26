import tkinter as tk


# create window
root = tk.Tk()
root.title("KANA Practice")
root.geometry("400x300")


def clear_window():
    for widget in root.winfo_children():
        widget.destroy() # removes all widgets from window


def open_settings():
    clear_window()

    # frame for alphabet choosing
    frame_alphabet = tk.Frame(root)
    frame_alphabet.pack(padx=5, pady=5)

    # default selection
    alphabet_var = tk.StringVar(value="Hiragana")

    tk.Label(frame_alphabet, text="Choose alphabet:").grid(row=0, column=0, columnspan=2, pady=5)
    button_hiragana = tk.Radiobutton(frame_alphabet, text="Hiragana",variable=alphabet_var, value="Hiragana", command=lambda: print(alphabet_var.get()))
    button_hiragana.grid(row=1, column=0, padx=10, pady=3)
    button_katakana = tk.Radiobutton(frame_alphabet, text="Katakana", variable=alphabet_var, value="Katakana", command=lambda: print(alphabet_var.get()))
    button_katakana.grid(row=1, column=1, padx=10, pady=3)

    # frame for configuration
    frame_configure = tk.Frame(root)
    frame_configure.pack(padx=5, pady=5)

    # phrases count
    tk.Label(frame_configure, text="How many phrases:").grid(row=0, column=0, padx=5, pady=5)
    entry_phrases = tk.Entry(frame_configure).grid(row=0, column=1, padx=5, pady=2)

    # characters count
    tk.Label(frame_configure, text="How many characters per phrase:").grid(row=1, column=0, padx=5, pady=5)
    entry_phrases = tk.Entry(frame_configure).grid(row=1, column=1, padx=5, pady=5)

    # frame practice / generate PDF
    frame_option = tk.Frame(root)
    frame_option.pack(padx=5, pady=5)

    # practice/pdf button
    button_practice = tk.Button(frame_option, text="Start Practice", command=lambda: print("practice beginning"))
    button_practice.grid(row=0, column=0, padx=5, pady=5)
    button_pdf = tk.Button(frame_option, text="Generate PDF", command=lambda: print("PDF beginning"))
    button_pdf.grid(row=0, column=1, padx=5, pady=5)

    # back to menu button
    button_back = tk.Button(root, text="Back", command=main_menu)
    button_back.pack(pady=10)


def main_menu():
    clear_window()

    # welcome label
    label_welcome = tk.Label(root, text="Welcome to KANA Practice", font=("Times-Roman", 16))
    label_welcome.pack(pady=20)

    # option buttons
    button_practice = tk.Button(root, text="Begin", command=open_settings)
    button_practice.pack(pady=30)
    button_exit = tk.Button(root, text="Exit", command=lambda: print("exit"))
    button_exit.pack(pady=5)

main_menu()

root.mainloop()