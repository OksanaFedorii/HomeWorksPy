from animal import Animal


class Dog(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            vet_appointment: str,
    ):
        """
        Клас відповідає за симуляцію життя собаки
        """
        super().__init__(
            name=name,
            age=age,
            say_word='Гав-гав!',
            preferred_food={'кашу', 'мясо', 'корм'},
            vet_appointment=vet_appointment

        )
        self.animal_type = 'Собака'

    def treat(self, hours: int) -> str:
        """
        Доглядаючи за твариною певну кількість часу, ми отримуємо хороший настрій
        :param hours: скільки годин доглядали
        :return: нічого або хороший настрій
        """
        if hours > 2:
            f'Ви глуляли з {self} {hours} годин, у вас підіймається настрій'
            return 'Ви приділили достатньо часу даній тварині, що задовільняє її потреби'
        'Ви гуляєте з {self} {hours} годин.'
        return 'Ви приділили мало часу псу. Пес потребує вашого догляду та уваги'
