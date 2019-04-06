# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd


def lesser_of_two_evens(num1, num2):
    return min(num1, num2) if (num1 % 2 == 0 and num2 % 2 == 0) else max(num1, num2)


print(lesser_of_two_evens(4, 6))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter


def animal_crackers(name):
    words = name.lower().split()
    return words[0][0] == words[1][0]


print(animal_crackers("Animal Alloo"))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If
# not, return False


def makes_twenty(num1, num2):
    return num1 + num2 == 20 or num1 == 20 or num2 == 20


print(makes_twenty(10, 20))


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name


def old_macdonald(name):
    # return name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return name[:3].capitalize() + name[3:].capitalize()


print(old_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed


def master_yoda(sentence):
    return ' '.join(sentence.split()[::-1])


print(master_yoda('We are ready'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(n):
    # return n in range(90, 111) or n in range(190, 211)
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


print(almost_there(190))


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.


def has_33(nums):
    # previous_num = 0
    # for num in nums:
    #     if num == 3 and previous_num == 3:
    #         return True
    #     else:
    #         previous_num = num
    # return False
    for idx, num in enumerate(nums):
        if nums[idx] == 3 and nums[idx + 1] == 3:
            return True
    return False


print(has_33([3, 1, 3, 3, 1]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters


def paper_doll(text):
    return ''.join(x * 3 for x in text)


print(paper_doll('Hello'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If
# their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment)
# exceeds 21, return 'BUST'


def blackjack(num1, num2, num3):
    sum_of_nums = sum([num1, num2, num3])
    if sum_of_nums <= 21:
        return sum_of_nums
    if sum_of_nums > 21 and 11 in [num1, num2, num3]:
        sum_of_nums -= 10
    if sum_of_nums > 21:
        return 'BUST'
    return sum_of_nums


print(blackjack(5, 11, 7))


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.


def summer_69(nums):
    need_the_number = True
    nums_to_sum = []
    for num in nums:
        if num == 6:
            need_the_number = False
        if need_the_number:
            nums_to_sum.append(num)
        if num == 9:
            need_the_number = True

    return sum(nums_to_sum)


print(summer_69([2, 1, 6, 9, 11]))


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order


def spy_game(nums):
    return '007' in ''.join([str(x) for x in nums if x == 0 or x == 7])


print(spy_game([1, 2, 4, 0, 0, 7, 5]))


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number


def count_primes(number):
    counter = 0
    for outer in range(1, number + 1):
        divisible_nums = []
        for inner in range(1, number + 1):
            if outer % inner == 0:
                divisible_nums.append(inner)
        if len(divisible_nums) == 2 and all(element in [1, outer] for element in divisible_nums):
            counter += 1
    return counter


print(count_primes(0))


