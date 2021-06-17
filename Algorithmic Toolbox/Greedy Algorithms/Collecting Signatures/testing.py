def intersection_of_two_lines(first_line, second_line):
    print(first_line)
    print(second_line)
    new_line = []
    if first_line[0] < second_line[0]:
        new_line.append(second_line[0])
        if first_line[1] < second_line[1]:
            new_line.append(first_line[1])
        else:
            new_line.append(second_line[1])
    else:
        new_line.append(first_line[0])
        if first_line[1] < second_line[1]:
            new_line.append(first_line[1])
        else:
            new_line.append(second_line[1])
    return new_line

if __name__ == '__main__':
    first_list = list(map(int, input().split()))
    second_list = list(map(int, input().split()))
    print(intersection_of_two_lines(first_list, second_list))