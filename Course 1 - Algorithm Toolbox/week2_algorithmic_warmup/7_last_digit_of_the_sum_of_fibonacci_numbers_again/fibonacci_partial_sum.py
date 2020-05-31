# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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
    n = 100
    m = m + 2
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
    if m_fib_mod % 100 == 0:
        return 99
    else:
        return (fib_fast(m_fib_mod) % n) - 1


def fibonacci_partial_sum_fast(from_, to):
    test1 = get_fibonacci_huge_fast(to)
    test2 = get_fibonacci_huge_fast(from_ - 1)
    return (test1 - test2) % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))