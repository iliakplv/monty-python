matrix_a = [[1, 2, 3],
            [4, 5, 6]]

matrix_b = [[7, 8],
            [9, 10],
            [11, 12]]


def check_dimensions(matrix1, matrix2):
    if not (check_rows_length(matrix1) and check_rows_length(matrix2)):
        return False

    matrix1lines = len(matrix1)
    matrix1rows = len(matrix1[0])
    matrix2lines = len(matrix2)
    matrix2rows = len(matrix2[0])

    return matrix1lines == matrix2rows and matrix1rows == matrix2lines


def check_rows_length(matrix):
    first_row_length = len(matrix[0])
    for line in matrix:
        if not len(line) == first_row_length:
            return False
    return True


def multiply(matrix1, matrix2):
    if not check_dimensions(matrix1, matrix2):
        return [['dimension_error']]

    matrix1lines = len(matrix1)
    matrix1rows = len(matrix1[0])
    matrix2rows = len(matrix2[0])

    result = []
    for line in range(matrix1lines):
        result_line = []
        for row in range(matrix2rows):
            cross_sum = 0
            for sum_index in range(matrix1rows):
                cross_sum += matrix1[line][sum_index] * matrix2[sum_index][row]
            result_line.append(cross_sum)
        result.append(result_line)

    return result


def print_result(result):
    for line in result:
        print(*line, sep='\t')


# Tests

print_result(multiply(matrix_a, matrix_b))
