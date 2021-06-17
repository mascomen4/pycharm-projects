# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    a = [0, 1]
    example = [0, 1]
    if n <= 1:
        return a[n]

    a.append((a[0]+a[1]) % m)
    i = 2
    while [a[i-1], a[i]] != example:
        a.append((a[i] + a[i-1]) % m)
        i += 1

    return a[n % (len(a)-2)]



if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
