# імпортуємо модуль для рандомного вибору
from random import choices, randint, random


# Створюємо клас
class Cat:
    def __init__(self, name: str, age: int, breed: str, preferred_food: set):
        # встановлюємо значення атибутів
        # ім'я кота
        self.name = name
        # вік кота
        self.age = age
        # порода кота
        self.breed = breed
        self.preferred_food = preferred_food
        # чи голодний кіт
        self.hungry = "Так"
        # скільки годин гуляв кіт
        self.hours_outdoors = 0
        # скільки годин спав кіт
        self.sleep = 0

    def __str__(self):
        starting_str = f"{self.breed.capitalize()} {self.name}, {self.age} "
        # вказуємо умови для віку тварини
        if self.age == 1:
            starting_str += "рік"
        elif 2 <= self.age <= 4:
            starting_str += "роки"
        else:
            starting_str += "років"
        starting_str += f", годин гуляв: {self.hours_outdoors}, годин спав: {self.sleep}, голодний: {self.hungry}"
        return starting_str

    # Функція мявкання
    def myaw(self, count: int):
        if count > 0:
            mew_str = '-'.join(["мяв"] * count).capitalize()
            print(f"{self.name} мявкає: {mew_str}!")

    # ф-я з визначення чи голодний кіт і що він буде чи не буде їсти
    def eat(self, food: str):
        if self.hungry:
            if food in self.preferred_food:
                print(f"{self.name} їсть {food}")
                self.hungry = "Ні "
            else:
                print(f"{self.name} таке не їсть: {food}")
                self.myaw(randint(1, 5))
        else:
            print(f"{self.name} не голодний")

    # функція визначає чи гуляв чи ні кіт, якщо гуляв то скільки часу
    def walk(self, walk: bool):
        if walk:
            hours = randint(1, 1)
            print(f"{self.name} гуляє {hours} годину")
        elif walk:
            hours = randint(2, 4)
            print(f"{self.name} гуляє {hours} години")
        else:
            hours = randint(5, 6)
            print(f"{self.name} гуляє {hours} годин")
        self.hours_outdoors += hours

    # функція визначає чи спав чи ні кіт, якщо спав то скільки часу
    def slept(self, nap: int):
        self.sleep += nap
        if nap == 1:
            print(f"Кіт спав {self.sleep} годину")
        elif 5 > nap > 2:
            print(f"Кіт спав {self.sleep} години ")
        else:
            print(f"Кіт спав {self.sleep} годин")


if __name__ == '__main__':
    # Дані про котів ( ім'я, вік, порода, що їсть)
    d = Cat('Мурчик', 3, "бурма", {'корм'})
    x = Cat('Сніжок', 4, "метис", {'мясо', 'кашу'})
    y = Cat('Тоторо', 3, "британець", {'рибу', 'мясо', 'кашу'})
    z = Cat('Рижик', 5, "мейнкун", {'мясо', 'корм'})
    q = Cat('Аанг', 1, "тібетський синій", {'мясо', 'рибу'})
    c = Cat('Олег', 9, "болотний", {'мясо', 'кашу'})
    cats = [d, x, y, z, q, c]
    # Створюємо список з їжі яку пропонуватимемо котам
    potential_food = ['корм', 'мясо', 'рибу', 'кашу', 'банан', 'виноград', 'редиску']
    print('Звичайний день в житті одного кота :)')
    print('-' * 36)

    # використовумо цикл для проходження всіх умов для кожного кота
    for cat in cats:
        # Кіт буде робити від 1 до 5 рандомних дій
        events_for_cat = randint(1, 5)
        for _ in range(events_for_cat):
            if random() > 0.5:
                print(f"Годуємо кота на ім'я {cat.name}")
                # Обирає 3 рандомних варіанти чим погодувати кота з вказаних варіантів в списку potential_food
                for random_food in choices(potential_food, k=3):
                    cat.eat(random_food)
            elif random() > 0.5:
                cat.walk(walk=True)
            elif random() > 0.5:
                cat.slept(randint(1, 3))

        print(f'Так пройшов день для: {cat}')
        print('=' * 75)
