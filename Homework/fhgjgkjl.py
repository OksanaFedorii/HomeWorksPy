STARTING_MENU = {
    "Американо": {
        "price": 20,
        "quantity": 50,
    },
    "Эспрессо": {
        "price": 15,
        "quantity": 50,
    },
    "Раф": {
        "price": 25,
        "quantity": 30,
    },
    "Чай альпийские луга": {
        "price": 13.5,
        "quantity": 50,
    },
    "Чай черный травяной альпийские луга": {
        "price": 135,
        "quantity": 50,
    },
    "Чай зелёный": {
        "price": 13,
        "quantity": 50,
    },
    "Круассан": {
        "price": 20,
        "quantity": 5,
    },
    "Пончик": {
        "price": 18,
        "quantity": 1,
    },
    "Пирожок": {
        "price": 15,
        "quantity": 0,
    },
}


def display_menu(menu: dict):
    """
    Функция красиво и презентабельно выводит на экран меню заведения
    :param menu: меню заведения в формате словаря
    """
    # pass можно вставлять после любого отступа как "затычку" для еще ненаписанного кода
    # позволяет программе выполняться без ошибок когда там еще не закончено заполнение логики
    # https://pyformat.info/
    # '{:10} {:20}'.format(test1, test2)
    # то же, что и ниже
    # f'{test1:10} {test2:20}'
    for key, value in menu.items():
        # print('{:20}'.format(key), value)
        if value["quantity"] > 0:
            print(f'{key:20} - {value["price"]}')


# ":" - прапорець для вказання форматування значення. Наприклад:
number = 3.14159
print("Значення числа: {:.2f}".format(number))    # Форматування: 2 значення після крапки
#  Вивід: Значення числа: 3.14


# ":>" - вирівнювання вправо. Наприклад:
name = "John"
print("Привіт, {:>10}!".format(name))
# Вивід: Привіт,       John!


# ":<" - вирівнювання вліво. Наприклад:
name = "John"
print("Привіт, {:<10}!".format(name))
# Вивід: Привіт, John      !

# ":^" - вирівнювання по центру. Наприклад:
name = "John"
print("Привіт, {:^10}!".format(name))
# Вивід: Привіт,   John   !

# ":+" - відображення знаку "+" або "-" для чисел з позначенням. Наприклад:
number = 10
print("Число: {:+}".format(number))
# Вивід: Число: +10

menu = {
    "Піца": {"price": 10, "quantity": 5},
    "Салат": {"price": 5, "quantity": 3},
    "Суп": {"price": 7, "quantity": 0},
    "Десерт": {"price": 3, "quantity": 2}
}

# Метод items() в Python використовується для повернення списку кортежів, які містять пари ключ-значення зі словника.
# Кожен кортеж містить ключ на першому місці і відповідне йому значення на другому місці.

for key, value in menu.items():
    if value["quantity"] > 0:
        print(f'{key:7} --- {value["price"]}')   # {key:7} відстань від key до value

menu_2 = {
    "Pizza": {
        "price": 9.99,
        "quantity": 5
    },
    "Burger": {
        "price": 5.99,
        "quantity": 10
    },
    "Salad": {
        "price": 4.99,
        "quantity": 3
    }
}

for key, value in menu_2.items():
    if value["quantity"] > 0:
        print(f'{key:10} - {value["price"]}')


# Приклад використання .items()
fruits = {
    "apple": 2,
    "banana": 5,
    "orange": 3
}

for key, value in fruits.items():
    print(f"{key:8} --- {value}")

""" import math as m """  # Використовується при імортувані довгих назв модулів
# print(m.sqrt(16))

# from math import sqrt   --- дозволяє імпотувати конкретні ф-ї по назві з з модуля, а не весь модуль
# from math import sqrt, cos  --- або декілька ф-й з модуля










