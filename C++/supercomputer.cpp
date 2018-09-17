/*
Rating: 3.8
Link: https://open.kattis.com/problems/supercomputer
Complexity: O(sqrt(n)) where n is number of bits (due to square root decomposition)
Memory: O(n) where n is number of bits
*/

#include <cmath>
#include <iostream>
#include <vector>
using namespace  std;

int main() {
  int n;
  int m;
  cin >> n >> m;

  int k = int(sqrt(n)) + 2;

  // bucketize array (square root decomposition)
  vector<int> bits(n);
  vector<int> buckets((n-1)/k + 1);

  for (int i = 0; i < m; i++) {
    char c;
    cin >> c;

    if (c == 'F') {
      int x;
      cin >> x;
      x--;

      // flip bit and update bucket
      if (bits[x] == 0) {
        bits[x] = 1;
        buckets[x/k]++;
      }
      else {
        bits[x] = 0;
        buckets[x/k]--;
      }
    }
    else {
      int l;
      int r;
      cin >> l >> r;
      l--;
      r--;

      // get segment from left index to next bucket, sum buckets, and get portion after last bucket to right index
      int sum = 0;
      for (size_t i = 0; i < buckets.size(); i++) {
        int a = k*i;
        int b = a + k - 1;

        if (l <= a && b <= r) {
          sum += buckets[i];
        }
        else if (b < l || r < a) {
          continue;
        }
        else {
          for (int j = max(a, l); j <= min(b, r); j++) {
            sum += bits[j];
          }
        }
      }
      cout << sum << '\n';
    }
  }
  return 0;
}
