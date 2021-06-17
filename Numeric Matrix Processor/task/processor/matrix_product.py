import math
import numpy as np


def print_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")


def read_choice():
    choice = int(input("Your choice: "))
    return choice


def read_const():
    const = input("Enter constant: ")
    try:
        const = int(const)
    except ValueError:
        const = float(const)
    return const


def read_matrix(msg1="Enter size of matrix: ", msg2="Enter matrix: "):
    try:
        m, n = input(msg1).split()
        m, n = int(m), int(n)
    except ValueError:
        print("Looks like you've entered more than 2 numbers or you've entered non integer values ...")
        return 1
    matrix = []

    print(msg2)
    try:
        for i in range(m):
            row = [val for val in input().split()]
            try:
                row = [int(val) for val in row]
            except ValueError:
                row = [float(val) for val in row]
            matrix.append(row)
        assert len(matrix) == m and [len(matrix[i]) == n for i in range(m)]
    except ValueError:
        print("Looks like you've input the matrix that is inconsistent with your n, m ...")

    return matrix, m, n


def read2matrices():
    msg1 = "Enter size of {} matrix: "
    msg2 = "Enter {} matrix: "
    return read_matrix(msg1=msg1.format("first"), msg2=msg2.format("first")), read_matrix(msg1=msg1.format("second"),
                                                                                          msg2=msg2.format("second"))


def print_matrix(matrix, m, n):
    for i in range(m):
        row = []
        for j in range(n):
            row.append(str(matrix[i][j]))
        string = " ".join(row)
        print(string)
    print("")


def matrix_mult_by_const(matrix=None, m=None, n=None, const=None):
    if matrix is None and const is None:
        matrix, m, n = read_matrix()
        const = read_const()

    for i in range(m):
        for j in range(n):
            try:
                matrix[i][j] *= const
                if str(type(matrix[i][j])) == "<class 'float'>":
                    if matrix[i][j] > 0:
                        matrix[i][j] = float(str(matrix[i][j])[:4])
                    elif matrix[i][j] < 0:
                        matrix[i][j] = float(str(matrix[i][j])[:5])
                    else:
                        matrix[i][j] = 0
            except:
                matrix[i][j] = float(matrix[i][j])
                matrix[i][j] *= const
                # truncating
                matrix[i][j] = float(str(matrix[i][j])[:4])
    return matrix, m, n


def matrix_sum():
    pack1, pack2 = read2matrices()
    matrix1, m1, n1 = pack1
    matrix2, m2, n2 = pack2
    if n1 == n2 and m1 == m2:
        summed_matrix = []
        for i in range(m1):
            row = []
            for j in range(n1):
                row.append(matrix1[i][j] + matrix2[i][j])
            summed_matrix.append(row)
        return summed_matrix, m1, n1
    else:
        return print("ERROR")


def matrix_product():
    pack1, pack2 = read2matrices()
    matrix1, m1, n1 = pack1
    matrix2, m2, n2 = pack2

    if n1 == m2:
        # Fill in the matrix with 0. The result matrix should be [m1 x n2] dimensions
        r_matrix = [[0 for _ in range(n2)] for _ in range(m1)]
        for result_col in range(n2):
            for row in range(m1):
                el = 0
                for column in range(n1):
                    el += matrix1[row][column]*matrix2[column][result_col]
                r_matrix[row][result_col] = el

        return r_matrix, m1, n2
    else:
        return print("ERROR")

### TRANSPOSING SECTION ###


def matrix_transpose_main_diagonal(matrix=None):
    if matrix is None:
        matrix, m, n = read_matrix()
    else:
        m = len(matrix)
        n = len(matrix[0])
    if m == n:
        for row in range(m):
            for column in range(n):
                if row == column:
                    break
                else:
                    matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
    else:
        new_matrix = []
        for col in range(n):
            column_ = []
            for row in range(m):
                column_.append(matrix[row][col])
            new_matrix.append(column_)
        matrix = new_matrix
        m, n = n, m
    return matrix, m, n


def matrix_transpose_side_diagonal(matrix=None):
    # Perform it using transposing along the vertical line
    if matrix is None:
        matrix, m, n = read_matrix()
    else:
        m = len(matrix)
        n = len(matrix[0])
    matrix, _, _ = matrix_transpose_vertical_line(matrix)
    matrix, _, _ = matrix_transpose_main_diagonal(matrix)
    matrix, _, _ = matrix_transpose_vertical_line(matrix)
    return matrix, m, n


