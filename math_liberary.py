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