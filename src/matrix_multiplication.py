matrix_a = [[1, 2, 3],
            [4, 5, 6]]

matrix_b = [[7, 8],
            [9, 10],
            [11, 12]]


def multiply(matrix1, matrix2):
    matrix1rows = len(matrix1)
    matrix1cols = len(matrix1[0])
    matrix2cols = len(matrix2[0])

    result = []
    for row in range(matrix1rows):
        result_line = []
        for col in range(matrix2cols):
            cross_sum = 0
            for sum_index in range(matrix1cols):
                cross_sum += matrix1[row][sum_index] * matrix2[sum_index][col]
            result_line.append(cross_sum)
        result.append(result_line)

    return result


def print_result(result):
    for line in result:
        print(*line, sep='\t')


print_result(multiply(matrix_a, matrix_b))
