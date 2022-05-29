#  Программа, которая определяет знак зодиака
month = input('Введите месяц своего рождения: ').lower()
day = int(input('Введите день своего рождения: '))
zodiak = ''
print()


if month == 'март' and 20 < day < 32 or month == 'апрель' and 0 < day < 21:
    zodiak = 'Овен'
if month == 'май' and 0 < day < 22 or month == 'апрель' and 20 < day < 31:
    zodiak = 'Телец'
if month == 'май' and 21 < day < 32 or month == 'июнь' and 0 < day < 22:
    zodiak = 'Близнецы'
if month == 'июль' and 0 < day < 23 or month == 'июнь' and 21 < day < 31:
    zodiak = 'Рак'
if month == 'июль' and 21 < day < 32 or month == 'август' and 0 < day < 22:
    zodiak = 'Лев'
if month == 'сентябрь' and 0 < day < 24 or month == 'август' and 21 < day < 32:
    zodiak = 'Дева'
if month == 'сентябрь' and 23 < day < 31 or month == 'октябрь' and 0 < day < 24:
    zodiak = 'Весы'
if month == 'ноябрь' and 0 < day < 23 or month == 'октябрь' and 23 < day < 32:
    zodiak = 'Скорпион'
if month == 'ноябрь' and 22 < day < 30 or month == 'декабрь' and 0 < day < 23:
    zodiak = 'Стрелец'
if month == 'январь' and 0 < day < 21 or month == 'декабрь' and 22 < day < 32:
    zodiak = 'Козерог'
if month == 'январь' and 20 < day < 31 or month == 'февраль' and 0 < day < 20:
    zodiak = 'Водолей'
if month == 'март' and 0 < day < 21 or month == 'февраль' and 19 < day < 30:
    zodiak = 'Рыбы'


print('Вывод:', zodiak, sep='\n')
