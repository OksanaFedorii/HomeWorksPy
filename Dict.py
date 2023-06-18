# Dict (Dictinary) - словник
# Ключем можу бути  - лише рядок або  число
# Значенням (value) - число, рядок, вложений список, ...

# 1) Можна так записувати словник
"""
d = {key : value, key : value, key : value...}
print(d)
"""

# 2) Можна ось так
"""""
d = {
    key : value,
    key : value,
    key : value
}
print(d)
""""""


3) Коли вказуємо, що це список,( 1- ше значення буде - ключ, 2-ге - вміст).
Програма автоматично = між key та value  міняє на :
                        <---> = dict(key = value, key:value, ...) """
a = dict(сонце="гаряче", небо="синє", трава="зелена")
b = dict(Стіч=268, Ліло=543, Нану=245)
print(a, b)

# 4) Створення словника з вкладеного списку
c = [["квіти", 345], ["чашка", 657], ["дитина", 578]]
d = dict(c)
e = [["квіти", "рожеві"], ["чашка", "біла"], ["дитина", "мала"]]
f = dict(e)
print(d, f)

# 5) <--> = dict.fromkeys(["key1", "key2", "key3"], value)
# однакове значення присвоюється всім ключам словника
q = dict.fromkeys(["dog", "cat", "rat"], 3)
print(q)

# 6) dict.fromkeys(keys, value)
x = ('key1', 'key2', 'key3')
# однакове значення присвоюється всім ключам словника
y = 5, 3, 8, 12
thisdict = dict.fromkeys(x, y)
print(thisdict)

# 7) keys for the dictionary
alphabets = {'a', 'b', 'c'}
# value for the dictionary
# однакове значення присвоюється всім ключам словника
number = 1  # можна присвоїть рядок "я тут"
# creates a dictionary with keys and values
dictionary = dict.fromkeys(alphabets, number)
print(dictionary)
# Output: {'a': 1, 'c': 1, 'b': 1}

# 8) set of vowels
keys = {'a', 'e', 'i', 'o', 'u'}
# list of number
value = [1]  # може бути і декілька значень [ 7, 9, 6]
vowels = dict.fromkeys(keys, value)
print(vowels)
# updates the list value
value.append(2)  # щоб додати вкінець ще один value
print(vowels)

# 9) Cтворення пустого словнику <--> = dict
# Звернення до списку може бути по ключі
c = [["квіти", 345], ["чашка", "біла"], ["дитина", 578]]
d = dict(c)
print(d["квіти"], d["чашка"])

# щоб добавити новий ключ з значенням до словнику     <назва словнику>[назва ключа] = "str" або 4 або [ 1,2,5]
d["пес"] = "блакитний"
print(d)
print(d["пес"])

# щоб змінити value звертаємось до словника і в ним  ключа і писвоюємо нове значення
# словник - змінюючий тип об'єкту
d["чашка"] = "чиста"
print(d)

# exemple
person = {}
s = "Іванов Назар Сміла НУБіП 5 4 3 5 2 5"
a = s.split()
print(a)
person["name"] = a[0]
person["last_name"] = a[1]
person["city"] = a[2]
person["university"] = a[3]
person["marks"] = []
for i in a[4:]:
    person["marks"].append(int(i))
print(person)

""""" ЩОб видалити один елемент з словнику
del <назва словнику>[<назва ключа>]
print(<назва словнику>) 
"""""
del person["city"]
print(person)

# Функції словника
print(len(person))  # Підраховує скільки є пар key : vaule в словнику
print("name" in person, "dog" in person)  # Перевіряє чи така назва ключа є в словнику
print("пес" not in person)  # Впевнюємось в тому, що даної назви ключу нема в словнику

""""" пошук назви ключа в словнику та вивід значень словнику
for key in <назва словнику>:
    print(key, <назва словнику>[key]) """""
for name in person:
    print(name, person["name"])


# Методи словнику
""" 
1) <назва словнику>.clear()   ----- Очищує весь словник
#print(<назва словнику>)

person.clear()
print(person) """

""" 2) <назва словнику>.get(<назва ключа>) ---- отримаємо value даного ключа """
print(person.get("name"))

""" 3) <назва словнику>.setdefault(<назва ключа>) ---- отримаємо value даного ключа
Якщо назви ключа не знайдено, то помилки небуде, буде None в value саме в ньому
Можна створити ключ і присвоїти йому значення <назва словнику>.setdefault(<key>, <value>) """
print(person.setdefault("name"))  # Отримали value даного key
print(person.setdefault("dog"))  # Отрималь None бо назви такого key нема
print(person.setdefault("dog", 34))  # Створюємо новий ключ в словнику і надаємо йому value

""" 4)<назва словнику>.pop(key) ---- видаляє з словнику вказаний key та vaule """
print(person)   # словник до змін
person.pop("last_name")
print(person)   # словник після видалення вказаного ключа та значення

"""5) <назва словнику>.keys()    ---- виводить назви всіх key що є в словнику """
print(person.keys())

"""""6) виводить всі значення value що є в словнику
print(<назва словнику.values()
for value in <назва словнику>.values():
    print(value)"""
print(person.values())
for value in person.values():
    print(value)

""" 7)<назва словнику>.items() ----  повертає всі пари key: value даного словнику """
print(person.items())  # Виводть у вигляді списку
for para in person.items():    # Виводить у вигляді кортежів пари (в колонці)
    print(para)

print(person.items())
for key, value in person.items():
    print(key, value)

"""Завдання: Підрахувати  кількість об'єктів які зустрічаються при введені 
Де key - обєкти, value - кількість """
s = input("Впишіть значення: ")
print(s)
d = {}   # Створюємо словник
for i in s:     # Де і приймає будь-яке значення. Перевірка чи і є в s
    if i.isalpha():   # перевіряє чи це буква, якщо так то все ок, якщо ні, то пропускає цифри і знаки
        if i in d:  # Якщо це значення є в словнику то:
            d[i] += 1   # Тоді додаємо це значення +1 в словник
        else:
            d[i] = 1    # Інакше додаємо вперше це значення
for i in sorted(d):   #Сортує в алфавітному порядку значення і
    print(i, d[i])
# АБО можна записати все коротше
s = input("Впишіть значення: ")
print(s)
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1  # (i, 0) **** і - вже було і підставляєтся з словнику к-ть, а якщо ще не було - тому 0
for i in sorted(d):
    print(i, d[i])















