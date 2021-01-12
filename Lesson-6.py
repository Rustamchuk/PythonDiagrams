# First Variant
import sys
import random


def Count_memory(things):
    summ = 0
    for thing in things:
        summ += sys.getsizeof(thing)
    return summ


# FirstLesson

number = str(random.randint(100, 999))
summ = 0
prod = 1

for f in number:
    summ += int(f)
    prod *= int(f)

# SecondLesson

number = str(random.randint(10, 500))
even = 0
odd = 0
for f in number:
    i = int(f)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

# ThirdLesson


r = [random.randint(0, 99) for _ in range(10)]
index_even = []

for n in r:
    if n % 2 == 0:
        index_even.append(r.index(n))

# Counting

# FirstVariant

count_things = [summ, prod]
print(f'First lesson first task is {Count_memory(count_things)}')

count_things = [number, even, odd]
print(f'Second lesson second task is {Count_memory(count_things)}')

count_things = [r, index_even]
print(f'Third lesson Second task is {Count_memory(count_things)}')

# SecondVariant

print(f'First lesson first task is {sys.getsizeof(summ) + sys.getsizeof(prod)}')
print(f'Second lesson Second task is {sys.getsizeof(number) + sys.getsizeof(even) + sys.getsizeof(odd)}')
print(f'Third lesson Second task is {sys.getsizeof(r) + sys.getsizeof(index_even)}')

# ThirdVariant

memory = 0
memory_thing = [summ, prod]
for thing in memory_thing:
    memory += sys.getsizeof(thing)
print(f'First lesson first task is {memory}')

memory = 0
memory_thing = [number, even, odd]
for thing in memory_thing:
    memory += sys.getsizeof(thing)
print(f'Second lesson Second task is {memory}')

memory = 0
memory_thing = [r, index_even]
for thing in memory_thing:
    memory += sys.getsizeof(thing)
print(f'Third lesson Second task is {memory}')
