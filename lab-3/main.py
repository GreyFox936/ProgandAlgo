def splits(length, width, mem=None):

    # Проверяем словарь на наличие пред. расчетов
    if (length, width) in mem:
        return mem[(length, width)]


    if (width, length) in mem:  # Зеркалим
        return mem[(width, length)]



    # Проверка что не рассматриваем 1х1
    if length == 1 and width == 1:
        return 0

    # Рекурсивный случай: разрезаем шоколадку на два блока
    if length > width:
        # Разрезаем горизонтально
        result = 1 + splits(length // 2, width, mem) + splits(length - length // 2, width, mem)
    else:
        # Разрезаем вертикально
        result = 1 + splits(length, width // 2, mem) + splits(length, width - width // 2, mem)

    # Сохраняем результат
    mem[(length, width)] = result
    return result

# Ввод данных
length = int(input('Введите длину шоколадки: '))
width = int(input('Введите ширину шоколадки: '))

# Инициализация словаря mem
mem = {}

# Вызов функции
result = splits(length, width, mem)

# Вывод результата
print(f"Для деления шоколадки размером {length}x{width} на кусочки 1x1 потребуется: {result} ходов")

# Вывод содержимого словаря memo
print("Вывод mem:")
print(mem)

