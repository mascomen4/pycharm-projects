# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    n = len(weights)
    array_weights = [0]*n
    value = 0
    for i in range(n):
        if capacity == 0:
            return value, array_weights
        max_temp_value = 0
        max_index = 0
        for j in range(n):
            if weights[j] != 0:
                if prices[j]/weights[j] > max_temp_value:
                    max_temp_value = prices[j]/weights[j]
                    max_index = j
        a = min(weights[max_index], capacity)
        value = value + a*max_temp_value
        weights[max_index] = weights[max_index] - a
        array_weights[max_index] = array_weights[max_index] + a
        capacity = capacity - a
    return value, array_weights


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print(opt_value[0])
    print(opt_value[1])
    print("{:.10f}".format(opt_value))
