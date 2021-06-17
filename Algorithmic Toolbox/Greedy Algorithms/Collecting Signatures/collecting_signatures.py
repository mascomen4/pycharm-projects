# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

def intersection_of_two_lines(first_line, second_line):
    temp_list = [first_line, second_line]
    temp_list.sort()
    first_line = temp_list[0]
    second_line = temp_list[1]

    new_line = []
    if first_line[0] <= second_line[0] and first_line[1] >= second_line[0]:
        new_line.append(second_line[0])
        if first_line[1] >= second_line[1]:
            new_line.append(second_line[1])
        else:
            new_line.append(first_line[1])
    else:
        return []
        '''
        new_line.append(first_line[0])
        if first_line[1] < second_line[1]:
            new_line.append(first_line[1])
        else:
            new_line.append(second_line[1])
        '''
    return new_line

def compute_optimal_points(segments):
    # sort segments by left corne
    n = len(segments)
    points = []
    segments.sort()
    max_line = [segments[0][0], segments[0][1]]

    for i in range(1, n):
        current_line = [segments[i][0], segments[i][1]]
        previous_line = max_line
        max_line = intersection_of_two_lines(max_line, current_line)

        if not max_line:
            points.append(previous_line[len(previous_line)-1])
            max_line = current_line
            previous_line = {}



    """
    for i in range(n):
        if not max_line:
            max_line = set([i for i in range(segments[i][0], segments[i][1] + 1)])
            points.append(list(previous_line)[0])
            previous_line = current_line
        else:
            current_line = set([i for i in range(segments[i][0], segments[i][1] + 1)])
            previous_line = max_line
            max_line = current_line & max_line
    """
    if max_line:
        points.append(list(max_line)[len(max_line)-1])
    return points





if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
