# -*- coding: utf-8 -*-
import os
from random import randint
from xlwt import Workbook
import sys

name = ''
number_of_tokens = 0
url = ''
writeToTxt = False

if len(sys.argv) == 4:
    name = str(sys.argv[1])
    number_of_tokens = int(sys.argv[2])
    url = str(sys.argv[3])
    toTxt = input('Kiírjuk a kódokat txt fájlba? Kérjük, írd ide, hogy IGEN vagy NEM: ')
    while toTxt != 'NEM' and toTxt != 'IGEN':
        toTxt = input('Kiírjuk a kódokat txt fájlba? Kérjük, írd ide, hogy IGEN vagy NEM: ')
    writeToTxt = False if toTxt == 'NEM' else True
else:
    print('Kevés paramétert adtál meg!')
    print('Helyes megadási mód: python RandomTokenGenerator.py név generálandó_tokenek_száma xls_fájl_helye')
    sys.exit()


class TokenGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_token(letters_param):
        token_arr = [None] * 14
        counter = len(letters_param)
        letter_index = 0
        number = 4

        for letter in letters_param:
            if counter != len(letters_param):
                letter_index = letter_index + 1
            random_integer = randint(letter_index, (len(token_arr) - counter) - number)
            token_arr[random_integer] = letter
            letter_index = token_arr.index(letter)
            counter -= 1
            number -= 1

        return token_arr


letters = [c.upper() for c in name]

token_set = set()
generating_counter = 100000

numb = 0
while numb < number_of_tokens:
    token = TokenGenerator.generate_token(letters)

    for i in range(len(token)):
        if token[i] is None:
            token[i] = randint(0, 9)

    tokenStr = ''
    for char in token:
        tokenStr += str(char)

    if tokenStr not in token_set:
        token_set.add(tokenStr)
        numb = numb + 1
    else:
        print('Token string is already in the set: ' + tokenStr)

    if len(token_set) % 100000 == 0:
        print("Generated " + str(generating_counter) + " tokens!")
        generating_counter = generating_counter + 100000

print('Generated ' + str(len(token_set)) + ' tokens at all!')

fifty_thousand = set()
one_and_a_half_million = set()

for idx, line in enumerate(token_set):
    if idx < 52500:
        fifty_thousand.add(line)
    else:
        one_and_a_half_million.add(line)

if writeToTxt:
    print('Writing tokens to txt!')
    with open('C:\\PycharmProjects\\first_tokens.txt', 'w') as f:
        for line in fifty_thousand:
            f.write(line)
            f.write('\n')
    with open('C:\\PycharmProjects\\second_tokens.txt', 'w') as f:
        for line in one_and_a_half_million:
            f.write(line)
            f.write('\n')
    #
    # tokens = set()
    # with open('C:\\PycharmProjects\\first_tokens.txt', 'r') as r:
    #     for i in range(1, numb + 1):
    #         tokens.add(r.readline()[:14:])
    #
    # print('EVERYTHING IS FINE'
    #       if len(tokens) == (numb - 1575000) and len(tokens) == len(fifty_thousand)
    #       else 'SOMETHING WENT WRONG')
    #
    # tokens.clear()
    # with open('C:\\PycharmProjects\\second_tokens.txt', 'r') as r:
    #     for i in range(1, numb + 1):
    #         tokens.add(r.readline()[:14:])
    #
    # print('EVERYTHING IS FINE'
    #       if len(tokens) == (numb - 52500) and len(tokens) == len(one_and_a_half_million)
    #       else 'SOMETHING WENT WRONG')
