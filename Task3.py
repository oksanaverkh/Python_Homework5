# Создайте программу для игры в ""Крестики-нолики"".

import os
import random
os.system('cls')

def check_coordinates():
    x, y = int(input()), int(input())
    while not 1 <= x <= 3 or not 1 <= y <= 3:
        print('Wrong number, try again')
        x, y = int(input()), int(input())
    return int(x), int(y)

def get_empty_table():
    empty_table = [['x/y   1    2    3'],
                    ['  1 ', ' _ |', ' _ |', ' _ '], 
                    ['  2 ', ' _ |', ' _ |', ' _ '], 
                    ['  3 ', ' _ |', ' _ |', ' _ ']]
    for i in range(0, len(empty_table)):
        for j in range(0, len(empty_table[i])):
            print(empty_table[i][j], end=' ')
        print()
    return empty_table

def game():
    player_number = 1
    x_list, y_list = [], []
    count = 1
    game_table = get_empty_table()
    while count<=9:
        print(f'Player {player_number} enters coordinates (x, y): ', end='')
        x, y = check_coordinates()        
        x_list.append(x)
        y_list.append(y)
        move = (x,y,)
        if count>=2:
            for i in range(len(coord_list)):
                while coord_list[i] == move:
                    print('Coordinates are already used, enter again')
                    x, y = check_coordinates()
                    move = (x,y,)
        for i in range(0, len(game_table)):
            for j in range(0, len(game_table[i])):
                if i==x and j==y:
                    if player_number==1:
                        game_table[i][j] = ' X  '
                    else:
                        game_table[i][j] = ' 0  '
                print(game_table[i][j], end=' ')
            print()
        coord_list = list(zip(x_list, y_list))
        count+=1
        player_number = 3-player_number

    game_table = game_table[1:4]
    del game_table[0][0]
    del game_table[1][0]  
    del game_table[2][0]  
    return game_table

game_table = [[' _ |', ' _ |', ' _ '], 
                [' _ |', ' _ |', ' _ '], 
                [' _ |', ' _ |', ' _ ']]        
def victory_check(game_table):
    result = 0
    for i in range(len(game_table)):
        if game_table[i][0]==game_table[i][1]==game_table[i][2]:
            if game_table[i][0]==' X  ':
                result = 'Player 1 WINS!!!'
            else:
                result = 'Player 2 WINS!!!'
            break    
    for j in range(len(game_table)):
        if game_table[0][j]==game_table[1][j]==game_table[2][j]:
            if game_table[0][j]==' X  ':
                result = 'Player 1 WINS!!!'
            else:
                result = 'Player 2 WINS!!!'
            break
    if game_table[0][0]==game_table[1][1]==game_table[2][2]:
        if game_table[0][0]==' X  ':
            result = 'Player 1 WINS!!!'
        else:
            result = 'Player 2 WINS!!!'
    elif game_table[2][0]==game_table[1][1]==game_table[0][2]:
        if game_table[1][1]==' X  ':
            result = 'Player 1 WINS!!!'
        else:
            result = 'Player 2 WINS!!!'
    else:
        result = 'Dead heat'

    return result
        
def main():
    print('Player 1 starts the game')
    print()
    table_game = game()
    print(victory_check(table_game))

if __name__ == "__main__":
    main()

