def scalar_product(vector1, vector2):
    """
    Calculate the scalar product (dot product) of two vectors.

    :param vector1: List of numbers representing the first vector.
    :param vector2: List of numbers representing the second vector.
    :return: Scalar product of the two vectors.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")


    return sum(x * y for x, y in zip(vector1, vector2))

def matrix_product(matrix1, matrix2):
    """
    Calculate the matrix product of two matrices.

    :param matrix1: List of lists where each sublist represents a row in the first matrix.
    :param matrix2: List of lists where each sublist represents a row in the second matrix.
    :return: Matrix product of the two matrices.
    """
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result