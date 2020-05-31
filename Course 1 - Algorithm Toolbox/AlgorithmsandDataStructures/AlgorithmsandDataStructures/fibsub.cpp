#include <iostream>
#include <vector>
#include <cassert>

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current = 1;
    long long sum = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

int fibonacci_sum_fast(long long n) {
    if (n <= 1)
        return n;
    n = 2 + n;
    std::vector<int> fib;
    fib.push_back(0);
    fib.push_back(1);
    long long curr_fib = 0;
    for (int i = 2; i < n + 1; i++)
    {
        curr_fib = fib[i - 1] % 10 + fib[i - 2] % 10;
        fib.push_back(curr_fib % 10);
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
            return (curr_fib -1) % 10;
        }
    }

}



long long fibonacci_sum_fast_again(long long n) {
    if (n <= 1)
    {
        return n;
    }
    n = n + 2;
    long double my_phi = (1 + sqrt(5)) / 2;
    int fib6[6] = { 0, 1, 1, 2, 3, 5 };
    {
        if (n < 6) {
            return fib6[n];
        }
        long long i = 5;
        long long fib_number = 5;
        while (i < n) {
            fib_number = round(fib_number * my_phi);
            i++;
        }
        return fib_number % 10;
    }
}

int main() {
    //test_solution();
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_naive(n);
}
