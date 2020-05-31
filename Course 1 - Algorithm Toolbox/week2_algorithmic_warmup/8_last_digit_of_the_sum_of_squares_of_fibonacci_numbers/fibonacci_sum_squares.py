# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fib_fast(n):
    fib = []
    fib.append(0)
    fib.append(1)
    curr_fib = 0
    for i in range(2,n+1):
        curr_fib = fib[i - 1] + fib[i - 2]
        fib.append(curr_fib)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return curr_fib

def get_fibonacci_huge_fast(m):
    n =10
    fib = []
    fibn_mod = []
    fib.append(0)
    fibn_mod.append(0%n)
    fib.append(1)
    fibn_mod.append(1%n)
    fib.append(1)
    fibn_mod.append(1%n)
    i = 3
    while (fibn_mod[i - 2] != 0 or fibn_mod[i - 1] != 1) and i >=2:
        curr_fib = fib[i - 1] + fib[i - 2]
        fib.append(curr_fib)
        fibn_mod.append(curr_fib%n)
        i += 1
    pisano_period =  len(fibn_mod)-2
    m_fib_mod = m % pisano_period
    return (fib_fast(m_fib_mod) % n)


if __name__ == '__main__':
    n = int(stdin.read())
    print((get_fibonacci_huge_fast(n) * get_fibonacci_huge_fast(n+1)) % 10)
