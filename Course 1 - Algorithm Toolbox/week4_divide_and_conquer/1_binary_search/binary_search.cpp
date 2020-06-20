#include <iostream>
#include <cassert>
#include <vector>
#include <cmath>

using std::vector;

int binary_search(const vector<int> &a, int x, int start, int end) {
  float left = start, right = end;
  if ((right < left) or (right == left and a[right] != x))
  {
      return -1;
  }
  float rightDiv2 = (ceil(float((right + left) / 2)));
  if (a[rightDiv2] == x)
  {
      return rightDiv2;
  }
  else
  {
      if (a[rightDiv2] < x)
      {
          end = right;
          binary_search(a, x, rightDiv2+1, end);
      }
      else
      {
              binary_search(a, x, left, rightDiv2-1);
      }
  }
}

int linear_search(const vector<int> &a, int x) {
  for (size_t i = 0; i < a.size(); ++i) {
    if (a[i] == x) return i;
  }
  return -1;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  int m;
  std::cin >> m;
  vector<int> b(m);
  for (int i = 0; i < m; ++i) {
    std::cin >> b[i];
  }
  for (int i = 0; i < m; ++i) {
    //replace with the call to binary_search when implemented
    std::cout << binary_search(a, b[i], 0, (int)a.size() -1) << ' ';
  }
}
