#far_east = ['амурская область', 'республика бурятия', 'еврейская автономная область', 'забайкальский край',
#            'камчатский край', 'магаданская область', 'приморский край', 'республика саха',
#            'сахалинская область', 'хабаровский край', 'чукотский автономный округ']


base_percent = 20
region = input('Введите регион вашего проживания: ').lower()


#if region in far_east:
if region == 'амурская область' or region == 'республика бурятия' or region == 'еврейская автономная область':
    base_percent = 2
else:
    children = int(input('Сколько детей в вашей семье? '))
    salary = input('Имеется ли у вас зарплатный проект в нашем банке? д/н ').lower()
    insurance = input('Оформлена ли на вас страховка в нашем банке? д/н ').lower()
    if children >= 3:
        base_percent -= base_percent / 100
    if salary == 'д':
        base_percent -= base_percent * 0.5 / 100
    if insurance == 'д':
        base_percent -= base_percent * 1.5 / 100


print(f'Процентная ставка в нашем банке для вас составит: {base_percent}%')