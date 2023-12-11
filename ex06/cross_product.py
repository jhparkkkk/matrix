# cross_product::<K>(u: &Vector::<K>, v: &Vector::<K>) -> Vector::<K>;
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from linear_algebra.vector import Vector


def cross_product(
    u: "linear.algebra.vector.Vector", v: "linear.algebra.vector.Vector"
) -> "linear.algebra.vector.Vector":
    """Compute the cross product of two 3D vectors.

    Args:
        u (linear.algebra.vector.Vector): The first 3D vector.
        v (linear.algebra.vector.Vector): The second 3D vector.

    Raises:
        ValueError: If either vector does not have exactly 3 values.

    Returns:
        linear.algebra.vector.Vector: The cross product of the two vectors.
    """
    if u.get_size() != 3 or v.get_size() != 3:
        raise ValueError("vector must contains 3 values")

    return Vector(
        [
            u.data[1] * v.data[2] - u.data[2] * v.data[1],
            u.data[2] * v.data[0] - u.data[0] * v.data[2],
            u.data[0] * v.data[1] - u.data[1] * v.data[0],
        ]
    )
