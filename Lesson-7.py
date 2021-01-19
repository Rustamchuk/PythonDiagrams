import random

# 1
print('\n1\n')


def sort(list):
    n = 1
    while n < len(list):
        for i in range(len(list) - n):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        n += 1
    return list


list = []

for i in range(20):
    list.append(random.randint(-100, 100))

print(*sort(list)[::-1])

# 2
print('\n2\n')


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2

    left_part = array[:mid]
    right_part = array[mid:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    return merge_list(left_part, right_part)


def merge_list(list_1, list_2):
    result = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    result += list_1[i:]
    result += list_2[j:]
    return result


numbers = [random.randint(0, 50) for i in range(20)]

print(numbers)
print(merge_sort(numbers))

# 3
print('\n3\n')

list = [random.randint(0, 50) for i in range(21)]
print(*list)

list = sort(list)
print(*list)

middle = list[len(list) // 2]
print(middle)
