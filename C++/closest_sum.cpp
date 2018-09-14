/*
* Rating: ~ 2.9 / 10
* Link: https://open.kattis.com/problems/closestsums
* Complexity: O(n^2) where n is number of numbers (pair wise sums)
* Memory: O(n) for each number
*/

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
  int case_num = 1;
  int n;
  while (cin >> n) {
    vector<int> nums;
    while (n--) {
      int tmp;
      cin >> tmp;
      nums.push_back(tmp);
    }

    // get pair wise sums for all numbers
    vector<int> sums;
    for (int i = 0; i < nums.size(); i++) {
      for (int j = i+1; j < nums.size(); j++) {
        sums.push_back(nums[i] + nums[j]);
      }
    }

    cout << "Case " << case_num++ << ":\n";
    int m;
    cin >> m;
    while (m--) {
      int target;
      cin >> target;
      int res = -1;
      int diff = 1000000000;
      // complete search
      for (int i = 0; i < sums.size(); i++) {
        int tmp = abs(sums[i] - target);
        if (tmp < diff) {
          diff = tmp;
          res = sums[i];
        }
      }
      cout << "Closest sum to " << target << " is " << res << ".\n";
    }
  }
}
