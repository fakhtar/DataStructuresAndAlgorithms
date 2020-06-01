#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    stops.push_back(dist);
    stops.insert(stops.begin(), 0);
    int sizeOfStops = stops.size();
    int currStop = 0;
    int distTrav;
    int numStops = 0;
    for (size_t i = 0; i < sizeOfStops; i++)
    {
        if (sizeOfStops > i+1 and stops[i + 1] - stops[i] > tank)
        {
            return -1;
        }
        else
        {
            if (stops[i] - stops[currStop] <= tank)
            {
                distTrav = stops[i];
            }
            else
            {
                currStop = i-1;
                numStops += 1;
            }
        }
    }
    return numStops;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
