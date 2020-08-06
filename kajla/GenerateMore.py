import sys
from random import randint


def generate_tokens(letters):
    number = 0
    already_in_use_number = 0

    tokens = read_tokens()

    print(f'Token list length is: {len(tokens)}')

    token_set = set()

    while number < 410_000:
        token = generate_token(letters)

        for i in range(len(token)):
            if token[i] is None:
                token[i] = randint(0, 9)

        token_str = ''
        for char in token:
            token_str += str(char)

        if token_str not in token_set and token_str not in tokens:
            token_set.add(token_str)
            number += 1
            if len(token_set) % 10000 == 0:
                print(f'Generated {number} tokens!')
        else:
            already_in_use_number += 1
            if already_in_use_number % 10000 == 0:
                print(f'Generated {already_in_use_number} tokens that are already in use.')

    with open('sok_gyerek_boldogsagaert_410000.txt', 'w') as f:
        for token in token_set:
            f.write(token)
            f.write('\n')

    sys.exit(1)


def read_tokens():
    tokens = []
    with open('albumkodok_52500.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tokens.append(line[:14:])
    with open('utlevelkodok_450000.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tokens.append(line[:14:])
    with open('utlevelkodok_v2_130000.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tokens.append(line[:14:])

    return tokens


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


if __name__ == '__main__':
    generate_tokens('KAJLA')

