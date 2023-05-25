salute = input("привітайтесь з ботом: ")
while True:
    answer = salute.lower()
    print(answer)
    if "привіт" in salute\
            or "хай" in salute \
            or "салют" in salute\
            or "доброго" in salute \
            or "добрий" in salute == answer:
        print("привіт, я бот з України!")
        break
    else:
        print("Ключових слів не знайдено")
        print("дуже цікаво, але не зрозуміло, спробуй знову")
        salute = input("привітайтесь з ботом: ")

salute_1 = input("як твої справи?: ")
while True:
    answer_1 = salute_1.lower()
    print(answer_1)
    if "хуйово" in salute_1 or "погано" in salute_1 or "кепсько" in salute_1 or "хріново" == answer_1:
        print("сумно, чим я тобі можу допомогти?")
        break
    elif "добре" in salute_1 or "чудово" in salute_1 or "прекрасно" in salute_1 or "чудово" == answer_1:
        print("це чудово, радий за тебе!")
        break
    else:
        print("Ключових слів не знайдено")
        print("дуже цікаво, але не зрозуміло, спробуй знову")
        salute_1 = input("як твої справи?: ")

salute_2 = input("що робиш?: ")