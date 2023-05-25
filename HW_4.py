# Створюємо пустий список
new_list = []
# Запускаємо цикл
while True:
    # Просимо в користувача ввести данні
    user_input = input("Ввідіть число або 'sum' для отримання суми введених чисел: ")
    # Видаляємо "-" якщо число відємне, бо "-" не є числом і ми отримуємо тип даних str, а нам потрібно тип даних float
    # Перевіряємо чи в рядку введено лише числа
    if user_input.replace("-", "").isdigit():
        # Змінюємо тип даних за для отримання дробового числа
        user_input = float(user_input)
        # Додаємо введене число до списку
        new_list = new_list + [user_input]
        # Виводимо оновлений список
        print(new_list)
    elif user_input == "sum":
        # Якщо користувач ввів слово sum цикл зупиняється
        break
    else:
        # Спрацьовує якщо користувач ввів не число та не sum
        print("введено некоректні дані")
# Додаємо всі числа в списку
total_sum = sum(new_list)
# Вивдимо результат
print(total_sum)





