import random
import sys
import re
import os

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.ttfonts import TTFError
from pyfiglet import Figlet


HIRAGANA = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o",

    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",

    "さ": "sa",
    "し": "shi",
    "す": "su",
    "せ": "se",
    "そ": "so",

    "た": "ta",
    "ち": "chi",
    "つ": "tsu",
    "て": "te",
    "と": "to",

    "な": "na",
    "に": "ni",
    "ぬ": "nu",
    "ね": "ne",
    "の": "no",

    "は": "ha",
    "ひ": "hi",
    "ふ": "fu",
    "へ": "he",
    "ほ": "ho",

    "ま": "ma",
    "み": "mi",
    "む": "mu",
    "め": "me",
    "も": "mo",

    "や": "ya",
    "ゆ": "yu",
    "よ": "yo",

    "ら": "ra",
    "り": "ri",
    "る": "ru",
    "れ": "re",
    "ろ": "ro",

    "わ": "wa",
    "を": "wo"
}

KATAKANA = {
    "ア": "a",
    "イ": "i",
    "ウ": "u",
    "エ": "e",
    "オ": "o",

    "カ": "ka",
    "キ": "ki",
    "ク": "ku",
    "ケ": "ke",
    "コ": "ko",

    "サ": "sa",
    "シ": "shi",
    "ス": "su",
    "セ": "se",
    "ソ": "so",

    "タ": "ta",
    "チ": "chi",
    "ツ": "tsu",
    "テ": "te",
    "ト": "to",

    "ナ": "na",
    "ニ": "ni",
    "ヌ": "nu",
    "ネ": "ne",
    "ノ": "no",

    "ハ": "ha",
    "ヒ": "hi",
    "フ": "fu",
    "ヘ": "he",
    "ホ": "ho",

    "マ": "ma",
    "ミ": "mi",
    "ム": "mu",
    "メ": "me",
    "モ": "mo",

    "ヤ": "ya",
    "ユ": "yu",
    "ヨ": "yo",

    "ラ": "ra",
    "リ": "ri",
    "ル": "ru",
    "レ": "re",
    "ロ": "ro",

    "ワ": "wa",
    "ヲ": "wo"
}

KANA_MAP = {
    "HIRAGANA": HIRAGANA,
    "KATAKANA": KATAKANA
}


def main():
    # intro
    f = Figlet(font='standard')
    print(f.renderText("Welcome to KANA Practice"), end="")
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    print("|=-=-=>    Generate KANA (Hiragana/Katakana)   <=-=-=|")
    print("|=-=-=>    phrases and write them in Romaji    <=-=-=|")
    print("|=-=-=>          (the classic alphabet).       <=-=-=|")
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")

    # 'start again' loop
    while True:
        print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
        print("|=-=-=-=-=>          KANA Practice         <=-=-=-=-=|")
        print("|=-=-=>      1) Start a new practice round     <=-=-=|")
        print("|=-=-=>      2) Generate a PDF with phrases    <=-=-=|")
        print("|=-=-=>                 3) Exit                <=-=-=|")
        print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
        option = input("Choose an option [1-3]: ")

        match option:
            case "1":
                # keep only python file name in 'sys.argv'
                sys.argv = sys.argv[:1]
                print(game_init())
            case "2":
                name = input("Name of the PDF file (including .pdf): ")
                # insert new filename into 'sys.argv[1]'
                if len(sys.argv) == 1:
                    sys.argv.append(name)
                else:
                    sys.argv[1] = name
                print(game_init())

            case "3":
                print(f.renderText("ARIGATOU"))
                sys.exit(0)
            case _:
                print("Invalid option")
                print(f.renderText("ARIGATOU"))
                sys.exit(0)


def game_init():
    """
    Initiate KANA practice puzzle game.
    Returns str, either score in terminal version or success message in pdf version.

    """

    # check filename
    checked = None
    if len(sys.argv) > 1:
        checked = check_filename(sys.argv[1], "pdf")
        if not checked[0]:
            print("|=-=-=-=>           Invalid filename         <=-=-=-=|")
            print("|=>  Valid characters: [a-z A-Z 0-9 . - _ <space>] <=|")
            sys.exit(0)

    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    print("|=-=-=-=-=-=-=>      alphabets:        <=-=-=-=-=-=-=|")
    print("|=-=-=-=-=-=>    HIRAGANA / KATAKANA     <=-=-=-=-=-=|")
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    kana_type = input("Alphabet: ").strip().upper()

    # check correct alphabet
    if kana_type not in KANA_MAP:
        return f"|=-=-=>    beep beep... invalid alphabet 🤖    <=-=-=|"
    else:
        kana_dict = KANA_MAP[kana_type]

    number_of_phrases = get_pos_int("Number of phrases? ")
    number_of_characters = get_pos_int("Number of characters per phrase? ", maximum=5)

    # generate random list with kana phrases
    kana_list = generate_kana(number_of_characters, kana_dict, number_of_phrases)

    # terminal version
    if len(sys.argv) == 1:
        # inquiry user for romaji translations
        score = terminal_inquiry(kana_list, kana_dict)

        # print out user's score
        return f"You scored {score}/{number_of_phrases}! Well done :D"

    # save to pdf version
    else:
        save_pdf(f"{checked[1]}", kana_list, kana_dict, number_of_phrases)
        return f"|=>  beep beep... 'export/{checked[1]}' saved into files 🤖  <=|"


