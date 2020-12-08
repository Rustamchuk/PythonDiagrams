'''В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.'''

multiple_numbers = [2, 99]
dividers = [i for i in range(2, 10)]
multiple_count = 0

for i in range(multiple_numbers[0], multiple_numbers[-1] + 1):
    for j in dividers:
        if i % j != 0:
            break
    else:
        multiple_count += 1

print(f'В диапозоне от {multiple_numbers[0]} до {multiple_numbers[1]} есть {multiple_count} чисел кратных числам от {dividers[0]} до {dividers[-1]}')
