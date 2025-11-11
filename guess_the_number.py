import random

def greeting():
    print('Добро пожаловать в угадайку')

def is_valid(n):
    if 1 <= n <= 100:
        return True
    else:
        return False

def is_valid_num(ur_number):
    while True:
        if is_valid(ur_number):
            return int(ur_number)
        else:
            print("Может все таки введем число от 1 до 100?")

def game(n, goal):
    counter = 0
    while True:
        if is_valid_num(n) > goal:
            print('Ваше число больше загаданного, попробуйте еще разок')
            n = int(input())
            counter += 1

        elif is_valid_num(n) < goal:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            n = int(input())
            counter += 1

        elif is_valid_num(n) == goal:
            print('Вы угадали, поздравляем!')
            print(f'Ваше число попыток: {counter}')
            break

greeting()

while True:
    game(int(input('Угадайте число: ')), random.randint(1,100))
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    retry = input('Хотите сыграть еще раз? ')
    if retry == 'Нет':
        break

