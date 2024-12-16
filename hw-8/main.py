import os
import csv
import time
from datetime import datetime
################################# End import

### Работа с вводной и конечной директориями
# Динамическое определение путей для папок
input_dir = 'input-data'      # Папка с исходными файлами - по ней будет вестись динамический поиск
output_dir = 'output-data'    # Папка для вывода

# Проверяем наличие папок
if not os.path.exists(input_dir):
    print(f"Папка {input_dir} не найдена. Создаем...")
    os.makedirs(input_dir)    # Если не обнаружена - создаем

if not os.path.exists(output_dir):
    print(f"Папка {output_dir} не найдена. Создаем...")
    os.makedirs(output_dir)   # Если не обнаружена - создаем
### Конец папок

# Функция для обработки строк вводной CSV-шки
def process_row(row_data):
    # Извлекаем данные из строки
    client_name = row_data['name']
    client_sex = row_data['sex']

    # Преобразуем возраст в десятичный float
    try:
        client_age = float(row_data['age'])
    except ValueError:
        client_age = 0  # При возникновении ошибки ставим зеро

    # Преобразуем сумму чека в float
    try:
        purchase_amount = float(row_data['bill'])
    except ValueError:
        purchase_amount = 0  # Если ошибка, ставим 0

    # Специфичные типы
    device = row_data['device_type']
    browser_type = row_data['browser']
    region_location = row_data['region']

    # Логика для генерирования строк с полом и действиями
    if client_sex == 'male':
        sex_description = 'мужского пола'
        action_word = 'совершил'
    else:
        sex_description = 'женского пола'
        action_word = 'совершила'

    # Генерация части строки с типом устройства
    if device == 'desktop':
        device_description = 'с компьютерного'
    elif device == 'laptop':
        device_description = 'с лаптопного'
    elif device == 'mobile':
        device_description = 'с мобильного'
    elif device == 'tablet':
        device_description = 'с планшетного'
    else:
        device_description = 'с неизвестного устройства'  # Для неучтенных типов

    # Форматируем возраст — если это целое число, выводим без десятичных
    if client_age.is_integer():
        client_age = int(client_age)

    # Формируем строку для записи в файл
    result = (f"Пользователь {client_name} {sex_description}, {client_age} лет {action_word} покупку на {purchase_amount} у.е. "
              f"{device_description} браузера {browser_type}. Регион с которого совершалась покупка: {region_location}.\n\n")

    return result


# Функция для обработки CSV файла
def process_csv(file_path, start_time):
    processed_data = []

    # Открываем файл и читаем строки
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Обрабатываем каждую строку из CSV
        for row_data in reader:
            processed_data.append(process_row(row_data))

    # Получаем текущую дату и время для имени файла
    timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M")

    # Генерируем имя для выходного файла
    base_file_name = os.path.basename(file_path).replace('.csv', '')
    output_file = os.path.join(output_dir, f"{timestamp}-outfile-{base_file_name}.txt")

    # Записываем результат в файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join(processed_data))

    # Имитация задержки — например, для слабых систем или эмуляции нагрузки
    time.sleep(5)  # Задержка на 5 секунд

    # Печатаем статистику: сколько строк обработано и время выполнения
    end_time = time.time()  # Засекаем время окончания
    print(f"Обработано {len(processed_data)} строк. Время выполнения: {end_time - start_time:.2f} секунд.")
    print(f"Результат записан в файл: {output_file}")


# Главная функция
def main():
    # Папка с файлами
    if not os.path.exists(input_dir):
        print(f"Папка {input_dir} не найдена.")
        return

    # Список файлов в папке
    files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
    if not files:
        print("Нет файлов .csv в папке.")
        return

    # Выводим список файлов
    print("Доступные файлы:")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")

    # Запрашиваем у пользователя выбор
    while True:
        choice = input(f"Выберите файл (цифра от 1 до {len(files)}), или 0 для выхода: ")
        if choice == '0':
            print("Программа завершена.")
            break
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            selected_file = os.path.join(input_dir, files[int(choice) - 1])
            print(f"Выбран файл: {selected_file}")
            start_time = time.time()  # Время начала обработки
            process_csv(selected_file, start_time)
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == '__main__':
    main()
