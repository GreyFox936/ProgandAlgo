def move_disks(n, source, target, inbetween, moves_list, counter):
    debug_flag = True  # Флаг отладки

    if debug_flag:
        counter[0] += 1  # Счётчик рекурсивных вызовов
        print(f"***[{counter[0]}] Запустили move_disks {counter[0]} раз для n = {n}")

    if n == 1:
        move = f"Блин 1: Стержень {source} -> Стержень {target}"
        moves_list.append(move)
        print(move)

        if debug_flag:
            print(f"[{counter[0]}] Для n = {n} прошли успешный if ")
            print(f"[{counter[0]}] Вышли из слоя if")
    else:
        move_disks(n - 1, source, inbetween, target, moves_list, counter)
        move = f"Блин {n}: Стержень {source} -> Стержень {target}"
        if debug_flag:
            print(f"[{counter[0]}] Для n = {n} провалились в else после первого рекурсивного вызова")
        moves_list.append(move)
        print(move)
        if debug_flag:
            print(f"[{counter[0]}] Для n = {n} дошли до середины рекурсивного else. Вызываем обратный move_disks")
        move_disks(n - 1, inbetween, target, source, moves_list, counter)
        if debug_flag:
            print(f"[{counter[0]}] Для n = {n} дошли до конца else после второго рекурсивного вызова; вышли из уровня рекурсии")
            print(f"[{counter[0]}] Вышли из слоя else")

def hanoi_tower(num_disks, num_rods):
    counter = [0]  # Счётчик слоёв рекурсии 
    if num_rods >= 3:  # Проверка выполнимости задачи
        moves_list = []  # Золотой словарь лучших мувов
        move_disks(num_disks, 1, 3, 2, moves_list, counter)  # Solution init
        # Запись решения в файл
        with open('решение.txt', 'w') as file:
            for move in moves_list:
                file.write(move + '\n')
    else:
        print("Недостаточно стержней для решения задачи.")

def main():
    # Запрос условий, вызов функции решения
    num_rods = int(input("Введите количество стержней: "))
    num_disks = int(input("Введите количество дисков: "))
    hanoi_tower(num_disks, num_rods)

if __name__ == "__main__":
    main()
