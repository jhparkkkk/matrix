from typing import TypeVar

V = TypeVar('V')

def lerp(u: V, v: V, t: float) -> V:
    if t < 0 or t > 1:
        raise ValueError("scalar t must be 0 ≤ t ≤ 1")
    if isinstance(u, (int, float)):
        return round((1 - t) * u + t * v, 2)
    elif hasattr(u, 'lerp') and callable(getattr(u, 'lerp')):
        res = u.lerp(v, t)
        # print(u)
        # print(res)
        return res
