import sys
from math import log

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7'
}


def convert(s):
    try:
        number = ''
        for token in s:
            print(token)
            number += DIGIT_MAP[token]
            print(number)
            x = int(number)
            print(f'Conversion success!! x = {x}')
    except (KeyError, TypeError) as e:
        print(f'Conversion failed!!:: {e!r}', file=sys.stderr)  # print error detail to standard error stream
        raise
    return x


def string_log(s):
    v = convert(s)
    return log(v)


def sqrt(x):
    """
    Compute square root using the method of
    Heron of Alexandria.
    Args:
        x: The number for which the square root is to be computed

    Returns:
    The square root of x

    Raise:
        ValueError: If x is negative.

    """
    if x < 0:
        raise ValueError(
            "Cannot compute square root of "
            f"negative number {x}"
        )
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))  # will throw divide by zero
    except ValueError as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
