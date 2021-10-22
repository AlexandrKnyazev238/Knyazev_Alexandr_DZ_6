# Task_2

with open('pars_logs.txt', 'w', encoding='utf-8') as p:
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        content = (f'{line.split()[0]} {line.split()[5][1:]} {line.split()[6]}' for line in f)
        for i in content:
            print(i, file=p)

import collections

with open('pars_logs.txt', 'r', encoding='utf-8') as f:
    new_dict = collections.Counter()

    for i in f:
        i = i.split()[0]
        new_dict[i] += 1

    ip, count = new_dict.most_common(1)[0][0], new_dict.most_common(1)[0][1]
    print(f'Spammer {ip} - {count} times')

#   Первый код взял у вас, он мне больше понравился и работает быстрее и в принципе
#   грамотнее, второй код у меня тоже рабочий получился, но длиннее и работает около минуты
#
# ip_numbers = {}
# with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#     file_lines = f.readlines()
#     f.seek(0)
#
#     for line in f:
#         new_line = f.readline()
#         ip = new_line.split()[0]
#         if ip not in ip_numbers:
#             log_filter = list(filter(lambda el: el.split()[0] == ip, file_lines))
#             ip_numbers[ip] = len(log_filter)
#         else:
#             continue
#
# key_val = ip_numbers.items()
# key_val_list = list(key_val)
# max_ip_number = max(key_val_list, key=lambda x: x[1])
# print(f'Spammer - {max_ip_number[0]} times - {max_ip_number[1]}')
