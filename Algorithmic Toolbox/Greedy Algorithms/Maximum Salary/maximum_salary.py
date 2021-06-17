# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def max_number_by_digit_in_list(a):
    max_number = max(a)
    for number in a:
        str_number = str(number)
        str_max_number = str(max_number)
        if len(str_number) == len(str_max_number):
            max_number = max(max_number, number)
        else:
            min_length = min(len(str_number), len(str_max_number))
            for i in range(min_length):
                if int(str_number[i]) == int(str_max_number[i]):
                    pass
                elif int(str_number[i]) > int(str_max_number[i]):
                    max_number = number
                    break
                else:
                    max_number = max_number
                    break
    return max_number

def find_number_with_max_digit(numbers, position):
    max_numbers = []
    if position == 0:
        max_digit = 0
        for number in numbers:
            position_digit = int(str(number)[position])
            if position_digit > max_digit:
                max_digit = position_digit
        for number in numbers:
            position_digit = int(str(number)[position])
            if position_digit == max_digit:
                max_numbers.append(number)
    else:
        max_first_digit = 0
        max_digit = 0
        for number in numbers:
            first_digit = int(str(number)[0])
            if first_digit > max_first_digit:
                max_first_digit = first_digit
        for number in numbers:
            if len(str(number)) >= (position + 1):
                position_digit = int(str(number)[position])
            else:
                position_digit = 0
            if position_digit > max_digit:
                max_digit = position_digit
        for number in numbers:
            if len(str(number)) >= (position + 1):
                position_digit = int(str(number)[position])
            else:
                position_digit = 0
            if position_digit == max_digit and position_digit >= max_first_digit:
                max_numbers.append(number)

    return max_numbers

def largest_number(numbers):
    max_number = ''
    number = 0
    numbers = [int(number) for number in numbers]
    for i in range(len(numbers)):
        found_numbers1 = find_number_with_max_digit(numbers, 0)
        found_numbers2 = find_number_with_max_digit(found_numbers1, 1)
        if not found_numbers2:
            temp = []
            for found_number in found_numbers1:
                if found_number < 10:
                    temp.append(found_number)
            number = max(temp)
            numbers.remove(number)
            max_number += str(number)
            pass
        found_numbers3 = find_number_with_max_digit(found_numbers2, 2)
        if not found_numbers3:
            temp = []
            for found_number in found_numbers2:
                if found_number < 100:
                    temp.append(found_number)
            number = max(temp)
            numbers.remove(number)
            max_number += str(number)
            pass
    max_number = int(max_number)
    return max_number








if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
