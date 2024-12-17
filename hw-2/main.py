import re #gex

# Запрашиваем у пользователя ввод слова:

input_valid = False
while not input_valid:
    word = input("Введите слово (только латинские или русские буквы, до 100 символов): ")

    # Проверка на соответствие регулярке
    if len(word) <= 100 and re.match("^[а-яА-Яa-zA-Z]+$", word):
        input_valid = True
    else:
        print("Введенная информация несоотстветвует заданному формату. Повторите.")

# Проверяем длину слова
length = len(word)

# Вычисляем и выводим среднюю букву или буквы
if length % 2 == 1:
    # Нечет - выводим одну среднюю букву
    middle_index = length // 2
    print(word[middle_index])
else:
    # Чёт - выводим две средних буквы
    middle_index1 = length // 2 - 1
    middle_index2 = length // 2
    print(word[middle_index1:middle_index2+1])
