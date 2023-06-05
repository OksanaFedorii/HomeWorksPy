#Записуємо функцію де дане введене значення має бути цілим числом та більшим або рівним нулю, інакше відпрацьовує else
def my_time(text):
    while True:
        input_time = int(input(f'{text}: '))
        if 0 <= input_time:
            return input_time
        else:
            print(f'Число: {input_time} не є додатним, повторіть спробу')

# Записуємо словник, де value вказано в секундах ( переведення згідно таблиці)
time_in_second = {
    "день": 86400.00,
    "година": 3600.00,
    "хвилина": 60.00
}


# записуємо ф-ю де ділимо введене користувачем число на за допомогою ф-ї на ціле та залишок
def separate_time(input_seconds):
    div = divmod(input_seconds, time_in_second["день"])
    # Цілому числу надаємо змінну
    days = div[0]
    # із залишком переходим на ділення другої умови ...
    input_seconds = div[1]
    div = divmod(input_seconds, time_in_second["година"])
    hours = div[0]
    input_seconds = div[1]
    div = divmod(input_seconds, time_in_second["хвилина"])
    minutes = div[0]
    input_seconds = div[1]
    #повертаємо значення та записуємо їх у вигляді словнику
    return dict(days=days, hours=hours, minutes=minutes, seconds=input_seconds)


if __name__ == '__main__':
    seconds = my_time("Введіть ціле число: ")
    time = separate_time(seconds)
    print(time)
