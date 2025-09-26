import pytest

from project import generate_kana, terminal_inquiry


HIRAGANA = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o"
}

def test_generate_kana():
    # random function - set seed!
    # assert generate_kana() ==


def test_terminal_inquiry():
    kana_list = ["あ", "い"]
    assert terminal_inquiry(kana_list, HIRAGANA) == 


def test_function_n():
    ...
