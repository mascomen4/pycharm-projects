# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert n >= 0
    assert n <= 10**18
    cycle_string = '011235831459437077415617853819099875279651673033695493257291'
    cycle = [int(number) for number in cycle_string]
    sum_cycle = sum(cycle)
    number_of_cycles = n // 60
    remainder_of_cycle = n % 60
    number = sum_cycle*number_of_cycles + sum(cycle[:remainder_of_cycle+1])
    return number % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    answer = 10 + last_digit_of_the_sum_of_fibonacci_numbers(to_index) - last_digit_of_the_sum_of_fibonacci_numbers(from_index-1)
    return answer % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))

