/*
Rating: ~ 3.6 / 10
Link: https://open.kattis.com/problems/communicationssatellite
*/

#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <tuple>
using namespace std;

typedef long long ll;

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int find(vector<int>& uf, int x) {
  if (uf[x] == -1) return x;
  return uf[x] = find(uf, uf[x]);
}

void join(vector<int>& uf, int x, int y) {
  int x_root = find(uf, x);
  int y_root = find(uf, y);
  if (x_root == y_root) return;
  uf[x_root] = y_root;
}

double distance(tuple<int, int, int> a, tuple<int, int, int> b) {
  int dx = get<0>(a) - get<0>(b);
  int dy = get<1>(a) - get<1>(b);
  return sqrt(dx*dx + dy*dy) - (get<2>(a) + get<2>(b));
}

int main() {
  fast();
  int n;
  cin >> n;
  vector<tuple<int, int, int>> sats;
  for (int i = 0; i < n; i++) {
    int x, y, r;
    cin >> x;
    cin >> y;
    cin >> r;
    sats.push_back({x, y, r});
  }

  vector<tuple<double, int, int>> edges;
  for (int i = 0; i < n; i++) {
    for (int j = i+1; j < n; j++) {
      auto a = sats[i];
      auto b = sats[j];
      double dist = distance(a, b);
      edges.push_back({dist, i, j});
    }
  }

  sort(edges.begin(), edges.end());

  vector<int> uf(n, -1);
  double total_dist = 0;
  for (int i = 0; i < edges.size(); i++) {
    if (find(uf, get<1>(edges[i])) != find(uf, get<2>(edges[i]))) {
      join(uf, get<1>(edges[i]), get<2>(edges[i]));
      total_dist += get<0>(edges[i]);
    }
  }
  cout << fixed;
  cout.precision(8);
  cout << total_dist << '\n';
  return 0;
}
