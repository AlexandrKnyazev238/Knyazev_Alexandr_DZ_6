# Task_4

from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        all_list = zip_longest(users, hobby)

        with open('users_hobby.txt', 'w', encoding='utf-8') as f:
            for i in all_list:
                print(f'{str(i[0]).strip()}: {str(i[1]).strip()}', file=f)
