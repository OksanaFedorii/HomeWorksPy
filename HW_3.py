salute = input("Привітайтесь з ботом: ")
while True:
    answer = salute.lower()
    print(answer)
    if answer.find("привіт") != -1:
        print("привіт, я бот з України!")
        break
    elif answer.find("хай") != -1:
        print("привіт, я бот з України!")
        break
    elif answer.find("вітаю") != -1:
        print("привіт, я бот з України!")
        break
    elif answer.find("доброго дня") != -1:
        print("Доброго дня, я бот з України!")
        break
    elif answer.find("доброго вечора") != -1:
        print("доброго вечора, я бот з України!")
        break
    elif answer.find("доброго ранку") != -1:
        print("доброго ранку, я бот з України!")
        break
    else:
        print("Ключових слів не знайдено")
        print("Дуже цікаво, але не зрозуміло, спробуй знову")
        salute = input("Привітайтесь з ботом: ")

interest = input('Ти можеш розмовляти зі мною як з другом, давай спробуємо, задай мені "людське питання": ')
while True:
    answer_1 = interest.lower()
    print(answer_1)
    if answer_1.find("справи") != -1:
        print("добре, адже вчусь програмувати на Python!")
        break
    elif answer_1.find("що робиш") != -1:
        print("вчусь програмувати на Python!")
        break
    elif answer_1.find("займаєшся") != -1:
        print("вчусь програмувати на Python!")
        break
    elif answer_1.find("життя") != -1:
        print("добре, адже вчусь програмувати на Python!")
        break
    else:
        print("Ключових слів не знайдено")
        print("Дуже цікаво, але не зрозуміло, спробуй знову")
        interest = input('Ти можеш розмовляти зі мною як з другом, давай спробуємо, задай мені "людське питання": ')

interest_1 = input("Напиши чим ти зазвичай займаєшся, коли маєш вільний час: ")
while True:
    answer_2 = interest_1.lower()
    print(answer_2)
    if answer_2.find("фільм") != -1:
        print('ого, круто, ти певно кіноман, знаю чудовий фільм з назвою "Платформа", якщо не дивився, то рекомендую!')
        break
    elif answer_2.find("серіал") != -1:
        print('ого, круто, маю для тебе чудовий серіал з назвою "Готем", думаю тобі сподобається')
        break
    elif answer_2.find("мульт") != -1:
        print('це дуже мило, всі ми трішки діти, знаю чудовий мультфільм "Ліло і Стіч", думаю тобі сподобається')
        break
    elif answer_2.find("граю") != -1:
        print('круто, ти певне знавець в Game сфері, знаю чудову гру з назвою "Кіберпанк", думаю тобі сподобається')
        break
    elif answer_2.find("читаю") != -1:
        print('це похвально, знаю чудову книгу з назвою "Зелена миля" автор С.Кінг, думаю тобі сподобається')
        break
    else:
        print("Ключових слів не знайдено")
        print("Дуже цікаво, але не зрозуміло, спробуй знову")
        interest_1 = input("Напиши чим ти зазвичай займаєшся, коли маєш вільний час: ")

interest_2 = input("Був радий поспілкуватись з тобою. До зустрічі: ")
while True:
    answer_3 = interest_2.lower()
    print(answer_3)
    if answer_3.find("бувай") != -1:
        print("побачимось у мережі, I'll be back.")
        break
    elif answer_3.find("до побачення") != -1:
        print("побачимось у мережі, I'll be back.")
        break
    elif answer_3.find("бай") != -1:
        print("побачимось у мережі, I'll be back.")
        break
    elif answer_3.find("до зустрічі") != -1:
        print("побачимось у мережі, I'll be back.")
        break
    elif answer_3.find("добраніч") != -1:
        print("побачимось у мережі, I'll be back.")
        break
    elif answer_3.find("пока") != -1:
        print("побачимось у мережі, I'll be back.")
        break
    else:
        print("Ключових слів не знайдено")
        print("Дуже цікаво, але не зрозуміло, спробуй знову")
        interest_2 = input("Був радий поспілкуватись з тобою. До зустрічі: ")
