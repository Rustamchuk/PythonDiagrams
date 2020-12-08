'''В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.'''

import random

array = [random.randint(-100, 100) for i in range(20)]
min_negativ = -100

print(*array)

for i in array:
    if 0 > i > min_negativ:
        min_negativ = i

print(f'Максимальный отрицательный член - {min_negativ} на позиции {array.index(min_negativ)}')
