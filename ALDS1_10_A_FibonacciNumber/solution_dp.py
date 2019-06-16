from time import time


def fibonacci(n):
    """
    >>> fibonacci(3)
    3
    >>> fibonacci(4)
    5
    >>> fibonacci(10)
    89
    """
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    n = int(input())
    start_time = time()
    ret = fibonacci(n)
    print(ret)
    print(time() - start_time)
