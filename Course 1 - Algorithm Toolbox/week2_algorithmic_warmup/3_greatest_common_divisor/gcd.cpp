#include <iostream>
#include <cassert>

int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
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


int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << gcd_euclidian(a, b) << std::endl;
  return 0;
}
