# Ожидание пользовательского ввода
ticket = input("Введите номер билета: ")

# Проверяем, что номер состоит из 6 цифр и является числом
if len(ticket) == 6 and ticket.isdigit():

    first_sum = sum(int(digit) for digit in ticket[:3])
    last_sum = sum(int(digit) for digit in ticket[3:])

    # Проверка на счастливость и радостность
    if first_sum == last_sum:
        print("Счастливый билет")
    else:
        print("Несчастливый билет")
else:
    print("Неверный формат номера билета. Требуется ввести шестизначное число.")
