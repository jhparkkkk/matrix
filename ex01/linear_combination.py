# fn linear_combination::<K>(u: &[Vector<K>], coefs: &[K]) -> Vector<K>;
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from colorama import Fore


def linear_combination(u: list[Vector], coef: [float]) -> Vector:
    """
    Computes a linear combination of vectors: multiply vector[i] by scalar[i]
    then add vectors

    B = c1⋅v1 + c2⋅v2 + … + cn⋅vn

    Args:
        u (list[Vector]): List of vectors to be combined
        coef (list[float]): List of coefficients for each vector to be scaled

    Returns:
        Vector: result vector from the linear combination.

    Raises:
        ValueError: If the dimensions of the vectors don't match or if the sizes of u and coef are different.
    """
    if not isinstance(u, list) or not all(isinstance(vec, Vector) for vec in u):
        raise TypeError("u must be a list of Vector objects")
    if not isinstance(coef, list) or not all(isinstance(c, float) for c in coef):
        raise TypeError("coef must be a list of floats")
    if len(u) != len(coef):
        raise ValueError(
            "cannot compute linear combination of vector if size u doesn't match with size of coef"
        )
    vec_linear_combination = Vector([0.0] * len(u[0].data))
    for i in range(len(u)):
        vec_linear_combination.add(u[i].scl(coef[i]))
    return vec_linear_combination
