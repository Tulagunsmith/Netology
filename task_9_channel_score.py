#  Два варианта решения. Программы выводят название канала с максимальным объёмом продаж.
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
for network, score in stats.items():
    if score == max(stats.values()):
        print(f'Канал с максимальным объёмом продаж:  {network}')
print('Канал с максимальным объёмом продаж: ',
      *[network for network, score in stats.items() if score == max(stats.values())])
