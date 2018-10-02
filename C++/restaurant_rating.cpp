/*
Rating: ~ 3.1 / 10
Link: https://open.kattis.com/problems/ratings
Complexity: O(NJK) where N is number of tie states, J is number of critics and K is number of possible sums
Memory: O(NKJ) for memo table for above parameters
*/

#include <cstdio>
using namespace std;

// memo table for 3 possible tie statuses, 15 possible critics,
// and 31 possible sums
long long memo[3][15][31];
int arr[15];
int n;

long long solve(int tie, int index, int remaining) {
  // no votes left so add 0 restaurants
  if (remaining < 0) return 0;

  // add one restaurant if not a tie and some remaining score is available
  if (index == n) {
    return (tie == 0 && remaining == 0) ? 0 : 1;
  }

  // if already calculated return
  if (memo[tie][index][remaining] != 0) {
    return memo[tie][index][remaining];
  }

  // recursive computations
  long long total = 0;
  for (int i = 0; i < 31; i++) {
    int tie_status = tie;
    // set tie status. 0 means not a tie, 1 means is a tie, 2 means current will lose
    if (tie == 1) {
      if (arr[index] < i) tie_status = 0;
      if (arr[index] == i) tie_status = 1;
      if (arr[index] > i) tie_status = 2;
    }
    // solve for remaining critics and scores
    total += solve(tie_status, index+1, remaining - i);
  }
  memo[tie][index][remaining] = total;
  return memo[tie][index][remaining];
}

int main() {
  while (true) {
    scanf("%d", &n);
    if (n == 0) break;

    int sum = 0;
    for (int i = 0; i < n; i++) {
      scanf("%d", &arr[i]);
      sum += arr[i];
    }
    // clear memo table
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 15; j++) {
        for (int k = 0; k < 31; k++) {
          memo[i][j][k] = 0;
        }
      }
    }

    printf("%lld\n", solve(1, 0, sum));
  }
  return 0;
}
