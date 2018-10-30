/*
Rating: ~ 3.0 / 10
Link: https://open.kattis.com/problems/dicebetting
Complexity: O(N) where N is number of throws
Memory: O(N) for memo array
*/

#include <iostream>
#include <vector>
using namespace std;

int n, s, k;
vector<vector<double>> memo;

// recursive function for finding probablity of a new number with n throws
// and s numbers already seen
double probability(int throws, int seen) {
  if (seen >= k) {
    return 1.0;
  }

  if (throws == 0) {
    return 0.0;
  }

  if (memo[throws][seen] != -1.0) {
    return memo[throws][seen];
  }

  // simple probablity
  double old_prob = (double)seen / s;
  // DeMorgan's Law
  double new_prob = 1 - old_prob;

  // recursive bit where first call represents not seeing a new number, and second represents
  // seeing a new number
  double prob = old_prob * probability(throws-1, seen) + new_prob * probability(throws-1, seen+1);
  memo[throws][seen] = prob;
  return prob;
}

int main() {
  cin >> n >> s >> k;
  memo.resize(n+1);
  for (int i = 0; i < n+1; i++) {
    memo[i].resize(s+1);
    fill(memo[i].begin(), memo[i].end(), -1.0);
  }

  cout.precision(9);
  // start with n throws and 0 seen
  cout << probability(n, 0) << endl;
}

