import pytest

from project import check_filename, check_phrase, generate_kana, kana_to_romaji, get_pos_int


HIRAGANA = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o"
}


def test_check_filename():
    assert check_filename("test.pdf", "pdf") == [True, "test.pdf"]
    assert check_filename("test_02.pdf", "pdf") == [True, "test_02.pdf"]
    assert check_filename("test 03.pdf", "pdf") == [True, "test 03.pdf"]




def test_check_invalid_fileformat():
    assert check_filename("test04.pfd", "pdf") == [False, "test04.pfd"]
    assert check_filename("test05", "pdf") == [False, "test05"]

def test_generate_kana_length():
    char_per_phrase = 4
    num_of_phrases = 10
    kana_list = generate_kana(char_per_phrase, HIRAGANA, num_of_phrases)
    assert len(kana_list) == num_of_phrases
    for phrase in kana_list:
        assert len(phrase) == char_per_phrase

def test_generate_kana_empty_dict():
    with pytest.raises(IndexError):
        generate_kana(3, {}, 4)
    


def test_kana_to_romaji():
    assert kana_to_romaji("あ", HIRAGANA) == "a"
    assert kana_to_romaji("あい", HIRAGANA) == "ai"



def test_check_phrase(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'ai')
    assert check_phrase("あい", HIRAGANA) == True

def test_check_phrase_wrong(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'ue')
    assert check_phrase("あい", HIRAGANA) == False




def test_get_pos_int(monkeypatch):
    inputs = iter(["-1", "abc", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_pos_int("Enter number: ") == 5


