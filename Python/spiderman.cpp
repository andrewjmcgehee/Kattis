#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> memo(40, vector<int>(1001, -1));
vector<vector<int>> path(40, vector<int>(1001, -1));
int INF = 1000000;

void reset() {
  for (int i = 0; i < memo.size(); i++) {
    fill(memo[i].begin(), memo[i].end(), -1);
  }
  for (int i = 0; i < path.size(); i++) {
    fill(path[i].begin(), path[i].end(), -1);
  }
}

int climb(vector<int> arr, int index, int height) {
  if (height < 0) return INF;
  if (index == arr.size()) {
    return height == 0 ? height : INF;
  }
  if (memo[index][height] != -1) {
    return memo[index][height];
  }

  int up = climb(arr, index+1, height + arr[index]);
  int down = climb(arr, index+1, height - arr[index]);
  int min;
  if (up < down) {
    path[index][height] = 1;
    min = up;
  }
  else {
    path[index][height] = 2;
    min = down;
  }
  memo[index][height] = max(height, min);
  return memo[index][height];
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector<int> dists(n);
    for (int i = 0; i < n; i++) {
      cin >> dists[i];
    }
    reset();
    if (climb(dists, 0, 0) == INF) {
      cout << "IMPOSSIBLE\n";
      continue;
    }

    string ans = "";
    int height = 0;
    for (int i = 0; i < n; i++) {
      if (path[i][height] == 1) {
        ans += "U";
        height += dists[i];
      }
      else {
        ans += "D";
        height -= dists[i];
      }
    }
    cout << ans << '\n';
  }
  return 0;
}
