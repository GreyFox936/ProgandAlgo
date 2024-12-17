import re #gexxx

# Регулярка для формата номеров РФ
pattern = re.compile(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}(?P<region>\d{2,3})$')
car_plate = 'АБ22ВВ193'  # Тут номерок, который проверяем

# Проводим
result = pattern.match(car_plate)

if result:
    # Номерок прошел 
    print(f"Результат: Номер {car_plate} валиден. Регион: {result['region']}")
else:
    # Номерок не прошел
    print(f"Результат: Номер {car_plate} не валиден")
