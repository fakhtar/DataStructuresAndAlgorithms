#include <iostream>
#include <cassert>
#include <vector>

// The following code calls a naive algorithm for computing a Fibonacci number.
//
// What to do:
// 1. Compile the following code and run it on an input "40" to check that it is slow.
//    You may also want to submit it to the grader to ensure that it gets the "time limit exceeded" message.
// 2. Implement the fibonacci_fast procedure.
// 3. Remove the line that prints the result of the naive algorithm, comment the lines reading the input,
//    uncomment the line with a call to test_solution, compile the program, and run it.
//    This will ensure that your efficient algorithm returns the same as the naive one for small values of n.
// 4. If test_solution() reveals a bug in your implementation, debug it, fix it, and repeat step 3.
// 5. Remove the call to test_solution, uncomment the line with a call to fibonacci_fast (and the lines reading the input),
//    and submit it to the grader.

long long fibonacci_naive(int n) {
    if (n <= 1)
        return n;

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2);
}

long long fibonacci_fast(int n) {
    std::vector<long long> fib;
    fib.push_back(0);
    fib.push_back(1);
    long long curr_fib = 0;
    for (int i = 2; i < n+1; i++)
    {
        curr_fib = fib[i - 1] + fib[i - 2];
        fib.push_back(curr_fib);
    }
    if (n==0)
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

void test_solution() {
    //int n = 1;
    //while (true)
    //{
    //    assert(fibonacci_fast(n) == fibonacci_naive(n));
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
    //test_solution();
    int n = 0;
    std::cin >> n;

    //std::cout << fibonacci_naive(n) << '\n';
    std::cout << fibonacci_fast(n) % 100 << '\n';
    return 0;
}
