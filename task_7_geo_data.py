#  Программа создает список с уникальными значениями координат по мере их появления в словаре
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

data = set()

# for user, num in ids.items():
#     for i in range(len(num)):
#         if num[i] not in data:
#             data.append(num[i])


for user, num in ids.items():
    for i in range(len(num)):
        data.add(num[i])
print(list(data))
