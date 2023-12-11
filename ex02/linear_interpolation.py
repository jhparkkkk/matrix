from typing import TypeVar

V = TypeVar("V")


def lerp(u: V, v: V, t: float) -> V:
    """
    Performs linear interpolation between two values or objects: find a value between two known values
    based on a parameter `t` that specifies the interpolation factor (weight)

    Args:
        u (V): Starting value or object.
        v (V): Ending value or object.
        t (float): Interpolation factor, must be in the range [0, 1].

    Returns:
        V: Result of the linear interpolation between `u` and `v`.

    Raises:
        ValueError: If `t` is outside the range [0, 1].
        TypeError: If the types of `u` and `v` are not supported for linear interpolation.
    """
    if t < 0 or t > 1:
        raise ValueError("scalar t must be 0 ≤ t ≤ 1")
    if isinstance(u, (int, float)) and isinstance(v, (int, float)):
        return round((1 - t) * u + t * v, 2)
    elif hasattr(u, "lerp") and callable(getattr(u, "lerp")):
        return u.lerp(v, t)
    else:
        raise TypeError("invalid type to compute linear interpolation")
