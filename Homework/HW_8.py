def added(notes):
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
        notes.append(new_tuple_1)
        # print(my_tuple_list)
    return notes


# Створюємо ф-ю для перегляду нотаток від найстаріших до найновіших в хронології
def old(notes):
    return notes


# Створюємо ф-ю для перегляду нотаток від найновіших до найстаріших в хронології
def early(notes):
    early_list = list(reversed(notes))
    return early_list


# Створюємо ф-ю для сортування нотаток від найдовжих до найкоротших.
def long(notes):
    sort_list = sorted(notes, key=lambda x: x[1], reverse=True)
    return sort_list


# Створюємо ф-ю для сортування нотаток від найкоротших до найдовших.
def short(notes):
    sort_list = sorted(notes, key=lambda x: x[1])
    return sort_list


def print_notes(notes):
    for note in notes:
        print(">", note[0])


if __name__ == '__main__':
    my_tuple_list = []
    init_message = "Введіть одне з ключових слів наведених в прикладі: "
    print("Введіть ключове слово 'add' якщо бажаєте додати нотатку. \n"
          "Введіть ключове слово 'earliest' якщо бажаєте переглянути нотатки в хронологічній послідовності. \n"
          "Введіть ключове слово 'latest' якщо бажаєте переглянути нотатки від найстаріших до найновіших. \n"
          "Введіть ключове слово 'longest' якщо бажаєте переглянути найдовші нотатки. \n"
          "Введіть ключове слово 'shortest' якщо бажаєте переглянути найкоротші нотатки. \n"
          "Введіть ключове слово 'exit' якщо ви завершили роботу в нотатнику.")
    main_word = input(init_message)
    while True:
        if main_word == "add":
            my_tuple_list = added(notes=my_tuple_list)
            main_word = input(init_message)
        elif main_word == "earliest":
            earliest = early(notes=my_tuple_list)
            print_notes(earliest)
            main_word = input(init_message)
        elif main_word == "latest":
            latest = old(notes=my_tuple_list)
            print_notes(latest)
            main_word = input(init_message)
        elif main_word == "longest":
            longest = long(notes=my_tuple_list)
            print_notes(longest)
            main_word = input(init_message)
        elif main_word == "shortest":
            shortest = short(notes=my_tuple_list)
            print_notes(shortest)
            main_word = input(init_message)
        elif main_word == "exit":
            break
        else:
            print("Введені дані не є коректні, повторіть, будь-ласка спробу")
            main_word = input(init_message)