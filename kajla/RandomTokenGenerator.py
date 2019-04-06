# -*- coding: utf-8 -*-
import os
from random import randint
from xlwt import Workbook
import sys

name = ''
number_of_tokens = 0
url = ''
writeToXls = False
writeToTxt = False

if len(sys.argv) == 4:
    name = str(sys.argv[1])
    number_of_tokens = int(sys.argv[2])
    url = str(sys.argv[3])
    toXls = input('Kiírjuk a kódokat xls fájlba? Kérjük, írd ide, hogy IGEN vagy NEM: ')
    while toXls != 'IGEN' and toXls != 'NEM':
        toXls = input('Kiírjuk a kódokat xls fájlba? Kérjük, írd ide, hogy IGEN vagy NEM: ')
    toTxt = input('Kiírjuk a kódokat txt fájlba? Kérjük, írd ide, hogy IGEN vagy NEM: ')
    while toTxt != 'NEM' and toTxt != 'IGEN':
        toTxt = input('Kiírjuk a kódokat txt fájlba? Kérjük, írd ide, hogy IGEN vagy NEM: ')
    writeToXls = False if toXls == 'NEM' else True
    writeToTxt = False if toTxt == 'NEM' else True
else:
    print('Kevés paramétert adtál meg!')
    print('Helyes megadási mód: python RandomTokenGenerator.py név generálandó_tokenek_száma xls_fájl_helye')
    sys.exit()


def generate_token(letters_param):
    token_arr = [None] * 12
    counter = len(letters_param)
    letter_index = 0

    for letter in letters_param:
        if counter != len(letters_param):
            letter_index = letter_index + 1
        random_integer = randint(letter_index, (len(token_arr) - counter))
        token_arr[random_integer] = letter
        letter_index = token_arr.index(letter)
        counter = counter - 1

    return token_arr


letters = []

for c in name:
    letters.append(c.upper())

token_set = set()
generating_counter = 10000

numb = 0
while numb < number_of_tokens:
    token = generate_token(letters)

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

    if len(token_set) % 10000 == 0:
        print("Generated " + str(generating_counter) + " tokens!")
        generating_counter = generating_counter + 10000

print('Generated ' + str(len(token_set)) + ' tokens at all!')

separate_character = ''
print(os.uname())

if writeToXls:
    print('Writing tokens to xls!')
    wb = Workbook(encoding='utf-8')
    count = 0
    xls_counter = 1
    sheet = wb.add_sheet(str(xls_counter) + ' millió token', cell_overwrite_ok=True)
    for line in token_set:
        sheet.write(count, 0, line)
        count = count + 1
        if count % 10000 == 0:
            wb.save(url + '/tokens' + str(xls_counter) + '.xls')
            print('Saved to: ' + url + '/tokens' + str(xls_counter) + '.xls')
            xls_counter = xls_counter + 1
            count = 0


if writeToTxt:
    with open('tokens.txt', 'w') as f:
        print('Writing tokens to tokens.txt!')
        for line in token_set:
            f.write(line)
            f.write('\n')

    tokens = []
    with open('tokens.txt', 'r') as r:
        tokens.append(r.readline())

    error_Counter = 0
    for line in tokens:
        for inner in token_set:
            if line == inner:
                error_Counter += 1
                print('ERROR')

    if error_Counter == 0:
        print('EVERYTHING IS FINE')
    else:
        print('SOMETHING IS WRONG')
