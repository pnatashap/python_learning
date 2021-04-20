from typing import List


def continued_fraction(n1: int, n2: int) -> List[int]:
    if n1 == 0:
        return [0]
    if n2 == 0:
        raise ZeroDivisionError(f"Wrong fraction {n1}/{n2}")

    res = []
    rest = n1 % n2
    res.append(n1//n2)
    if rest > 1:
        res.extend(continued_fraction(n2, rest))
    elif rest == 1:
        res.append(n2)
    return res
