#include <bits/stdc++.h>
using namespace std;

int main() {
  int h, w, n;
  cin >> h >> w >> n;

  int layers = 0;
  bool possible = true;
  int row = 0;
  for (int i = 0; i < n; i++) {
    int brick;
    cin >> brick;
    row += brick;
    if (layers == h) {
      break;
    }
    if (row > w) {
      possible = false;
      break;
    }
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
