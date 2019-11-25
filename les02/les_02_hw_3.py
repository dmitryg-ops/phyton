"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

months = {
'1': 'jan', 'type': int,
'2': 'feb', 'type': int,
'3': 'mar', 'type': int,
'4': 'apr', 'type': int,
'5': 'may', 'type': int,
'6': 'jun', 'type': int,
'7': 'jul', 'type': int,
'8': 'aug', 'type': int,
'9': 'sep', 'type': int,
'10': 'oct', 'type': int,
'11': 'nov', 'type': int,
'12': 'dec', 'type': int,
}

for quest in months:
    tmp = input('Введите число: ')

print()

