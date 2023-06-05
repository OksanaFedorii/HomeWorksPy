# Імпортуємо модуль math
import math

# Викликаємо функцію def
def set_side(text):
    # Запускаємо цикл
    while True:
        # просимо користувача ввести дані, які відповідають вставленому тексту, присвоюємо зміну
        my_side = input(f"{text}: ")
        try:
            # вказуємо що даний об'єкт має бути цілим числом
            my_side = int(my_side)
            # дане число має бути більшим від нуля
            if my_side > 0:
                # Повертаємо значення
                return my_side
            # Інакше, якщо дане число є недодатнім, починаємо цикл знову ж
            else:
                print(f" Число: '{my_side} не є додатнім, повторіть спробу")
        # Даний блок вказує, що якщо буде помилка, то виведеться даний текст і цикл оновиться
        except Exception:
            print(f" Не вдалось отримати ціле число із введення: '{my_side}, повторіть спробу")


# запускаємо функцію яка буде перевіряти на можливість існування трикутника де а, b, c - сторони трикутника
def triangle(a, b, c):
    #  повертає значення якщо всі умови будуть дійсними
    return a + b > c and a + c > b and b + c > a


# запускаємо функцію яка визначає периметр трикутника
def perimeter(a, b, c):
    # повертає периметр трикутника
    return a + b + c


# запускаємо функцію яка визначає площу трикутника
def square(a, b, c):
    # визначаємо напівпериметр, присвоюємо йому змінну
    half_perimeter = perimeter(a, b, c) / 2
    # знаходимо площу трикутника з використанням формули та імпортованого модулю. Повертаємо значення
    return math.sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))


if __name__ == '__main__':
    first_side = set_side("Введіть a сторону трикутника ")
    second_side = set_side("Введіть b сторону трикутника ")
    third_side = set_side("Введіть c сторону трикутника ")
    #     трикутник правильний
    if triangle(first_side, second_side, third_side):
        p = perimeter(first_side, second_side, third_side)
        print("Перииметр трикутника =", p)
        s = square(first_side, second_side, third_side)
        print("Площа трикутника =", s)
    #     трикутник неправильний
    else:
        print("Трикутник неправильний")
