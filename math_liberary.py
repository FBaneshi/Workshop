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


def vector_product(vector1, vector2):
    """
    Calculate the vector product (cross product) of two 3-dimensional vectors.

    :param vector1: List of 3 numbers representing the first vector.
    :param vector2: List of 3 numbers representing the second vector.
    :return: Vector product of the two vectors as a list of 3 numbers.
    """
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Both vectors must be of length 3")

    x1, y1, z1 = vector1
    x2, y2, z2 = vector2

    return [
        y1 * z2 - z1 * y2,
        z1 * x2 - x1 * z2,
        x1 * y2 - y1 * x2
    ]