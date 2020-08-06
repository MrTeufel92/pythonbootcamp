from os import name, system

for i in ['a', 'b', 2]:
    try:
        print(i ** 2)
    except TypeError:
        print('There is a letter in the list instead of a number!')


x = 5
y = 0

try:
    print(x / y)
except ZeroDivisionError:
    print('Y is zero.')
finally:
    print('ALL DONE')


def clear_board():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def ask():
    while True:
        try:
            number = int(input('Please enter a number: '))
            print(f'Thank you, your number squared is: {number ** 2}')
            break
        except ValueError:
            clear_board()
            print('You did not enter a number, please try again!')


ask()
