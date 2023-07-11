def word_gen(text):
    # У цій функції рядок text розбивається на окремі слова за допомогою методу split()
    # результат зберігається у змінній words
    words = text.split()
    for word in words:
        # ключове слово yield, що перетворює функцію на генератор
        yield word


if __name__ == '__main__':
    text = 'i am generating words from text'
    word_generate = word_gen(text)
    for data in word_generate:
        print(data)
