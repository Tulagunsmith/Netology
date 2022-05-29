text = ['2018-01-01', 'yandex', 'cpc', 100]
reversed_text = list(reversed(text))

dictionary = {reversed_text[1]: reversed_text[0]}

for i in range(2, len(reversed_text)):
    matreshka = {reversed_text[i]: dictionary}
    dictionary = matreshka
print(matreshka)
