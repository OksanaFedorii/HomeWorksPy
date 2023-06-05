# Записуємо ф-ю з параметрами
def read_user_number(user_prompt, lower_bound, upper_bound):
    # Запускаємо цикл
    while True:
        # присвоюємо зміну
        number = input(f"{user_prompt}: ")
        try:
            # вказуємо що данний об'єкт має бути дробовим числом
            number = float(number)
            # пропичуємо умови дане число має бути більшим за нижню межу(0) і меншим за верхню межу(99999)
            if lower_bound < number < upper_bound:
                # повертаємо значення
                return number
            # інакше відпацьовує умова else
            else:
                print(f"Введіть число від {lower_bound} до {upper_bound}")
        # Якщо виникає помилка введення ( не число, а рядок, то відпрацьовує except
        except Exception:
            print(f" Не вдалось отримати ціле число із введення: '{number}, повторіть спробу")


# Визначаємо скільки літрів топлива піде на дану дистанцію за допомогою ф-ї
def calc_amount_of_fuel(consumption, distance):
    return round(consumption / 100 * distance, 2)


# Визначаємо загальні витрати на топливо в даній поїздці за допомогою ф-ї
def calc_cost(amount1, amount2):
    return round(amount1 * amount2, 2)


if __name__ == '__main__':
    required_distance = read_user_number("Введіть дистанцію, яку необхідно здолати ", 0, 99999)
    fuel_consumption = read_user_number("Введіть витрату палива на 100 км ", 0, 99999)
    fuel_price = read_user_number("Введіть ціну палива за літр ", 0, 99999)
    amount_of_fuel = calc_amount_of_fuel(fuel_consumption, required_distance)
    print(amount_of_fuel)
    costs = calc_cost(amount_of_fuel, fuel_price)
    print(costs)
