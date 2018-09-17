/*
Rating: ~ 5.6 / 10
Link: https://open.kattis.com/problems/10kindsofpeople
Complexity: O(N*K) for an NxK matrix (assuming worst possible find in union find)
Memory: O(N*K) for an NxK matrix
*/

#include <iostream>
#include <vector>
using namespace std;

// union find methods
int find(vector<int>& uf, int a) {
  if (uf[a] == a) {
    return a;
  }
  uf[a] = find(uf, uf[a]);
  return uf[a];
}

void unite(vector<int>& uf, int a, int b) {
  a = find(uf, a);
  b = find(uf, b);

  if (a == b) {
    return;
  }
  uf[a] = b;
}

// helper for checking array bounds
bool safe(int row, int col, int i, int j) {
  if (i < 0) {
    return false;
  }
  if (j < 0) {
    return false;
  }

  if (i >= row) {
    return false;
  }
  if (j >= col) {
    return false;
  }
  return true;
}

int main() {
  int row, col;
  cin >> row >> col;

  // populate map
  int map[row][col];
  for (int i = 0; i < row; i++) {
    for (int j = 0; j < col; j++) {
      char tmp;
      cin >> tmp;
      map[i][j] = tmp - '0';
    }
  }

  // initialize union find
  vector<int> uf;
  for (int i = 0; i < row*col; i++) {
    uf.push_back(i);
  }

  // union all neighbors of like kind
  for (int i = 0; i < row; i++) {
    for (int j = 0; j < col; j++) {
      int x, y;

      x = i-1;
      y = j;

      if (safe(row, col, x, y) && map[i][j] == map[x][y]) {
        unite(uf, i*col + j, x*col + y);
      }

      x = i;
      y = j-1;
      if (safe(row, col, x, y) && map[i][j] == map[x][y]) {
        unite(uf, i*col + j, x*col + y);
      }

      x = i+1;
      y = j;
      if (safe(row, col, x, y) && map[i][j] == map[x][y]) {
        unite(uf, i*col + j, x*col + y);
      }

      x = i;
      y = j+1;
      if (safe(row, col, x, y) && map[i][j] == map[x][y]) {
        unite(uf, i*col + j, x*col + y);
      }
    }
  }

  // check if in same component
  int m;
  cin >> m;
  while (m--) {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    x1--;
    x2--;
    y1--;
    y2--;

    if (find(uf, x1*col + y1) == find(uf, x2*col + y2)) {
      if (map[x1][y1] == 1) {
        cout << "decimal" << '\n';
      }
      else {
        cout << "binary" << '\n';
      }
    }
    else {
      cout << "neither" << '\n';
    }
  }
}
