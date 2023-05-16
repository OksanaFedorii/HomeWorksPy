user_name = input("Enter your name: ")
answer = f"HelLo!, my name {user_name}, I aM prograMMing on C++) What abOuT yoU? :)"
print(answer)
# Запитуємо яке слово хоче змінити користувач
replacing_word = input("What do you want to replace?: ")
print(replacing_word)
# Шукаємо індекс словосполучення в рядку
search_index = answer.index("C++")
found_index = f"{replacing_word},was found at position {search_index} "
print(found_index)
# Запитуємо на яке слово будемо змінювати
replaced_word = input("With what do you want to replace?: ")
print(replaced_word)
# Видаляємо з рядку символи пунктуації
result_1 = answer.replace(",", "").replace(")", "").replace("?", "").replace("!", "").replace(".", "").replace(":", "")
# Видаляємо зайві пробіли з правого кінця рядка
result_2 = result_1.rstrip()
# Здійснюємо заміну слова в рядку
result_3 = result_2.replace(replacing_word, replaced_word)
# Переводимо рядок в нижній регістр
result_4 = result_3.lower()
print(result_4)
