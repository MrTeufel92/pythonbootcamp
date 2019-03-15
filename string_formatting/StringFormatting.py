# Format the string with the .format() method

a = 'This is a test string'

b = 'example'

print(a + ' {test}'.format(test=b))

floating_number = 120.3466545

print('This is the original floating number: {number}'.format(number=floating_number))

print('This is the formatted floating number: {number:1.3f}'.format(number=floating_number))
