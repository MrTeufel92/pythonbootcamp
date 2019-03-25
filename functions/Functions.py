
def my_func(my_string):
    switcher = True
    result = ''
    for char in my_string:
        if switcher:
            result += char.upper()
        else:
            result += char.lower()
        switcher = not switcher
    return result


print(my_func('Carwasher'))
