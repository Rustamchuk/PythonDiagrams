'''Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.'''

print('Для остановки напишите 0')
max_number = int(input('Введите число - '))
user_answer = 1

while(user_answer != 0):
    user_answer = int(input('Введите число - '))

    if user_answer > max_number:
        max_number = user_answer

print('Максимальное число -', max_number)