"""
 5. Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
 Выведите соответствующее сообщение.
 Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
 Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

viruchka = int(input('Введите выручку: '))
izdershki = int(input('Введите издержки: '))
sotrudniki = int(input('Введите количество сотрудников:  '))
#rasxodi = int(input('Введите расходы: '))

pribil = viruchka - izdershki
print(pribil)
if pribil > 0:
print(f'Работаем {pribil} в плюсе !!!')
    rent = str(pribil / izdershki * 100) + '%'
    print(f'Рентабильность = {rent} ')
if sotrudniki > 0:
    result = pribil / sotrudniki
    print(f'Каждый сотрудник зарабатывает: {result}')


else:
    print(f'Работаем {pribil} в минус !!!')





