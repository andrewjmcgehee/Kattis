#include <bits/stdc++.h>
using namespace std;

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  fast();
  int n, m;
  while (true) {
    cin >> n >> m;
    if (n == 0 && m == 0) {
      break;
    }
    unordered_set<int> jack;
    for (int i = 0; i < n; i++) {
      int tmp;
      cin >> tmp;
      jack.insert(tmp);
    }
    int common = 0;
    for (int i = 0; i < m; i++) {
      int tmp;
      cin >> tmp;
      if (jack.find(tmp) != jack.end()) {
        common++;
      }
    }
    cout << common << endl;
  }
  return 0;
}
