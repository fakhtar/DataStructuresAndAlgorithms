#include <iostream>
#include <vector>
#include <cassert>

int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}

int get_fibonacci_last_digit_fast(int n) {
    std::vector<int> fib;
    fib.push_back(0);
    fib.push_back(1);
    int curr_fib = 0;
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
            return curr_fib % 10;
        }
    }

}

void test_solution() {
    //int n = 1;
    //while (true)
    //{
    //    //assert(get_fibonacci_last_digit_naive(n) == get_fibonacci_last_digit_fast(n));
    //std::cout << "FIB Fast 1: " << get_fibonacci_last_digit_fast(n) << '\n';
    //std::cout << "FIB Naieve 1: " << get_fibonacci_last_digit_naive(n) << '\n';
    //    n += 1;
    //}

    //std::cout << "FIB Fast 1: " << fibonacci_fast(1) << '\n';
    //std::cout << "FIB Naieve 1: " << fibonacci_naive(1) << '\n';

    //assert(fibonacci_fast(3) == 2);
    //assert(fibonacci_fast(10) == 55);
    //for (int n = 0; n < 20; ++n)
    //    assert(fibonacci_fast(n) == fibonacci_naive(n));


    //for (int n = 0; n < 20; ++n){
    //    std::cout << "FIB Naieve: " << n << fibonacci_naive(n) << '\n';
    //    std::cout << "FIB Fast: " << n << fibonacci_fast(n) << '\n';
    //}
}

int main() {
    int n;
    std::cin >> n;
    int c = get_fibonacci_last_digit_fast(n);
    std::cout << c << '\n';
    }
