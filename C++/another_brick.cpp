/*
Rating: ~ 1.9 / 10
Link: https://open.kattis.com/problems/anotherbrick
Complexity: O(N) where N is number of bricks
Memory: O(1)
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
  int h, w, n;
  cin >> h >> w >> n;

  // layers does not need to exceed height
  int layers = 0;
  bool possible = true;
  int row = 0;
  for (int i = 0; i < n; i++) {
    int brick;
    cin >> brick;
    row += brick;
    // success
    if (layers == h) {
      break;
    }
    // failure because row is uneven
    if (row > w) {
      possible = false;
      break;
    }
    // successfully added 1 layer
    else if (row == w) {
      layers += 1;
      row = 0;
    }
  }
  if (possible) {
    cout << "YES\n";
  }
  else {
    cout << "NO\n";
  }
  return 0;
}
