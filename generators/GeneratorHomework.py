import random


# Create a generator that generates the squares of numbers up to some number N.
import sys


def gen_squares(n):
    for i in range(n):
        yield i ** 2


# for x in gen_squares(10):
#     print(x)


# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
def rand_num(low, high, n):
    while n > 0:
        yield random.randint(low, high)
        n -= 1


# for num in rand_num(1, 10, 12):
#     print(num)

# Use the iter() function to convert the string below into an iterator
s = 'hello'
s_iter = iter(s)


class Test:

    def __init__(self, number, word, letter):
        self.number = number
        self.word = word
        self.letter = letter
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while self.counter < len(self.word):
                letter = self.word[self.counter]
                self.counter += 1
                return letter
            else:
                raise StopIteration
        except IndexError:
            raise StopIteration


test_class = Test(8, 'SOMETHING', 'm')

# for c in test_class:
#     print(c)

print(sys.getsizeof((x ** 2 for x in range(0, 100))))
