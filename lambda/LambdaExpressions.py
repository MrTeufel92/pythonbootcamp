# square = lambda num: num ** 2

# print(square(int(input("NUMB\n"))))

# map(lambda num: num + 2, x for x in input("numbs\n").split(','))
print(list(map(lambda num: num * 2, (int(x) for x in input("numbs\n").split(',')))))

