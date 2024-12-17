def find_matches(boys, girls):
    if len(boys) == len(girls):
        sorted_boys = sorted(boys)
        sorted_girls = sorted(girls)
        matches = zip(sorted_boys, sorted_girls)
        print("Идеальные пары:")
        for boy, girl in matches:
            print(f"{boy} и {girl}")
    else:
        print("Внимание, кто-то может остаться без пары.")


# Задаем переменную для выбора набора имен
massive_number = int(input("Введите 1 для первого набора имен или 2 для второго: "))
''' 
Гениальная механика выбора массива связана с нелюбовью автора к  
микроменджменту многострочных комментариев, во время сравнения работы ПО с разным набором данных
'''

# Первый набор
boys1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Второй набор
boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

# ifelse для выбора входного массива
if massive_number == 1:
    find_matches(boys1, girls1)
elif massive_number == 2:
    find_matches(boys2, girls2)
else:
    print("Введено неверное значение. Пожалуйста, выберите 1 или 2.")
