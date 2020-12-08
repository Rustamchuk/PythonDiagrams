'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import random

array = [random.randint(0, 100) for i in range(20)]
max_number = 0
min_number = 100

print(*array)

for i in array:
    if max_number < i:
        max_number = i
    elif min_number > i:
        min_number = i

min_index = array.index(min_number)
array[array.index(max_number)] = min_number
array[min_index] = max_number

print(*array)
