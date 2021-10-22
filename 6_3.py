# Task_3

from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        if len(users.readline()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open('users_hobby.json', 'w', encoding='utf-8') as f:
                all_list = zip_longest((' '.join(us.split(',')) for us in users), hobby)
                new_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}

                dump(new_dict, f, ensure_ascii=False, indent=4)
            print(new_dict)
        else:
            exit(1)
