def read_matrix_and_const():
    try:
        n, m = input().split()
        n, m = int(n), int(m)
    except:
        print("Looks like you've entered more than 2 numbers or you've entered non integer values ...")

    matrix = []

    try:
        for i in range(n):
            row = [int(val) for val in input().split()]
            matrix.append(row)
        assert len(matrix) == n and [len(matrix[i]) == m for i in range(n)]
    except:
        print("Looks like you've input the matrix that is inconsistent with your n, m ...")

    try:
        const = int(input())
    except:
        print("Looks like you've entered more than 2 numbers or you've entered non integer values ...")

    return matrix, n, m, const


def matrix_mult_const(const, matrix, n, m):
    for i in range(n):
        for j in range(m):
            matrix[i][j] *= const

    return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print("")


def main():
    matrix1, n1, m1, const = read_matrix_and_const()
    mult_matrix = matrix_mult_const(const, matrix1, n1, m1)
    print_matrix(mult_matrix)


main()

