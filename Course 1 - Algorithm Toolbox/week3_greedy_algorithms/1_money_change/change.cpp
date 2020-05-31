#include <iostream>

int get_change(int changeOf) {
    int n = (int)changeOf / 10;
    changeOf = changeOf % 10; 
    if (changeOf == 0)
    {
        return n;
    }
    n = n + (int)changeOf / 5;
    changeOf = changeOf % 5; 
    if (changeOf == 0)
    {
        return n;
    }
    n = n + (int)changeOf / 1;
    changeOf = changeOf % 1;
    if (changeOf == 1)
    {
        return n;
    }
  return n;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
