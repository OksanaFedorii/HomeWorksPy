# ФУНКЦІЯ - багаторазове використання фрагменту програми.
# 1. Дозволяє з'єднувати декілька інструкцій в один блок -- присвоїть ім'я блоку--- звертатись по імені блоку---
# -- виконання інструкцій всередині блоку скільки хочеш разів і в будь-якій частині програми

# Функція Def (definition - визначення)

# def <name - ім'я функції/блоку>(): ім'я обєкту - це силка, дужки і те що в них - це те що воно робитиме
    # тіло
# Ім'я функції рекомендовано писати як дієслово бо вона щось робить
def say_hello():
    print("Hello")
    print("world")
    print("and everybody")
# якщо цей блок просто запустити то він не спрацює бо це задання ф-ї, а викликати її треба з нового рядку
# між визначенням функції та викликом її треба пропустити 2 рядки
say_hello()
print("pause")
# Викликати одну і ту ж функцію можна багато разів
say_hello()

#def send_mail():
#    text = "Дорогий користувач нашого продукту ... бла-бла"
#    print(text)

#send_mail()

def send_mail(from_name, old):   #(from_name) - це параметр - це визначення всередині ф-ї
    text = f"Дорогий користувач {from_name} ми раді, що ви з нами {old} років ... бла-бла"
    print(text)

send_mail("Оксана Андріївна", "5")  #("Оксана Андріївна") - аргумент - це передача значення при виклику ф-ї
# Скільки параметрів, стільки і аргументів

def square(x):
    print("Квадрат числа", x, "=", x ** 2)
#square(5)
#square(10)
for i in range(1, 12):
    square(i)

def multiplay(a, b):
    print(a * b)
multiplay(3, 5)
# можна міняти аргументи, проте використовувати одну і ту ж ф-ю
multiplay(60, 20)

def number(d):
    if d % 2 == 0:
        print(d, " - even")
    else:
        print(d, " - odd")
for i in range (20, 31):
    number(i)



if 5 > 7:
    def priclad():
        print("OK")
else:
    def priclad():
        print("Not ok")
priclad()

def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res
print(get_sqrt(49)) # можна присвоїть змінну результату
# resalt = get_sqrt(якесь число)
#print(resalt)

def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return (res, x)   # Виводимо дані за допомогою кортежу
a, b = get_sqrt(36)
print(a, b)  # a - приймає значення res, b - значення х ( тобто те, що ми вводимо в get_sqrt)

# ф-я return - повертає значення

def get_max2(a, b):
    return a if a > b else b
# x, y = 5, 7           ----- можна
#print(get_max2(x, y))        ось так  ( спочатку присвоївши нові змінні)
print(get_max2(6, 9))      # або так  ( напряму вказувати значення а та b)


# щоб порівняти 3 аргументи
def get_max2(a, b):
    return a if a > b else b
x, y, z = 5, 7, 9
print(get_max2(x, get_max2(y, z))) # спочатку порівнюється y та z і те що більше порівнюється з x


def get_max2(a, b):
    return a if a > b else b
x, y, z, u = 5, 7, 9, 12
print(get_max2(x, get_max2(y, get_max2(z, u))))

def get_rect(a, b):
    return 2 * (a + b)
print(get_rect(6,9))  #Вписуємо будь-які значення

def even(x):
    return x % 2 == 0
for i in range (1,21):
    if even(i):
        print(i)

#def read_user_number(user_prompt):
#    while True:
#        number = input(f"{user_prompt}\n: ")
#        try:
#            number = float(number)
#            break
#        except Exception:
#            print(f" Не вдалось отримати ціле число із введення: '{number}, повторіть спробу")

# read_user_number(user_prompt)
#read_user_number("введіть сторону трикутнику а = ")
#read_user_number("Введіть ціну за 1л топлива: ")
#read_user_number("Скільки вам повних років: ")
#read_user_number(" Яка температура повітря: ")
# Такий метод не виводить print бо викристовуємо брейк і не присвоюємо нові змінні

#def read_user_number(user_prompt):
#    while True:
#        number = input(f"{user_prompt}\n: ")
#        try:
#            number = float(number)
#            # return - Повертає значення і виходить з функції
#            return number
#        except Exception:
#            print(f" Не вдалось отримати ціле число із введення: '{number}, повторіть спробу")

#a = read_user_number("введіть сторону трикутнику а = ")
#cost = read_user_number("Введіть ціну за 1л топлива: ")
#age = read_user_number("Скільки вам повних років: ")
#temperature = read_user_number(" Яка температура повітря: ")
#print(a, cost, age, temperature)



def read_user_number(user_prompt, lower_bound, upper_bound):
    while True:
        number = input(f"{user_prompt}: ")
        try:
            number = float(number)
            if lower_bound < number < upper_bound:
                return number
            else:
                print(f"Введіть число від {lower_bound} до {upper_bound}")
        except Exception:
            print(f" Не вдалось отримати ціле число із введення: '{number}, повторіть спробу")

a = read_user_number("введіть сторону трикутнику а = ", 0, 999999)
cost = read_user_number("Введіть ціну за 1л топлива: ", 0, 999999)
age = read_user_number("Скільки вам повних років: ", 0, 150)
temperature = read_user_number("Яка температура повітря: ", -999999, 999999)
print(a, cost, age, temperature)