def matrix_transpose_vertical_line(matrix=None):
    if matrix is None:
        matrix, m, n = read_matrix()
    else:
        m = len(matrix)
        n = len(matrix[0])
    # Now m - is the number or columns, n - number of rows
    matrix, _, _ = matrix_transpose_main_diagonal(matrix)
    matrix, _, _ = matrix_transpose_horizontal_line(matrix)
    # Now the dimensions are back to the initial state
    matrix, _, _ = matrix_transpose_main_diagonal(matrix)
    return matrix, m, n


def matrix_transpose_horizontal_line(matrix=None):
    # Let's define 2 states of the function. When it has to read the matrix by itself, and when it
    # has to transpose the given matrix
    if matrix is None:
        matrix, m, n = read_matrix()
    else:
        m = len(matrix)
        n = len(matrix[0])
    matrix = matrix[::-1]
    return matrix, m, n


def print_transpose_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")


def matrix_transpose_perform_choice(choice):
    if choice == 1:
        # Main diagonal
        matrix, m, n = matrix_transpose_main_diagonal()
    elif choice == 2:
        matrix, m, n = matrix_transpose_side_diagonal()
    elif choice == 3:
        matrix, m, n = matrix_transpose_vertical_line()
    elif choice == 4:
        matrix, m, n = matrix_transpose_horizontal_line()
    return matrix, m, n


def matrix_transpose():
    print_transpose_menu()
    choice = read_choice()
    matrix = matrix_transpose_perform_choice(choice)
    return matrix

### THE END OF THE MATRIX TRANSPOSE SECTION ###
### START OF THE DETERMINANT SECTION ###


def cofactor(i, j, val=None):
    if val is None:
        return (-1)**(i+j)
    else:
        return (-1)**(i+j)*val


def minor(matrix, i, j):
    matrix.pop(i)
    matrix, _, _ = matrix_transpose_main_diagonal(matrix)
    matrix.pop(j)
    matrix, _, _ = matrix_transpose_main_diagonal(matrix)
    return matrix


def calc_determinant(matrix=None):
    if matrix is None:
        matrix, m, n = read_matrix()
    # Base case of the recursion dim(matrix) = 1
    if len(matrix) == 1:
        # Not sure about the following
        return matrix[0][0]
    # Base case of the recursion dim(matrix) = 2
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det = 0
        for j, value in enumerate(matrix[0]):
            det += calc_determinant(minor(matrix.copy(), 0, j)) * cofactor(1, j + 1) * value
    return det

### THE END OF THE DETERMINANT SECTION ###
### START OF THE INVERSE MATRIX SECTION ###


def cofactors_matrix(matrix):
    if str(type(matrix)) in {"<class 'list'>"}:
        cofs = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                row.append(cofactor(i, j, calc_determinant(minor(matrix.copy(), i, j))))
            cofs.append(row)
        return cofs
    else:
        return "Sorry, looks like you've entered not the Python list"


def inverse_matrix(matrix=None):
    if matrix is None:
        matrix, m, n = read_matrix()

    m, n = len(matrix), len(matrix[0])
    det = calc_determinant(matrix)
    matrix_t, _, _ = matrix_transpose_main_diagonal(matrix.copy())
    cofs_t = cofactors_matrix(matrix_t)
    if det != 0:
        return matrix_mult_by_const(matrix=cofs_t, m=m, n=n, const=1/det)
    else:
        return "This matrix doesn't have an inverse."


### START OF THE MAIN FUNCTION SECTION ###
# TODO: Change the print_matrix function so that the matrix becomes readable


def perform_choice(choice):
    if choice == 1:
        summed_matrix, m, n = matrix_sum()
        print("The result is: ")
        print_matrix(summed_matrix, m, n)
        return True
    elif choice == 2:
        multed_matrix, m, n = matrix_mult_by_const()
        print("The result is: ")
        print_matrix(multed_matrix, m, n)
        return True
    elif choice == 3:
        try:
            p_matrix, m, n = matrix_product()
            print("The result is: ")
            print_matrix(p_matrix, m, n)
        except TypeError:
            pass
        return True
    elif choice == 4:
        tmatrix, m, n = matrix_transpose()
        print("The result is: ")
        print_matrix(tmatrix, m, n)
        return True
    elif choice == 5:
        determinant = calc_determinant()
        print("The result is: ")
        print(determinant)
        return True
    elif choice == 6:
        res = inverse_matrix()
        if str(type(res)) == "<class 'str'>":
            print("This matrix doesn't have an inverse.")
        else:
            matrix, m, n = res
            print("The result is: ")
            print_matrix(matrix, m, n)
        return True
    elif choice == 0:
        return False


def main():
    while True:
        print_menu()
        choice = read_choice()
        # I'm performing the choice and also taking the return. If the choice is 0, I break the loop
        flag = perform_choice(choice)
        if not flag:
            break


main()
