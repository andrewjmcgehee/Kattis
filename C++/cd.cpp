/*
Rating: ~ 4.1 / 10
Link: https://open.kattis.com/problems/cd
Complexity: O(N + K) where N is number of Jacks CDs and K is number of Jills
Memory: O(N) where N is number of Jacks CDs
*/

#include <bits/stdc++.h>
using namespace std;

// I/O optimization
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
    // duplicates don't matter. use a set
    unordered_set<int> jack;
    for (int i = 0; i < n; i++) {
      int tmp;
      cin >> tmp;
      jack.insert(tmp);
    }
    // no need to represent jill as set, ust check if jack has the CD
    // only interested in intersect
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
