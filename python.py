# tuple / кортёж
t = (1, 5.5, -10, 'the string', [1, 2, 4], False)
print(type(t), t)
 # t[2] = 20 - ми не можемо змінити бо кортеж незмінний
 # t.append('new item') - неможемо змінити бо він незмінний
# t.insert(1, -3) - добавити теж за допомогою функції неможна
t = t + (6, 3)
t = t + (5,)
#t.extend([8, 3]) - функції не працюють для змін кортеджу
# "x.extend(список)" то же, что и "x = x + список"
print(t)
print('len', len(t), t)
# Кортёж нельзя редактировать после его создания. Однако на основании кортежа можно создать новый кортёж
# Похожим образом работают строки
t[4].append(5)
print('len', len(t), t)

# set / множество - содержит только уникальные элементы
s = set()
# list не может быть частью set, потому что он может видоизменяться и не сообщать об этом сету.
# Тогда сет не может гарантировать уникальность своих элементов
# хэш таблица - таблица где все данные представлены в виде хэша и связи к их реальному значению. Например:
# hash1: 3
# hash2: 4.4
# ...
s = {3, 4.4, 5, 6, True, 'asdasd', (4, 5, 7), 5}
print(type(s), s)
# s[3] # по индексу к сету не обратишься
s.add(3)
s.add(4.5)
print('len', len(s), s)
s1 = {3, 5, 6, 8, 9}
s2 = {3, 5, 6, 2, 1}
# difference (разница) s1 - s2 выводит то, что есть в s1, но нету в s2
print(s1.difference(s2))
print(s1 - s2)
# union (объединение) - то что есть или в s1, или в s2. Хотя бы в одном из них
s3 = s1.union(s2)
print(type(s3), s3)
# intersection (пересечение) - То что есть и в s1, и в s2
print(s1.intersection(s2))

l = [1, 2, 3, 10, 20]
print(l[-200:])
print(l[200:])

# Def імя функції(параметр функції, параметр функції,...):     - можна декілька ф-й через кому
    # тіло функції з відступом
# параметр функції -
# Def read_user_number()

def read_user_number(user_promp):
    # тіло
    print(user_promp)
read_user_number("Tea")
read_user_number("Water")

# return - вихід з функції з поверненням якогось значення