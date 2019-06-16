from time import time


n_max = 44
memo = [-1] * n_max


def fibonacci(n):
    global memo
    fib_nm1, fib_nm2 = memo[n - 1], memo[n - 2]

    if n == 0 or n == 1:
        return 1
    if fib_nm1 == -1:
        fib_nm1 = memo[n - 1] = fibonacci(n - 1)
    if fib_nm2 == -1:
        fib_nm2 = memo[n - 2] = fibonacci(n - 2)
    return fib_nm1 + fib_nm2


n = int(input())
start_time = time()
ret = fibonacci(n)
print(ret)
# print('{:.2f}s'.format(time() - start_time))
