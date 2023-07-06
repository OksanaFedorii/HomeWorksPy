from animal import Animal


class Cat(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            vet_appointment: str
    ):
        """
        Клас відповідає за симуляцію життя собаки
        """
        super().__init__(
            name=name,
            age=age,
            say_word="Мяв-Мяв",
            preferred_food={'кашу', 'мясо', 'корм', 'рибу'},
            vet_appointment=vet_appointment
        )
        self.animal_type = 'Кіт'

    def treat(self, hours: int) -> str:
        """
        Доглядаючи за твариною певну кількість часу, ми отримуємо хороший настрій
        :param hours: скільки годин доглядали
        :return: нічого або хороший настрій
        """
        if hours > 2:
            f'Ви гладили {self} {hours} годин, у вас та кота підіймається настрій'
            return 'Ви приділили достатньо часу даній тварині, що задовільняє її потреби'
        f'Ви гладили {self} {hours} годин.'
        return 'Ви приділили мало часу коту. Кіт потребує вашого догляду та уваги'
