# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    a = [0, 1]
    if n <= 1:
        return a[n]

    for i in range(2, n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
