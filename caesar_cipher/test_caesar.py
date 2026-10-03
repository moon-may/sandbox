from caesar import *
import pytest

# Данные
NON_LETTERS_CASES = [
        ('123', 0),
        ('123', 3),
        ('123', -5),
        (' ', 20),
        ('!', 3),
        ('world', 7)
        ]

# Тесты для encrypt
def test_correct_encrypt_input():
    '''Корректный ввод encrypt, только буквы'''
    assert encrypt('абв', 1) == 'бвг'
    assert encrypt('АбВ', 1) == 'БвГ'

@pytest.mark.parametrize('text, shift', NON_LETTERS_CASES)
def test_encrypt_entered_digits(text, shift):
    '''
    В строке присутствуют некириллические символы для ф-ции encrypt:
        - цифры, 
        - латинские буквы,
        - знаки препинания,
        - пробел
    '''
    assert encrypt(text, shift) == text

def test_encrypt_negative_shift():
    '''Отрицательный сдвиг для ф-ции encrypt'''
    assert encrypt('опрст', -1) == 'нопрс'

def test_mixed_encrypt():
    '''Смешанный ввод для ф-ции encrypt'''
    assert encrypt('Привет, Python! 42', 5) == 'Фхнжйч, Python! 42'

@pytest.mark.parametrize(
        'text, shift, offset', [
            ('привет', 35, 2), 
            ('мир', 43, 10)
        ]
)
def test_encrypt_shift_above_alphabet(text, shift, offset):
    '''Сдвиг превышает число букв в алфавите для ф-ции encrypt'''
    assert encrypt(text, shift) == encrypt(text, offset)

@pytest.mark.parametrize(
        'text, shift, expected', [
            ('я', 3, 'в'),
            ('Я', 3, 'В'),
            ('б', -5, 'ь'),
            ('Б', -5, 'Ь')
        ]
)
def test_encrypt_above_alphabet(text, shift, expected):
    '''Проход через границу алфавита для ф-ции encrypt'''
    assert encrypt(text, shift) == expected


# Тесты для decrypt
def test_correct_decrypt_input():
    '''Корректный ввод decrypt, только буквы'''
    assert decrypt('бвг', 1) == 'абв'
    assert decrypt('Бвг', 1) == 'Абв'

@pytest.mark.parametrize('text, shift', NON_LETTERS_CASES)
def test_decrypt_entered_digits(text, shift):
    '''
        В строке присутствуют некириллические символы для ф-ции decrypt:
            - цифры, 
            - латинские буквы,
            - знаки препинания,
            - пробел
        '''
    assert decrypt(text, shift) == text

def test_decrypt_negative_shift():
    '''Отрицательный сдвиг для ф-ции decrypt'''
    assert decrypt('ножагр', -2) == 'привет'

def test_mixed_decrypt():
    '''Смешанный ввод для ф-ции decrypt'''
    assert decrypt('Фхнжйч, Python! 42', 5) == 'Привет, Python! 42'

@pytest.mark.parametrize(
        'text, shift, offset', [
            ('привет', 35, 2), 
            ('мир', 43, 10)
        ]
)
def test_decryrpt_shift_above_alphabet(text, shift, offset):
    '''Сдвиг превышает число букв в алфавите для ф-ции decrypt'''
    assert decrypt(text, shift) == decrypt(text, offset)

@pytest.mark.parametrize(
        'text, shift, expected', [
            ('в', 3, 'я'),
            ('В', 3, 'Я'),
            ('ь', -5, 'б'),
            ('Ь', -5, 'Б')
        ]
)
def test_decrypt_above_alphabet(text, shift, expected):
    '''Проход через границу алфавита для ф-ции decrypt'''
    assert decrypt(text, shift) == expected









