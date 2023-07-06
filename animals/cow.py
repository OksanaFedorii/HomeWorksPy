from animal import Animal


class Cow(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            vet_appointment: str
    ):
        """
        Клас відповідає за симуляцію життя корови
        """
        super().__init__(
            name=name,
            age=age,
            say_word="Муууууу",
            preferred_food={'траву', 'сіно, овочі'},
            vet_appointment=vet_appointment
        )
        self.animal_type = 'Корова'

    def treat(self, hours: int) -> str:
        """
        Доглядаючи за коровою певну кількість часу ми отримуємо молоко
        :param hours: час догляду
        :return: отримуємо молоко або нічого
        """
        if hours > 1:
            print(f'Ви доглядали {hours} годин і отримуєте відро молока')
            return 'Ви приділили достатньо часу даній тварині, що задовільняє її потреби'
        print(f'Ви доглядали {hours} годин - цього недостатньо, щоб отримати достатньо молока')
        return 'Ви приділили мало часу тварині. Корова потребує вашого догляду та уваги'
