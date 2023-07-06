from dog import Dog
from cow import Cow
from hen import Hen
from cat import Cat
from animal import Animal
from random import choices, randint

if __name__ == '__main__':
    preferred_food = ['траву', 'сіно', 'овочі', 'зерно', 'пшоно', 'кашу', 'мясо', 'корм', 'рибу']
    cat = Cat("Мурчик", 6, "був на огляді")
    dog = Dog("Гавчик", 3, "не був на огляді")
    hen = Hen("Коко", 2, "не була на огляді")
    cow = Cow("Корівка", 4, "була на огляді")
    my_animals = [cat, dog, hen, cow]

    for animal in my_animals:
        for random_food in choices(preferred_food, k=3):
            animal.eat(random_food)
        print("-" * 80)
        print(animal.history())
        print("Якщо тварина голодна, погодуйте її")
        mood = animal.treat(randint(1, 5))
        print(mood)
        print("=" * 80)
