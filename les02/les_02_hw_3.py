"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# Создаём словарь.
seasons = {
           'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)
}
# Просим пользователя ввести
month = int(input('Выберите месяц: '))
for key in seasons.keys():           # Создаём цикл по поиску ключа в словаре
    if month in seasons[key]:
        print(key)

