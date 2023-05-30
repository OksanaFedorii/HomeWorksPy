# Написати програму що перевіряє чи є введена строка дзеркальною (паліндромом).
# Вхідну строку треба перевести в один регістр, позбавити пробілів, переносів на нову строку та розділових знаків.

my_text = input("Введіть слово чи фразу: ")
punctuation = ',.!:?-+"`'
# Змінюємо текст: переводимо в нижній регістр, видаляємо пробіли, видаляємо переноси на новий рядок
updated_text = my_text.lower().replace(" ", "").strip().replace("\n", "")
# Запускаємо цикл for якщо знаки пунктуації є в змінній punctuation, то змінюємо текст видаляючи знаки пунктуації
for punctuation_symbol in punctuation:
    updated_text = updated_text.replace(punctuation_symbol, "")
print(updated_text)
# Робимо інверсію рядка і порівнюємо їх
if updated_text[::-1] == updated_text:
    print("Даний рядок є паліндромом")
elif updated_text[::-1] != updated_text:
    print("Даний рядок не є паліндромом")

