my_text = input("Введіть текст: ")
print(my_text)
what_we_seek = "("
what_we_seek_2 = ")"
i = my_text.find(what_we_seek)
j = my_text.find(what_we_seek_2)
while i != -1:
    #print(i)
    i = my_text.find(what_we_seek, i + 1)
    if what_we_seek == "(" and i != -1:
        what_we_seek.replace("(", "")
while j != -1:
    j = my_text.find(what_we_seek_2, j + 1)
    if what_we_seek_2 == ")" and j != -1:
        what_we_seek_2 = ")"
    # Визначаємо індекс перших та останніх дужок
    find_first_index = my_text.find("(")
    print(find_first_index)
    find_second_index = my_text.find(")")
    print(find_second_index)
    # Робимо зріз тексту за індексом та вносимо потрібний зріз (дужки та текст в нім) в змінну
    inserted_text = my_text[find_first_index: find_second_index + 1]
    # робимо перевірку на наявність зрізу в тексті та змінюємо даний зріз на пустоту (тобто видаляємо його)
    if inserted_text in my_text:
        my_text = my_text.replace(inserted_text, "")
print(my_text)