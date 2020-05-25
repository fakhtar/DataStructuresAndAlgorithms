#include <iostream>
#include <cassert>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long long gcd_euclidian(long long a, long long b) {
    if (b == 0)
    {
        return a;
    }
    else
    {
        return gcd_euclidian(b, a % b);
    }
}

bool is_prime(long long n) {
    bool isPrime = true;

    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }
    return isPrime;
}

long long lcm_euclidian(long long a, long long b) {
        long long curr_gcd = gcd_euclidian(a, b);
        return (a * b) / curr_gcd;
}


//void test_solution() {
//    while (true)
//    {
//        int a = rand() * 100000;
//        int b = rand() * 100000;
//        assert(lcm_euclidian(a, b) == lcm_naive(a, b));
//    }
//}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm_euclidian(a, b) << std::endl;
  return 0;
}
