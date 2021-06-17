# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    n = len(stops)
    number_of_stops = 0
    current = 0
    stops.append(d)
    stops.insert(0, 0)
    while current <= n:
        last = current
        while (current <= n) and (stops[current+1] - stops[last] <= m):
            current += 1
        if current == last:
            return -1
        if current <= n:
            number_of_stops += 1

    return number_of_stops





if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
