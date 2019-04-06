from os import system, name
from time import sleep


def player_input():
    player1 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input("Player 1, choose X or O: ")

    player2 = 'O' if player1 == 'X' else 'X'
    return player1, player2


def print_board(board):
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


