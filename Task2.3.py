# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
import random
os.system('cls')


def check(border):
    quantity = int(input())
    while not 1 <= quantity <= border:
        print('Wrong number, try again')
        quantity = int(input())
    return int(quantity)

def game(player_number):
    candies, initial_candies = 2021, 2021
    
    # 1st move:
    if player_number == 2:
        move = candies % 29
        print(f'Computer takes candies: {move}')
        candies -= move
        print(f'Candies remainder = {candies}')
        player_number = 3-player_number

    if player_number == 1:
        print(f'Player {player_number} takes candies: ', end='')
        move = check(min(28, candies))
        candies -= move
        print(f'Candies remainder = {candies}')
        player_number = 3-player_number

        if move < initial_candies % 29:
            move = initial_candies % 29-move
            print(f'Computer takes candies: {move}')
            candies -= move
            print(f'Candies remainder = {candies}')
        if move >= initial_candies % 29:
            move = (initial_candies % 29+29)-move
            print(f'Computer takes candies: {move}')
            candies -= move
            print(f'Candies remainder = {candies}')
    player_number = 3-player_number

    # following moves:
    while candies > 0:
        if player_number == 1:
            print(f'Player {player_number} takes candies: ', end='')
            move = check(min(28, candies))
            candies -= move
            print(f'Candies remainder = {candies}')
            player_number = 3-player_number

        if candies >= 1:
            if 28 < candies <= 29*2:
                move = candies-29
                print(f'Computer takes candies: {move}')
                candies -= move
                print(f'Candies remainder = {candies}')
            if candies > 29*2:
                move = 29-move
                print(f'Computer takes candies: {move}')
                candies -= move
                print(f'Candies remainder = {candies}')
            if 1<=candies<=28:
                move = candies
                print(f'Computer takes candies: {move}')
                candies -= move
                print(f'Candies remainder = {candies}')
            player_number = 3-player_number

    player_number = 3-player_number
    print()
    if player_number == 1:
        print(f'Player {player_number} WINS!!!')
    else:
        print('Computer WINS!!!')

def main():
    queue = random.randint(1, 2)
    if queue == 1:
        print(f'Player {queue} starts the game')
    else:
        print('Computer starts the game')
    game(queue)


if __name__ == "__main__":
    main()
