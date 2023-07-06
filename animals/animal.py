class Animal:
    def __init__(self, name: str, age: int, say_word: str, preferred_food: set, vet_appointment: str):
        """
        Клас відповідає за життєдіяльність тварини
        :param name: імя тварини
        :param age: вік тварини
        :param say_word: якою "фразою" тварина стимулює розмову
        :param preferred_food: раціон тварини
        """
        self.animal_type = '???'  # в дочірній
        self.name = name
        self.age = age
        self.say_word = say_word  # в дочірній
        self.preferred_food = preferred_food  # в дочірній
        self.hungry = "так"
        self.vet_appointment = vet_appointment

    def history(self):
        starting_str = f"{self.name}, {self.age} "
        # вказуємо умови для віку тварини
        if self.age == 1:
            starting_str += "рік"
        elif 2 <= self.age <= 4:
            starting_str += "роки"
        else:
            starting_str += "років"
        starting_str += f", голодний: {self.hungry}, чи була тварина у ветеринара: {self.vet_appointment}"
        return starting_str


    def eat(self, food: str):
        """
        Метод відровідає за симуляцію їжі на фермі
        Якщо запропонована їжа є в preferred_food, то тварина наїлась і self.hungry = False
        Інакше тварина не поїсть
        :param food: що їсть
        """
        if not self.hungry:
            return
        if food in self.preferred_food:
            print(f'{self.name} їсть {food}')
            self.hungry = "ні"
        else:
            print(f'{self.name} не їсть: {food}, {self.say_word}')

    def treat(self, hours: int):
        """
        Метод догляду за твариною
        :param hours: скільки годин ми проводимо з твариною
        :return: що отимуємо натомість
        """
        raise NotImplementedError
