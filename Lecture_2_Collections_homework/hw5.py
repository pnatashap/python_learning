# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function named custom_range that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, List, Sequence


def custom_range(orig_seq: Sequence[Any], *args: Any) -> List[Any]:
    seq = orig_seq
    start, stop, step = None, None, 1
    start_index = 0
    if len(args) == 3:
        start, stop, step = args
        start_index = -1
    elif len(args) == 2:
        if type(args[1]) is int:
            step = args[1]
            stop = args[0]
        else:
            stop = args[1]
            start = args[0]
            start_index = -1
    elif len(args) == 1:
        stop = args[0]
    elif len(args) > 3:
        raise Exception("Invalid number of input parameters")

    result = []
    if step < 1:
        seq = reversed(orig_seq)

    for i, o in enumerate(seq):
        if start_index < 0:
            if o == start:
                start_index = i
            else:
                continue

        if o == stop:
            break

        if (i - start_index) % step == 0:
            result.append(o)

    return result
