/*
Rating: ~ 5.6 / 10
Link: https://open.kattis.com/problems/stogovi
Complexity: O(
Memory: O(
*/

#include <cstdio>
#include <vector>
using namespace std;

const int MAX = 300001;

vector<int> paths[MAX];
vector<int> tour;
int depth[MAX];
int position[MAX];
int tree[MAX*8];
int parent[MAX];
int id[MAX];

void dfs(int current, int parent) {
  position[current] = tour.size();
  tour.push_back(current);
  for (int i : paths[current]) {
    depth[i] = depth[current] + 1;
    dfs(i, current);
    tour.push_back(current);
  }
}

void build(int i, int left, int right) {
  if (left == right) {
    tree[i] = tour[left];
    return;
  }
  int mid = (left + right) / 2;
  build(i*2, left, mid);
  build(i*2 + 1, mid+1, right);
  tree[i] = min(tree[i*2], tree[i*2 + 1]);
}

int query(int i, int left, int right, int s, int e) {
  if (left > e || right < s) return 1000000000;
  if (left >= s && right <= e) return tree[i];
  int mid = (left + right) / 2;

  int q1 = query(i*2, left, mid, s, e);
  int q2 = query(i*2 + 1, mid+1, right, s, e);
  return min(q1, q2);
}

int main() {
  int N, a, b, c;
  char command;
  vector<pair<int,int>> qs;

  scanf("%d", &N);
  for (int i = 0;i <= N; i++) {
    id[i] = i;
  }

  for (int i = 1;i <= N; i++) {
    scanf(" %c", &command);
    if (command == 'a') {
      scanf("%d", &a);
      paths[id[a]].push_back(i);
      parent[i] = id[a];
    }
    else if (command == 'b') {
      scanf("%d", &a);
      qs.push_back({-1, id[a]});
      id[i] = parent[id[a]];
      parent[i] = parent[parent[id[a]]];
    }
    else {
      scanf("%d %d", &a, &b);
      id[i] = id[a];
      parent[i] = parent[id[a]];
      qs.push_back({i,b});
    }
  }
  dfs(0, -1);
  build(1, 0, tour.size()-1);
  for (pair<int,int> i : qs) {
    if (i.first == -1){
      printf("%d\n", i.second);
      continue;
    }
    a = id[i.first];
    b = id[i.second];
    if (position[a] > position[b]) swap(a, b);
    c = query(1, 0, tour.size()-1, position[a], position[b]);
    printf("%d\n", depth[c]);
  }
  return 0;
}
