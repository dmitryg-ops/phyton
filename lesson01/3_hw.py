"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

var = int(input('Введите число: '))    # Запрашиваме у пользователя число

var1 = int( '%s' % var)                # Обозначаем переменную и присваеваем ей значение, которое ввёл пользователь
var2 = int('%s%s' % (var, var))
var3 = int('%s%s%s' % (var, var, var))
print(var1 + var2 + var3)




