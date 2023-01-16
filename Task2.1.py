# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

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
    candies = 2021
    while candies > 0:
        print(f'Player {player_number} takes candies: ', end='')
        move = check(28)
        candies -= move
        print(f'Candies remainder = {candies}')
        player_number = 3-player_number
        while 0 < candies < 28:
            print(f'Player {player_number} takes candies: ', end='')
            move = check(candies)
            candies -= move
            player_number = 3-player_number
            print(f'Candies remainder = {candies}')
    player_number = 3-player_number
    print()
    print(f'Player {player_number} WINS!!!')

def main():
    queue = random.randint(1, 2)
    print(f'Player {queue} starts the game')
    game(queue)

if __name__ == "__main__":
    main()
