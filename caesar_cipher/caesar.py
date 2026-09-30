# Реализация шифра Цезаря на Python для русского языка

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 
            'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 
            'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 
            'э', 'ю', 'я']

def encrypt(text, shift):
    coding_text = []
    cur_text = list(text)

    for i in cur_text:
        if i in alphabet:
            index = (alphabet.index(i) + shift) % 33
            coding_text.append(alphabet[index])
        else:
            coding_text.append(i)

    return ''.join(coding_text)


def decrypt(text, shift):
    coding_text = []
    cur_text = list(text)

    for i in cur_text:
        if i in alphabet:
            index = (alphabet.index(i) - shift) % 33
            coding_text.append(alphabet[index])
        else:
            coding_text.append(i)

    return ''.join(coding_text)
