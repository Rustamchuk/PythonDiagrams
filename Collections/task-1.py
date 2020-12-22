'''Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.'''

import collections

buisness_counter = int(input('Сколько преддприятий - '))
earning = collections.Counter()

for i in range(buisness_counter):
    name = input('название - ')
    first = int(input('1 - '))
    second = int(input('2 - '))
    third = int(input('3 - '))
    fourth = int(input('4 - '))
    earning[name] = first + second + third + fourth

medium_earning = 0

for i in earning:
    medium_earning += earning[i]

medium_earning /= 2

print(f'средний заработок - {medium_earning}')

less_earning = collections.Counter()
more_earning = collections.Counter()

for i in earning:
    if medium_earning > earning[i]:
        less_earning[i] = earning[i]
    elif medium_earning <= earning[i]:
        more_earning[i] = earning[i]

print('меньше среднего заработка - ', end='')
for i in less_earning:
    print(f'{i}', end=', ')

print()

print('больше среднего заработка - ', end='')
for i in more_earning:
    print(f'{i}', end=', ')

