#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

long long MaxPairwiseProduct(const std::vector<long long>& numbers) {
    long long max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,
                numbers[first] * numbers[second]);
        }
    }

    return (long long)max_product;
}

long long MaxPairwiseProductFast(const std::vector<long long>& numbers) {
    int index1 = 0;
    int n = numbers.size();
    for (int i = 0; i < n; i++)
    {
        if (numbers[i] > numbers[index1])
        {
            index1 = i;
        }
    }
    int index2;
    if (index1 == 0)
    {
        index2 = 1;

    }
    else
    {
        index2 = 0;
    }
    for (int i = 0; i < n; i++)
    {
        if (i != index1 and numbers[i] > numbers[index2])
        {
            index2 = i;
        }
    }
    return ((long long)(numbers[index1] * numbers[index2]));
}

long long MaxPairwiseProductFastest(const std::vector<long long>& numbers) {
    std::vector<long long> pair_vec;
    int n = numbers.size();
    for (int i = 0; i < n; i++)
    {
        if (pair_vec.size() < 2)
        {
            pair_vec.push_back(numbers[i]);
        }
        else
        {
            long long max_elm = *max_element(pair_vec.begin(), pair_vec.end());
            long long min_elm = *min_element(pair_vec.begin(), pair_vec.end());
            if (numbers[i] >= max_elm or numbers[i] >= min_elm)
            {
                pair_vec.erase(std::find(pair_vec.begin(), pair_vec.end(), min_elm));
                pair_vec.push_back(numbers[i]);
            }
        }
    }
    return (long long)pair_vec[0] * pair_vec[1];
}


int main() {
    /*while (true)
    {
        int n = rand() % 100 + 2;
        std::cout << n << "\n";
        std::vector<long long> a;
        for (int i = 0; i < n; i++)
        {
            long long z =  (rand() * (long long)10000);
            a.push_back(z);
            std::cout << z << ' ';
        }
        std::cout << "\n";
        long long res1 = MaxPairwiseProduct(a);
        long long res2 = MaxPairwiseProductFastest(a);
        if (res1 == res2)
        {
            std::cout <<  "ok-----\n";
        }
        else
        {
            std::cout << "Error -------\n";
            break;
        }
    }*/
    int n;
    std::cin >> n;
    std::vector<long long> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProductFastest(numbers) << "\n";
    return 0;
}
