#include <iostream>
#include <vector>

using std::vector;

vector<int> optimal_summands(int n) {
  int num = 0;
  vector<int> summands;
  while (n != 0)
  {
      num += 1;
      n = n - num;
      summands.push_back(num);
      if (std::count(summands.begin(), summands.end(), n) != 0)
      {
          summands.pop_back();
          n = n + num;
      }
  }
  return summands;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> summands = optimal_summands(n);
  std::cout << summands.size() << '\n';
  for (size_t i = 0; i < summands.size(); ++i) {
    std::cout << summands[i] << ' ';
  }
}
