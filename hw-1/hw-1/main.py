# Ожидание ввода от пользователя
year = int(input("Введите год: "))

# Проверка на введение числового значения, и что значение находится в рамках hardcode диапазона для избежания перегрузок
if year < 0 or year > 20000:
    print("Введен недопустимый год!")
else:
    # Проверка на високосность - год делится на 4 без остатка, но не делится на 100, или год делится на 400 без остатка
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Високосный год")
    else:
        print("Обычный год")
