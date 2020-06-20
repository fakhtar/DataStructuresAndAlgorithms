#include <algorithm>
#include <iostream>
#include <vector>
#include <unordered_map>

using std::vector;


int get_majority_element(vector<int> &a, int left, int right) {
    std::unordered_map<int, int> u = {    };
    float arr_len_div2 = float(right) / 2;
    for (int i = 0; i < right; i++)
    {
        int item = a[i];
        std::unordered_map<int, int>::const_iterator got = u.find(item);
        if (got == u.end())
            u[item] = 1;
        else {
            u[item] = u[item] + 1;
            if (u[item] > arr_len_div2)
            {
                return 1;
            }
        }
    }
    return -1;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  std::cout << (get_majority_element(a, 0, a.size()) != -1) << '\n';
}
