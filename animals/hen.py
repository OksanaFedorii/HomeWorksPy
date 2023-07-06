from animal import Animal
from random import randint


class Hen(Animal):
    """
    Клас відповідає за симуляцію життя курки
    """

    def __init__(
            self,
            name: str,
            age: int,
            vet_appointment: str
    ):
        super().__init__(
            name=name,
            age=age,
            say_word="Ко-ко-ко",
            preferred_food={'зерно', 'пшоно', 'трава'},
            vet_appointment=vet_appointment
        )
        self.animal_type = 'Курка'

    def treat(self, hours: int) -> str:
        """
        Доглядаючи за куркою певну кількість часу ми отримуємо 10 яєць
        Якщо доглядаємо менше- від 1 до 5 яєць
        :param hours: Скільки годин доглядаємо
        :return: від 1 до 10 яєць
        """
        if hours > 2:
            print(f'Ви доглядали {hours} годин і отримуєте 10 курячих яєць')
            return 'Ви приділили достатньо часу тварині'
        print(f'Ви доглядали {hours} годин внаслідок чого курка знесла мало яєць')
        return f'Ви приділили мало часу, тварина потребує вашого догляду курка знесла: {randint(1, 5)} шт.'
