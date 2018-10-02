/*
Rating: ~ 5.8 / 10
Link: https://open.kattis.com/problems/knapsack
Complexity: O(NK) for N weights and K values
Memory: O(NK) for N weights and K values
*/

#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> &vals, vector<int> &weights, int n, int cap) {
  // build 2d memo array where row is item id and col is weight
  vector<vector<int>> memo(n+1, vector<int>(cap+1, 0));

  for (int i = 1; i <= n; i++) {
    // actual index is one less
    int index = i-1;
    for (int j = 0; j <= cap; j++) {
      int weight = j + weights[index];
      int value = memo[i-1][j] + vals[index];

      // max of including it or not including it
      memo[i][j] = max(memo[i][j], memo[i-1][j]);

      // bounds checking
      if (weight <= cap) {
        memo[i][weight] = max(memo[i][weight], value);
      }
    }
  }

  // retrace items included by checking if val is the same as cell above it
  vector<int> indices;
  int col = cap;
  for (int i = n; i > 0; i--) {
    if (memo[i][col] != memo[i-1][col]) {
      int index = i-1;
      indices.push_back(index);
      col -= weights[index];
    }
  }
  return indices;
}

int main() {
  double m;
  int n;
  while (cin >> m >> n) {
    int capacity = (int) m;

    vector<int> vals(n);
    vector<int> weights(n);
    for (int i = 0; i < n; i++) {
      cin >> vals[i] >> weights[i];
    }

    // returns indices of items included in optimal solution
    vector<int> indices = solve(vals, weights, n, capacity);
    cout << indices.size() << '\n';

    for (int i = 0; i < indices.size(); i++) {
      cout << indices[i] << " ";
    }
    cout << '\n';
  }
}
