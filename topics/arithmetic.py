# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ С ЧИСЛАМИ

# ===== 1. ПЛОЩАДЬ И ПЕРИМЕТР =====
def s_and_p():
    '''
    Программа запрашивает длину и ширину прямоугольника (int), вычисляет его площадь и периметр, выводит результат
    '''
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    s = a * b
    p = 2 * a + 2 * b
    print(f'Площадь прямогольника равна {s}\n'
          f'Периметр прямоугольника равен {p}')


# ===== 2. СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ =====
def mean():
    '''
    Программа запрашивает три числа (int или float), вычисляет их среднее арифметическое 
    и выводит результат с точностью до двух знаков после запятой.
    '''
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    mean = round((a + b + c) / 3, 2)
    print(f'Среднее арифметическое: {mean}')


# ===== 3. КОНВЕРТЕР СЕКУНД =====
def time_convert():
    '''
    Пользователь вводит количество секунд (int). 
    Программа переводит время в формат "часы:минуты:секунды"
    '''
    time = int(input('Введите целое количество секунд: '))
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60
    print(f'Конвертированное время: {hours}:{minutes}:{seconds}')


# ===== 4. СУММА ЦИФР ЧИСЛА =====
def sum_of_digits():
    '''
    Пользователь вводит целое число. 
    Программа находит сумму всех его цифр, не используя str.
    '''
    number = int(input('Введите целое число: '))
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    print(f'Сумма цифр: {total}')


# ===== 5. КАЛЬКУЛЯТОР СКИДКИ =====
def discount():
    '''
    Пользователь вводит стоимость товара и процент скидки. 
    Программа выводит итоговую стоимость после скидки.
    '''
    count = int(input('Введите стоимость: '))
    percent = int(input('Введите процент скидки: '))
    total = count - (count / percent)
    print(f'Цена со скидкой: {total}')


# ===== 6. ДЕЛИТЕЛИ ЧИСЛА =====
def divisors():
    '''
    Пользоваель вводит целое число, 
    программа выводит все делители этого числа
    '''
    number = int(input('Введите целое число: '))
    div_list = []
    for i in range(1, number+1):
        if number % i == 0:
            div_list.append(str(i))
    print (' '.join(div_list))


# ===== 7. ПРОСТОЕ ЧИСЛО =====
def is_prime():
    '''
    Функция возвращает True, если введенное пользователем число - простое
    Функция возвращает False, если введенное пользователем число - составное
    '''
    number = int(input('Введите целое число: '))
    if number == 1:
        return False
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            if count > 2:
                return False
    return True


'''
if __name__ == '__main__':
   mean()
   s_and_p()
   time_convert()
   sum_of_digits()
   discount()
   divisors()
   print(is_prime())
'''