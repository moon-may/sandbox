from caesar import *
import pytest

# todo структуру улучшить

@pytest.mark.parametrize(
        'text, shift', [
            ('123', 0),
            ('123', 3),
            ('123', -5)
        ]
)
def test_entered_digits(text, shift):
    assert encrypt(text, shift) == text
    assert decrypt(text, shift) == text

# todo переписать с parametrize, добавить на дешифровку
#      пустые строки, сдвиг больше алфавита, сдвиг кратный 33, сдвиг 0,
#      пробелы, смешанный ввод, согласные
def test_correct_input():
    assert encrypt('абв', 1) == 'бвг'

def test_negative_shift():
    assert encrypt('опрст', -1) == 'нопрс'

def test_above_alphabet():
    assert encrypt('я', 3) == 'в'
    assert encrypt('б', -5) == 'ь'

def test_symbol_input():
    assert encrypt('ура!', 3) == 'цуг!'