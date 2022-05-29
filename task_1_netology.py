sq_side = int(input('Введите длину стороны квадрата: '))
perimeter = sq_side * 4

print('Периметр:', perimeter)
print(f'Площадь: {sq_side ** 2}')

orth_length = int(input('Введите длину прямоугольника: '))
orth_width = int(input('Введите ширину прямоугольника: '))
square = orth_length * orth_width

print(f'Периметр: {orth_length * 2 + orth_width * 2}')
print('Площадь:', square)

separator = input('Введите любой символ: ')

print(separator * (perimeter + square))

income = int(input('Введите размер вашей заработной платы: '))
mortgage = int(input('Введите, какой процент вы тратите в месяц на ипотеку: '))
spent = int(input('Введите, какой процент от зарплаты вы тратите в месяц на жизнь: '))

mortgage = int(mortgage * income / 100)
spent = int(spent * income / 100)

print(f'На ипотеку было потрачено: {mortgage * 12} рублей')
print(f'Было накоплено: {income * 12 - mortgage * 12 - spent * 12} рублей')
