tokens = []


def read_tokens():
    tokens_2 = []
    with open('albumkodok_52500.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tokens_2.append(line[:14:])
    with open('utlevelkodok_450000.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tokens_2.append(line[:14:])
    with open('utlevelkodok_v2_130000.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tokens_2.append(line[:14:])

    return tokens_2


with open('sok_gyerek_boldogsagaert_410000.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        tokens.append(line)

print(len(tokens))
print(len(set(tokens)))

strings = []
for line in tokens:
    temp = []
    formatted = line[:14:]
    for c in formatted:
        if c in ['K', 'A', 'J', 'L', 'A']:
            temp.append(c)
    strings.append(temp)

for arr in strings:
    if ''.join(s for s in arr) != 'KAJLA':
        print('Error')

old_tokens = read_tokens()
new_tokens = tokens


old_counter = 0
new_counter = 0
found_wrong_token_counter = 0

# for old_token in old_tokens:
#     old_counter += 1
#     for new_token in new_tokens:
#         new_counter += 1
#         if old_token == new_token:
#             found_wrong_token_counter += 1
#             print(f'{old_token} is equal to {new_token}. '
#                   f'Old token counter: {old_counter}, new token counter: {new_counter}')

number = 0

for new_token in new_tokens:
    number += 1
    if old_tokens.__contains__(new_token):
        print('Error')
    elif number % 1000 == 0:
        print(f'Checked {number} number of tokens.')

print(f'Found {found_wrong_token_counter} wrong tokens.')
