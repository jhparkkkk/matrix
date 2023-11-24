# fn linear_combination::<K>(u: &[Vector<K>], coefs: &[K]) -> Vector<K>;
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from colorama import Fore


def linear_combination(u, coef: [float]) -> 'linear_algebra.vector.Vector':
    """
    Computes a linear combination of vectors: multiply vector[i] by scalar[i]
then add vectors 

    Args:
        u (list[Vector]): List of vectors to be combined
        coef (list[float]): List of coefficients for each vector to be scaled

    Returns:
        Vector: result vector from the linear combination.
        
    Raises:
        ValueError: If the dimensions of the vectors don't match or if the sizes of u and coef are different.
    """
    size = len(u)
    if size != len(coef):
        raise ValueError("cannot compute linear combination of vector if size u doesn't match with size of coef")  
    res = Vector([0.] * len(u[0].data))
    for i in range(size):
        res.add(u[i].scl(coef[i]))
    return res

    # TODO: matrix linear combination
    # matrix_size = u[0].get_shape()
    # print('matrix size:', matrix_size)
    # Initialize res as a matrix with zeros
    # res = Matrix([[0.] * matrix_size[0] for _ in range(matrix_size[1])])