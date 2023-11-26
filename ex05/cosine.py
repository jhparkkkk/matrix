
def angle_cos(u: 'linear.algebra.vector.Vector', v: 'linear.algebra.vector.Vector') -> float:
    if all(component == 0.0 for component in u) or all(component == 0.0 for component in v):
        raise ValueError("one of the vector is zero")
    if u.get_size() != v.get_size():
        raise ValueError("vectors are different size")
    return round((u.dot(v) / (u.norm() * v.norm())), 9)