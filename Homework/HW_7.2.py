# записуємо ф-ю де користувач вводить ціле число яке більше за 0 і менше за 100 з поверненням значення
def number(text):
    while True:
        input_number = input(f'{text}: ')
        try:
            input_number = int(input_number)
            if 0 < input_number < 100:
                return input_number
            # якщо умови if були не пройдені то працює else
            else:
                print(f'Число: {input_number} не задовільняє вимоги, введіть число від 0 до 100')
        # Якщо помилка введення то відпрацьовує except
        except Exception:
                print(f" Не вдалось отримати ціле число із введення: '{input_number}, повторіть спробу")

# пишемо ф-ю якщо дане число є в ряді простих чисел - True
def is_simple(a):
    return a in simple_set

if __name__ == '__main__':
    integer = number("Введіть ціле число: ")
    # Ряд простих чисел
    simple_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    while True:
        if is_simple(integer):
            print("Дане число є простим")
            break
        else:
            print("Дане число не є простим")
            break