# Создайте программу для игры в ""Крестики-нолики"".


import os
import random
os.system('cls')

def check_coordinates():
    x, y = int(input()), int(input())
    while not 0 <= x <= 2 or not 0 <= y <= 2:
        print('Wrong number, try again')
        x, y = int(input()), int(input())
    return int(x), int(y)

def get_empty_table():
    print('x/y  0   1   2')
    game_table = []

    for i in range (3):
        for j in range(4):
            if j==0:
                # print(f'  {i} ', end='')
                el = f'  {i} '
                game_table.append(el)
            elif 0<j<3:
                # print(' _ |', end='')
                game_table.append(' _ |')
            else:
                # print(' _ ', end='')
                game_table.append(' _ ')
        print(*game_table)
    print()
    # print(game_table)

def get_game_table(player_number):
    print('x/y  0   1   2')
    x_list, y_list = [], []
    # game_table = []
    print(f'Player {player_number} enters coordinates (x, y): ')

    for x in range(3):
        for y in range(4):
            x, y = check_coordinates()
            x_list.append(x)
            y_list.append(y)
            coord_list = list(zip(x_list, y_list))
            move = (x,y,)
            if y==0:
                print(f'  {x} ', end='')
            elif 0<y<3:
                print(f' {x} |', end='')
            else:
                print(' _ ', end='')

        for i in range(len(coord_list)):
            while coord_list[i] == move:
                print('Coordinates are already used, enter again')
            print()

# def victory_check()



# def game(player_number):
#     candies = 2021
#     while candies > 0:
#         print(f'Player {player_number} takes candies: ', end='')
#         move = check(28)
#         candies -= move
#         print(f'Candies remainder = {candies}')
#         player_number = 3-player_number
#         while 0 < candies < 28:
#             print(f'Player {player_number} takes candies: ', end='')
#             move = check(candies)
#             candies -= move
#             player_number = 3-player_number
#             print(f'Candies remainder = {candies}')
#     player_number = 3-player_number
#     print()
#     print(f'Player {player_number} WINS!!!')

def main():
    queue = random.randint(1, 2)
    print(f'Player {queue} starts the game')
    get_empty_table()
    # get_game_table(queue)

    # game(queue)

if __name__ == "__main__":
    main()