my_text = input("Введіть текст: ")
print(my_text)
# Запускаємо цикл де він буде працювати допоки було знайдено "(" та ")"
while my_text.find("(") != -1 and my_text.find(")", my_text.find("(")) != -1:
    # Визначаємо індекс перших та останніх дужок
    find_first_index = my_text.find("(")
    find_second_index = my_text.find(")", find_first_index)
    find_index_of_second_open_dujka = my_text.find("(", find_first_index + 1)
    # Треба переписати цю умову щоб рекурсивно перевіряти, що між "(" та ")" нема іншої "("
    while find_first_index < find_index_of_second_open_dujka < find_second_index:
        find_first_index = find_index_of_second_open_dujka
    # Робимо зріз тексту за індексом та вносимо потрібний зріз (дужки та текст в нім) в змінну
    inserted_text = my_text[find_first_index: find_second_index + 1]
    # робимо перевірку на наявність зрізу в тексті та змінюємо даний зріз на пустоту ('тобто видаляємо його)
    if inserted_text in my_text:
        my_text = my_text.replace(inserted_text, "")
print(my_text)
