import random
a = random.randint(0, 100)
b = int(input(f'Введите число: '))
def f(a, b):
    if b < 0:
        print('Number should be more than 0 and less than 100')
        while a != b:
            b = int(input(f'Введите новое число: '))
            if a == b:
                print('You guessed!')
                break
            if a < b:
                print('Try less.')
            if a > b:
                print('Try more.')
    elif b >= 100:
        print('Number should be more than 0 and less than 100')
        while a != b:
            b = int(input(f'Введите новое число: '))
            if a == b:
                print('You guessed!')
                break
            if a < b:
                print('Try less.')
            if a > b:
                print('Try more.')
    elif a < b:
        print('Try less.')
        while a != b:
            b = int(input(f'Введите новое число: '))
            if a == b:
                print('You guessed!')
                break
            if a < b:
                print('Try less.')
            if a > b:
                print('Try more.')
    elif a > b:
        print('Try more.')
        while a != b:
            b = int(input(f'Введите новое число: '))
            if a == b:
                print('You guessed!')
                break
            if a < b:
                print('Try less.')
            if a > b:
                print('Try more.')
    elif a == b:
        print('You guessed!')
f(a, b)
