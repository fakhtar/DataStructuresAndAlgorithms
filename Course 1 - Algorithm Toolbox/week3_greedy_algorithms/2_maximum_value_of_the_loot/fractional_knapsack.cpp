#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

//struct less_than_key
//{
//    inline bool operator() (const item& item1, const item& item2)
//    {
//        return (item1.valPerWEight < item1.valPerWEight);
//    }
//};
class item
{
public:
    int weight;
    int value;
    double valPerWEight;
    item(int weight, int value, double valPerWEight) {
        this->weight = weight;
        this->value = value;
        this->valPerWEight = valPerWEight;
    };
    bool operator < (const item& item) const
    {
        return (valPerWEight > item.valPerWEight);
    }

private:

};


double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;
  vector<item> items;
  //vector<double> wPerVal;
  for (int i = 0; i < weights.size(); i++)
  {
      item item(weights[i], values[i], double (values[i]) / double (weights[i]));
      items.push_back(item);
      //wPerVal.push_back(values[i] / weights[i]);
  }
  std::sort(items.begin(), items.end());
  return value;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
