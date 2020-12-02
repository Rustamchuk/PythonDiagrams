'''В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.'''

from random import randint


def SearchAnswer(chance):
    user_answer = int(input('Что думаете? '))

    if right_answer == user_answer:
        return True
    elif chance == 0:
        return False
    else:
        if user_answer > right_answer:
            print('Правильный ответ меньше')
        else:
            print('Правильный ответ больше')

        chance -= 1
        return SearchAnswer(chance)


right_answer = randint(0, 100)
chance = 10

print('Угадайте число от 0 до 100')

if SearchAnswer(chance):
    print('Right!')
else:
    print("You're lousier!")
