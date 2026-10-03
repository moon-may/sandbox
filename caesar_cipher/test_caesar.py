from caesar import *
import pytest

# todo структуру улучшить

# в строке присутствуют цифры
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
def test_correct_encrypt_input():
    assert encrypt('абв', 1) == 'бвг'

def test_correct_decrypt_input():
    assert decrypt('бвг', 1) == 'абв'

def test_negative_shift():
    assert encrypt('опрст', -1) == 'нопрс'

# сдвиг больше, чем число букв в алфавите
@pytest.mark.parametrize(
        'text, shift, offset', [
            ('привет', 35, 2), 
            ('мир', 43, 10)
        ]
)
def test_shift_above_alphabet(text, shift, offset):
    assert encrypt(text, shift) == encrypt(text, offset)

def test_above_alphabet():
    assert encrypt('я', 3) == 'в'
    assert encrypt('б', -5) == 'ь'

def test_symbol_input():
    assert encrypt('ура!', 3) == 'цуг!'