def input_user(text):
    while True:
        number = float(input(f'{text}: '))
        if number > 0:
            return number
        else:
            print("введіть число більше за 0")


def calculate_gas(summ, distsnce):
    result = summ / 100 * distsnce
    return result


def spend(spended_gas, price):
    result_2 = spended_gas * price
    return result_2


required_distance = input_user("Введіть дистанцію, яку необхідно здолати: ")
fuel_consumption = input_user("Введіть витрату палива на 100 км: ")
fuel_price = input_user("Введіть ціну палива за літр: ")
# Визначаємо скільки літрів топлива піде на дану дистанцію
amount_of_fuel = calculate_gas(fuel_consumption, required_distance)
print(round(amount_of_fuel, 2))
# Визначаємо загальні витрати на топливо в даній поїздці
costs = spend(amount_of_fuel, fuel_price)
print(round(costs, 2))
