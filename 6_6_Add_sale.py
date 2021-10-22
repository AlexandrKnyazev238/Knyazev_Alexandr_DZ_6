# Task_6_Add_sale

from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as donut_f:
    with open('bakery.csv', 'r', encoding='utf-8') as donut_g:
        if len(argv) > 1 and [i for i in argv[1:] if '.' in i and i.replace('.', '').isdigit()]:
            if round(float(argv[1]), 3) <= 99999.999:
                print(f'{round(float(argv[1]), 3):>010}', file=donut_f)
            else:
                print('Number must be less than 99 999,999')
        else:
            print(donut_g.read())
