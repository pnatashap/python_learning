"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    k = len(args)
    result = []
    idx = [0 for i in range(k)]
    has_next = True
    while has_next:
        result.append([args[x][idx[x]] for x in range(k)])
        has_next = _shift_to_next(k-1, idx, args)

    return result


def _shift_to_next(position: int, idx: List[int], args: List[any]) -> bool:
    next_position = idx[position] + 1
    idx[position] = next_position
    if len(args[position]) <= next_position:
        next_position = 0
        idx[position] = next_position
        if position > 0:
            return _shift_to_next(position-1, idx, args)
        else:
            return False

    return True
