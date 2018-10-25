/*
Rating: ~ 5.7 / 10
Link: https://open.kattis.com/problems/unionfind
Complexity: O(N log(N)) for N elements in the union find
Memory: O(N) for the union find parent array
*/
#include <iostream>
#include <vector>
using namespace std;

vector<int> parent(1000001);

// faster I/O - may TLE without it
void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

// builds the union find array
void build() {
  for (int i = 0; i < 1000001; i++) {
    parent[i] = i;
  }
}

// returns representative element of a given element in the union find
int find(int x) {
  if (parent[x] == x) return x;
  parent[x] = find(parent[x]);
  return parent[x];
}

// unites two disjoint sets
void unite(int x, int y) {
  parent[find(x)] = find(y);
}

int main() {
  build();
  fast();
  int n, q;
  cin >> n >> q;

  for (int i = 0; i < q; i++) {
    // store the operation
    char op;
    cin >> op;
    int x, y;
    cin >> x >> y;

    // ? means to compare find() of each element
    if (op == '?') {
      bool connected = find(x) == find(y);
      if (connected) {
        printf("yes\n");
      }
      else {
        printf("no\n");
      }
    }
    // otherwise unite the two
    else {
      unite(x, y);
    }
  }
  return 0;
}
