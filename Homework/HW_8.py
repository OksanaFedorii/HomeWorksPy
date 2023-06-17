init_message = "Введіть одне з ключових слів наведених в прикладі: "
print("Введіть ключове слово 'add' якщо бажаєте додати нотатку. \n"
      "Введіть ключове слово 'earliest' якщо бажаєте переглянути нотатки в хронологічній послідовності. \n"
      "Введіть ключове слово 'latest' якщо бажаєте переглянути нотатки від найстаріших до найновіших. \n"
      "Введіть ключове слово 'longest' якщо бажаєте переглянути найдовші нотатки. \n"
      "Введіть ключове слово 'shortest' якщо бажаєте переглянути найкоротші нотатки. \n"
      "Введіть ключове слово 'exit' якщо ви завершили роботу в нотатнику.")

# Створюємо пустий список
my_tuple_list = []


# Створюємо функцію для додавання нотатки
def added():
    new_note = input("Введіть нотатку: ")
    new_note = new_note.lower()
    # Визначення довжини нотатки введеної користувачем
    length = new_note.__len__()
    # Якщо нотатка містить якість символи, тоді ми записуємо цю нотатку та її довжину у вигляді tuple
    if length > 0:
        new_tuple_1 = (new_note, length)
        # print(new_tuple_1)
        # користувачу виводимо лише нотатку добавлену
        print(">", new_note)
        # додаємо нотатку + довжину її у вигляді tuple в створений заздалегідь список
        my_tuple_list.append(new_tuple_1)
        # print(my_tuple_list)


# Створюємо ф-ю для перегляду нотаток від найстаріших до найновіших в хронології
def old():
    for note in my_tuple_list:
        print(">", note[0])


# Створюємо ф-ю для перегляду нотаток від найновіших до найстаріших в хронології
def early():
    early_list = list(reversed(my_tuple_list))
    for note in early_list:
        print(">", note[0])


# Створюємо ф-ю для сортування нотаток від найдовжих до найкоротших. Сортуємо за допомогою ф-ї sorted та ф-ї lambda
# де сортування буде здійснюватись за другим елементом кожного кортежу (в другому елементі[1] в нас збережена довжина)
def long():
    sort_list = sorted(my_tuple_list, key=lambda x: x[1], reverse=True)
    # print(sort_list)
    for note in sort_list:
        print(">", note[0])


# Створюємо ф-ю для сортування нотаток від найкоротших до найдовших.
def short():
    sort_list = sorted(my_tuple_list, key=lambda x: x[1])
    # print(sort_list)
    for note in sort_list:
        print(">", note[0])


if __name__ == '__main__':
    main_word = input(init_message)
    while True:
        if main_word == "add":
            added()
            main_word = input(init_message)
        elif main_word == "earliest":
            early()
            main_word = input(init_message)
        elif main_word == "latest":
            old()
            main_word = input(init_message)
        elif main_word == "longest":
            long()
            main_word = input(init_message)
        elif main_word == "shortest":
            short()
            main_word = input(init_message)
        elif main_word == "exit":
            break
        else:
            print("Введені дані не є коректні, повторіть, будь-ласка спробу")
            main_word = input(init_message)
