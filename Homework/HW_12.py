#  функція fibonacci_sequence є генератором послідовності чисел Фібоначчі
def fibonacci_sequence(end_index):
    # змінні a та b та їхні початкові значення: a = 0 та b = 1
    a, b = 0, 1
    # Використовуючи цикл for ми проходимо через ітерації від 0 до end_index - 1.
    # Змінна _ використовується як псевдонім для ітерацій
    for _ in range(end_index):
        # У тілі циклу ми використовуємо ключове слово yield, що робить функцію генератором.
        # Функція повертає поточне значення і призупиняє своє виконання.
        # Коли генератор викликається знову, виконання продовжується з місця призупинки і значення a оновлюється.
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # створюємо змінну end_index, яка визначає кінцевий індекс елементу послідовності, який ми хочемо згенерувати
    end_index = 10

    sequence = fibonacci_sequence(end_index)
    # У циклі for ми проходимо по sequence і виводимо кожен елемент послідовності чисел Фібоначчі
    for number in sequence:
        print(number)