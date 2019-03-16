from random import randint
from xlwt import Workbook
import sys

name = ''
number_of_tokens = 0
url = ''

if len(sys.argv) == 4:
    name = str(sys.argv[1])
    number_of_tokens = int(sys.argv[2])
    url = str(sys.argv[3])
else:
    print('Kevés paramétert adtál meg!')
    print('Helyes megadási mód: python RandomTokenGenerator.py név generálandó_tokenek_száma xls_fájl_helye')
    sys.exit()


def generate_token(letters_param):
    token_arr = [None] * 16
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
generating_counter = 100

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

    if len(token_set) % 100 == 0:
        print("Generated " + str(generating_counter) + " tokens!")
        generating_counter = generating_counter + 100000

print('Generated ' + str(len(token_set)) + ' tokens at all!')

wb = Workbook()

count = 0
xls_counter = 1
sheet = wb.add_sheet(str(xls_counter) + ' millió token', cell_overwrite_ok=True)
for line in token_set:
    sheet.write(count, 0, line)
    count = count + 1
    if count % 100 == 0:
        wb.save(url + '\\tokens' + str(xls_counter) + '.xls')
        xls_counter = xls_counter + 1
        count = 0
