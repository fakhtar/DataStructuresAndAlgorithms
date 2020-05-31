#include <iostream>
#include <vector>

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % m;
}
uint64_t fibonacci_fast(int n) {
    std::vector<uint64_t> fib;
    fib.push_back(0);
    fib.push_back(1);
    uint64_t curr_fib = 0;
    for (int i = 2; i < n + 1; i++)
    {
        curr_fib = fib[i - 1] + fib[i - 2];
        fib.push_back(curr_fib);
    }
    if (n == 0)
    {
        return 0;
    }
    else
    {
        if (n == 1)
        {
            return 1;
        }
        else
        {
            return curr_fib;
        }
    }

}
uint64_t get_fibonacci_huge_fast(uint64_t m, uint64_t n) {
    std::vector<uint64_t> fib;
    std::vector<uint64_t> fibn_mod;
    fib.push_back(0);
    fibn_mod.push_back(0 % n);
    fib.push_back(1);
    fibn_mod.push_back(1 % n);
    fib.push_back(1);
    fibn_mod.push_back(1 % n);
    int i = 3;
    while ((fibn_mod[i - 2] != 0 or fibn_mod[i - 1] != 1) and i >= 2)
    {
        uint64_t curr_fib = fib[i - 1] + fib[i - 2];
        fib.push_back(curr_fib);
        fibn_mod.push_back(curr_fib % n);
        i += 1;
    }
    uint64_t pisano_period = fibn_mod.size()-2;
    uint64_t m_fib_mod = m % pisano_period;
    return (fibonacci_fast(m_fib_mod) % n);
}
int main() {
    uint64_t n, m;
    std::cin >> n >> m;
    std::cout << get_fibonacci_huge_fast(n, m) << '\n';
}
