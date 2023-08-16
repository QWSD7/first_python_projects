#Заголовок программы
from random import *

# Функция проверки корректности введенных данных
def is_valid(number):
    if number.isdigit():
        if 1 <= int(number) <= 100:
            return 0
        else:
            return 1
    else:
        return 2

def input_num(): # ввод данных
    while True:
        number = input()
        Response = is_valid(number)

        if Response == 2:
            print('А может быть все-таки введем целое число от 1 до 100?')
        elif Response == 1:
            print('Вы вышли за пределы диапазона от 1 до 100')
        else:
            return  int(number)

def compare_num(down_num, up_num): # Сравнение введенного значения с загаданным
    num = randint(down_num, up_num)
    total = 0
    while True:
        n = input_num()
        total += 1
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Победа!!! Вы угадали ответ за', total,  'попыток, поздравляем!' )
            break

def continue_game(): # Предложение продолжить игру
    ans = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
        elif ans in ('n', 'н'):
            print('До новых встреч!!!')
            return False
        else:
            return True


def game():  # Запуск игры
    print("Добро пожаловать в числовую угадайку!")
    while True:
        print('Укажите, в каком диапазоне Вы готовы угадывать числа\n(В пределах от 1 до 100):\n')
        x, y = input_num(), input_num()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y, '\n')
        compare_num(x, y)
        if continue_game():
            continue
        else:
            break

game() #запуск игры
