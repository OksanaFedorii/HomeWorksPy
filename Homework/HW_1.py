# Завдання №4
required_distance = float(input("Введіть дистанцію, яку необхідно здолати: "))
fuel_consumption = float(input("Введіть витрату палива на 100 км: "))
fuel_price = float(input("Введіть ціну палива за літр: "))
# Визначаємо скільки літрів топлива піде на дану дистанцію
amount_of_fuel = fuel_consumption / 100 * required_distance
print(round(amount_of_fuel, 2))
# Визначаємо загальні витрати на топливо в даній поїздці
costs = amount_of_fuel * fuel_price
print(round(costs, 2))


# Завдання №3
income = float(input("Введіть число надходження: "))
percentage_tax = float(input("Введіть число податку: "))
# Визначаємо скільки потрібно сплатити податку
impost = income / 100 * percentage_tax
print(round(impost, 2))
# Визначаємо чистий дохід
net_profit = income - impost
print(round(net_profit, 2))
