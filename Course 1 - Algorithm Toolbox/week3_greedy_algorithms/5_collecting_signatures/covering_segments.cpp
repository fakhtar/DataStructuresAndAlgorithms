#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

using std::vector;

class Segment {
public:
  int start, end;
  bool operator < (const Segment& seg) const
  {
      return (end < seg.end);
  }
};

vector<int> optimal_points(vector<Segment> &segments) {
  vector<int> points;
  std::sort(segments.begin(), segments.end());
  int currEnd;

  //write your code here
  for (size_t i = 0; i < segments.size(); ++i) {

      if (points.size()==0)
      {
          int countOfEnd = std::count(points.begin(), points.end(), segments[i].end);
          if (countOfEnd == 0)
          {
              points.push_back(segments[i].end);
              currEnd = segments[i].end;

          }
      }
      else
      {
          if (segments[i].start <= currEnd and segments[i].end >= currEnd)
            {
                continue;
            }
          else
          {
              points.push_back(segments[i].end);
              currEnd = segments[i].end;
          }
      }
      
  }
  return points;
}

int main() {
  int n;
  std::cin >> n;
  vector<Segment> segments(n);
  for (size_t i = 0; i < segments.size(); ++i) {
    std::cin >> segments[i].start >> segments[i].end;
  }
  vector<int> points = optimal_points(segments);
  std::cout << points.size() << "\n";
  for (size_t i = 0; i < points.size(); ++i) {
    std::cout << points[i] << " ";
  }
}
