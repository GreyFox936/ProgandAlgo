import os
import csv
import time
from datetime import datetime

# Дефолтный путь к файлу
input_folder = r'C:\UTMN\Python'  # Здесь указываем папку с исходными файлами
output_folder = 'output-data'  # Папка для сохранения обработанных данных


# Функция для обработки каждой строки
def process_row(row):
    # Получаем данные из строки
    name = row['name']
    sex = row['sex']

    # Преобразуем возраст в число
    try:
        age = float(row['age'])  # Преобразуем возраст в число
    except ValueError:
        age = 0  # Если ошибка — ставим 0

    # Преобразуем сумму чека
    try:
        bill = float(row['bill'])
    except ValueError:
        bill = 0  # Если ошибка — ставим 0

    # Получаем тип устройства, браузер и регион
    device_type = row['device_type']
    browser = row['browser']
    region = row['region']

    # В зависимости от пола, выбираем соответствующее слово
    if sex == 'female':
        sex_str = 'женского пола'
        action = 'совершила'
    else:
        sex_str = 'мужского пола'
        action = 'совершил'

    # Выбираем строку для типа устройства
    if device_type == 'mobile':
        device_str = 'с мобильного'
    elif device_type == 'desktop':
        device_str = 'с компьютерного'
    elif device_type == 'laptop':
        device_str = 'с лаптопного'
    elif device_type == 'tablet':
        device_str = 'с планшетного'
    else:
        device_str = 'с неизвестного устройства'  # Если тип устройства не известен

    # Форматируем возраст — если целое число, выводим без десятичных
    if age.is_integer():
        age = int(age)

    # Формируем итоговую строку для записи в файл
    result = (f"Пользователь {name} {sex_str}, {age} лет {action} покупку на {bill} у.е. "
              f"{device_str} браузера {browser}. Регион с которого совершалась покупка: {region}.\n\n")

    return result


# Функция для обработки CSV файла
def process_csv(file_path, start_time):
    processed_data = []

    # Открываем файл и читаем строки
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Обрабатываем каждую строку
        for row in reader:
            processed_data.append(process_row(row))

    # Получаем текущую дату и время для имени файла
    timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M")

    # Генерируем имя для выходного файла
    base_name = os.path.basename(file_path).replace('.csv', '')
    output_file = os.path.join(output_folder, f"{timestamp}-outfile-{base_name}.txt")

    # Записываем результат в файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join(processed_data))

    # Замедляем выполнение на 5 секунд, чтобы проверить таймер
    time.sleep(5)

    # Печатаем статистику по времени и количеству обработанных строк
    end_time = time.time()
    print(f"Обработано {len(processed_data)} строк. Время выполнения: {end_time - start_time:.2f} секунд.")
    print(f"Результат записан в файл: {output_file}")


# Главная функция
def main():
    # Путь к файлу с данными
    selected_file = os.path.join(input_folder, 'web_clients_correct.csv')  # Здесь жестко указываем путь к файлу
    print(f"Выбран файл: {selected_file}")
    start_time = time.time()  # Время начала обработки
    process_csv(selected_file, start_time)


if __name__ == '__main__':
    main()
