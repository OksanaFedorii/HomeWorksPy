#Трикутник існує тоді, коли сумма двох його сторін більше за третю сторону.
#Тобто у трикутника зі сторонами a, b, c мають виконуватись такі вимоги: a + b > c. a + c > b, b + c > a.
# Периметр трикутника - то є сума всіх його сторін, тобто p = a + b + c

def serch_side(text):
   while True:
    number = int(input(f'{text}'))
    if number > 0:
       return number
    else:
       print("введіть число юільше за 0")

def corect_triagone(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = a + b + c
        return p
    else:
        print("трикутник неправильний, оновіть дані")

first_side = serch_side("Ведіть сторону а: ")
second_side = serch_side("Ведіть сторону b: ")
third_side = serch_side("Ведіть сторону c: ")
print(first_side, second_side, third_side)
perimetr = corect_triagone (first_side, second_side,third_side)
print("Периметр трикутника =", perimetr)