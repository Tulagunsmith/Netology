queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]
counter_one_word, counter_two_words, counter_three_words, counter_four_and_more = 0, 0, 0, 0
for i in queries:
    if len(i.split()) == 1:
        counter_one_word += 1
    if len(i.split()) == 2:
        counter_two_words += 1
    if len(i.split()) == 3:
        counter_three_words += 1
    if len(i.split()) >= 4:
        counter_four_and_more += 1


print(*[f'Поисковых запросов из одного слова {round(counter_one_word * 100 / len(queries))} %, ',
      f'Поисковых запросов из двух слов {round(counter_two_words * 100 / len(queries))} %, ',
      f'Поисковых запросов из трёх слов {round(counter_three_words * 100 / len(queries))} %, ',
      f'Поисковых запросов из четырёх и более слов {round(counter_four_and_more * 100 / len(queries))} %'], sep='\n')