def check_filename(filename, filetype):
    """
    Return list where first item is True/False and second item is name of the file.

    filename - str, name of the file.
    filetype - str, file format (e.g., 'pdf', 'txt').
    """

    pattern = rf"^([\w\.\- ]+)\.{re.escape(filetype)}$"
    match = re.search(pattern, filename, re.IGNORECASE)

    if match:
        return [True, filename]
    else:
        return [False]

def generate_kana(char_per_phrase, kana_dict, phrases_num=1):
    """
    Returns list of KANA characters.

    char_per_phrase - int, number of characters to return.
    kana_dict - dict, dictionary with chosen kana.
    phrases_num - int, number of 'phrases' to return in a list (default=1).
    """

    characters = []
    for _ in range(phrases_num):
        phrase = ""
        for _ in range(char_per_phrase):
            phrase += random.choice([key for key in kana_dict.keys()])

        characters.append(phrase)
    return characters


def terminal_inquiry(kana_list, kana_dict):
    """
    Returns count of correct answers.

    kana_list - list, list with kana phrases.
    kana_dict - dict, dictionary with chosen kana.
    """

    score = 0

    for phrase in kana_list:
        if check_phrase(phrase, kana_dict):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! {phrase} - {kana_to_romaji(phrase, kana_dict)}")

    return score


def check_phrase(phrase, kana_dict):
    """
    Returns true or false whether input corresponds with dict values.

    phrase - str, str to check with.
    kana_dict - dict, dictionary with chosen kana.
    """

    guess = input(f"{phrase}: ")
    phrase = kana_to_romaji(phrase, kana_dict)

    return guess.strip().lower() == phrase


def kana_to_romaji(phrase, kana_dict):
    """
    Returns phrase in romaji alphabate (classic alphabet).

    phrase - str, str to convert.
    kana_dict - dict, dictionary with chosen kana.
    """

    return "".join([kana_dict[char] for char in phrase])


def save_pdf(filename, kana_list, kana_dict, phrase_count):
    """
    Saves a pdf with kana phrases, blank lines and answers at the bottom.

    filename - str, name of the saved file.
    kana_list - list, kana phrases to translate.
    kana_dict - dict, dictionary with chosen kana.
    phrases_count - int, number of phrases in the kana_list.
    """

    # make sure file 'export' exist in the directory
    os.makedirs("export", exist_ok=True)

    # register Japanese font
    try:
        pdfmetrics.registerFont(TTFont("NotoSansJP", "static/NotoSansJP-Regular.ttf"))
    except (FileNotFoundError, TTFError):
        print("Couldn't find 'static/NotoSansJP-Regular.ttf' font.")
        sys.exit(0)

    # initiate reportLab engine
    page_width = 595
    page_height = 842
    c = canvas.Canvas(f"export/{filename}", pagesize=(page_width, page_height))

    phrases_per_page = 30
    phrases_per_column = phrases_per_page // 2
    line_height = 38
    start_y = 660

    left_margin = 25
    right_margin = 305

    count = 0
    while count < phrase_count:
        # insert image template
        c.drawImage("static/template.png", 0, 0)

        # set font
        c.setFont("NotoSansJP", 20)

        page_items = kana_list[count:count + phrases_per_page]

        for i, phrase in enumerate(page_items):
            if i < phrases_per_column:
                x = left_margin
                y = start_y - (i * line_height)
            else:
                x = right_margin
                y = start_y - ((i - phrases_per_column) * line_height)

            underlines = "_" * (len(phrase)) * 2
            c.drawString(x, y, f"{i + 1}) {phrase} : {underlines}")

        # page number
        c.setFont("Times-Roman", 10)
        c.drawString(
            290, 40, f"{(count // phrases_per_page) + 1}/{(len(kana_list) // phrases_per_page) + 1}")

        # answers at the bottom
        c.setFont("Times-Roman", 5)
        answers = [f"{i + 1}) {kana_to_romaji(phrase, kana_dict)}" for i,
                   phrase in enumerate(page_items)]
        half = len(answers) // 2
        c.drawString(5, 15, "Answers: ")
        c.drawString(5, 10, (' | '.join(answers[:half])))
        c.drawString(5, 5, (' | '.join(answers[half:])))

        # go to next page
        c.showPage()

        # count increment
        count += phrases_per_page

    # save pdf to files
    c.save()


def get_pos_int(phrase="", maximum=60):
    """
    Return a positive int from user's input.

    phrase - str, optional string to prompt user.
    maximum - int, optional maximum boundry.
    """

    while True:
        try:
            number = int(input(phrase))
            if number > 0 and number <= maximum:
                return number
            else:
                print(f"Number must be between 1 and {maximum}")
        except ValueError:
            pass


if __name__ == "__main__":
    main()
