# python3

def check_split(number, k):
    # Check if exist the splitting and return it if exists
    temp = number
    last_number = 1 + (k-2)*1
    arithmetic_sum = ((1 + last_number)/2)*(k-1)
    rest = number - int(arithmetic_sum)

    if rest >= k:
        #splitting = [i for i in range(1, k)]
        #splitting.append(rest)
        return True
    else:
        return False


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    # Find the max k for which it works
    i = 1
    while check_split(n,i):
        i += 1
    i -= 1

    # Construct the list for which it works
    last_number = 1 + (i-2)*1
    arithmetic_sum = ((1 + last_number)/2)*(i-1)
    rest = n - int(arithmetic_sum)

    summands = [i for i in range(1, i)]
    summands.append(rest)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
