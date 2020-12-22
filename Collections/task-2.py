'''Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
 их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
 Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].'''

import collections

first = input('first number - ')
second = input('second number - ')

first_in_ten = 0
second_in_ten = 0

j = 0
for i in first[::-1]:
    if i == 'A':
        i = 10
    elif i == 'B':
        i = 11
    elif i == 'C':
        i = 12
    elif i == 'D':
        i = 13
    elif i == 'E':
        i = 14
    elif i == 'F':
        i = 15

    first_in_ten += int(i) * 16 ** j

    j += 1

j = 0
for i in second[::-1]:
    if i == 'A':
        i = 10
    elif i == 'B':
        i = 11
    elif i == 'C':
        i = 12
    elif i == 'D':
        i = 13
    elif i == 'E':
        i = 14
    elif i == 'F':
        i = 15

    second_in_ten += int(i) * 16 ** j

    j += 1

results = collections.Counter(summ = first_in_ten + second_in_ten, total = first_in_ten * second_in_ten)

number = results['summ']
results['summ'] = ''
while (number != 0):
    summ1 = number % 16
    number = number // 16

    if summ1 == 10:
        results['summ'] += 'A'
    elif summ1 == 11:
        results['summ'] += 'B'
    elif summ1 == 12:
        results['summ'] += 'C'
    elif summ1 == 13:
        results['summ'] += 'D'
    elif summ1 == 14:
        results['summ'] += 'E'
    elif summ1 == 15:
        results['summ'] += 'F'
    else:
        results['summ'] += str(summ1)
results['summ'] = results['summ'][::-1]

number = results['total']
results['total'] = ''
while (number != 0):
    total1 = number % 16
    number = number // 16

    if total1 == 10:
        results['total'] += 'A'
    elif total1 == 11:
        results['total'] += 'B'
    elif total1 == 12:
        results['total'] += 'C'
    elif total1 == 13:
        results['total'] += 'D'
    elif total1 == 14:
        results['total'] += 'E'
    elif total1 == 15:
        results['total'] += 'F'
    else:
        results['total'] += str(total1)
results['total'] = results['total'][::-1]

print(f'сумма - {results["summ"]}')
print(f'произведение - {results["total"]}')