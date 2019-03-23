# Format the string with the .format() method

a = 'This is a test string'

b = 'example'

# print(a + ' {test}'.format(test=b))

floating_number = 120.3466545

# print('This is the original floating number: {number}'.format(number=floating_number))

# print('This is the formatted floating number: {number:1.3f}'.format(number=floating_number))

# Simple formatting

# print(f'This is an {b}')

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

# print(d['k1'][0]['nest_key'][1][0])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}

# print(d['k1'][2]['k2'][1]['tough'][2][0])

tup = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, s, y in tup:
    print(a)

tup_list = []
for a, b, c in tup:
    tup_list.append(a)
    tup_list.append(b)
    tup_list.append(c)

print(tup_list)

my_string = "hello world"

my_list = [letter for letter in my_string]

print(my_list)

my_list = [num for num in range(0, 11) if num % 2 == 0]

print(my_list)

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]

print(results)
