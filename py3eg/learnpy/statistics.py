import sys
import collections
import copy
import math

Statistics = collections.namedtuple("Statistics",
                                    "mean median mode std_dev")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h','--help'}:
        print('usage: {0} file1 [ file2 [ fileN ]]'.format(sys.argv[0]))
        sys.exit()

    numbers = []
    freq = collections.defaultdict(int)
    for filename in sys.argv[1:]:
        read_data(filename, numbers, freq)
    if numbers:
        statistics = calculate_statistics(numbers, freq)
        print_out(len(numbers), statistics)
    else:
        print('no numbers found')
        

def read_data(filename, numbers, freq):
    for lino, line in enumerate(open(filename, encoding = "ascii"),
                          start = 1):
        for x in line.split():
            try:
                number = float(x)
                numbers.append(number)
                freq[number] += 1
            except ValueError as err:
                print("{0}:{1}: skipping {2}: {3}".format(
                    filename, lino, x , err))


def calculate_statistics(numbers, freq):
    count = len(numbers)
    mean = sum(numbers)/len(numbers)
    median = calculate_median(numbers, count)
    mode = calculate_mode(freq)
    std_dev = calculate_std_dev(numbers, mean)
    return Statistics(mean, mode, median, std_dev)

def calculate_median(numbers, count):
    numbers.sort()
    median = numbers[count//2]
    if count % 2 == 0:
        median = (numbers[count//2 - 1] + numbers[count//2])/2
    return median

def calculate_mode(freq):
    highest_freq = max(freq.values())
    mode = [number for number, freque in freq.items()
            if math.fabs(freque - highest_freq) <= sys.float_info.epsilon]
    if not (1 <= len(mode) <= 3):
        mode = None
    else:
        mode.sort()
    return mode

def calculate_std_dev(numbers, mean):
    total = 0
    for number in numbers:
        total += ((number - mean) ** 2)
    variance = total / (len(numbers) - 1)
    return math.sqrt(variance)
    
def print_results(count, statistics):
    real = "9.2f"
    if statistics.mode is None:
        modeline = ""
    elif len(statistics.mode) == 1:
        modeline = "mode = {0:{fmt}}\n".format(
            statistics.mode[0], fmt=real)
    else:
        modeline = ("mode = [" +
                    ", ".join(["{0:.2f}".format(m)
                    for m in statistics.mode]) + "]\n")
    print("""\
    count = {0:6}
    mean = {1.mean:{fmt}}
    median = {1.median:{fmt}}
    {2}\
    std. dev. = {1.std_dev:{fmt}}""".format(
        count, statistics, modeline, fmt=real))

main()
