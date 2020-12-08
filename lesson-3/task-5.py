'''В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.'''

import random

array = [random.randint(0, 100) for i in range(20)]
max_number = 0
min_number = 100
summ = 0

print(*array)

for i in array:
    if max_number < i:
        max_number = i
    elif min_number > i:
        min_number = i

first_index = 0
second_index = 0

if array.index(min_number) > array.index(max_number):
    first_index = array.index(max_number)
    second_index = array.index(min_number)
else:
    first_index = array.index(min_number)
    second_index = array.index(max_number)

for i in range(first_index + 1, second_index):
    summ += array[i]

print(f'сумм между максимальным {max_number} и минимальным {min_number} членами равна {summ}')
