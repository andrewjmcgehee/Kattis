/*
Rating: ~ 5.2 / 10
Link: https://open.kattis.com/problems/allpairspath
Complexity: O(N^3) due to floyd-warshall's algorithm
Memory: O(V^2) where V is number of vertices
*/

#include <cstdio>
using namespace std;

const int INF = 1000000;

int main() {
  while (true) {
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    if (n == 0 && m == 0 && q == 0) break;

    // adjacency matrix
    int adj[n][n];

    // initially all infinite weight
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        adj[i][j] = INF;
      }
    }

    // directed edges get assign positive or negative weights
    for (int i = 0; i < m; i++) {
      int u, v, weight;
      scanf("%d %d %d", &u, &v, &weight);
      adj[u][v] = weight;
    }

    // all identity edges have weight 0
    for (int i = 0; i < n; i++) {
      adj[i][i] = 0;
    }

    // floyd-warshall's
    for (int k = 0; k < n; k++) {
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
          if (adj[i][j] > (adj[i][k] + adj[k][j]) && adj[i][k] < INF && adj[k][j] < INF) {
            adj[i][j] = (adj[i][k] + adj[k][j]);
          }
        }
      }
    }

    // detect negtive cycles
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        for (int k = 0; k < n && adj[i][j] != -INF; k++) {
          if (adj[k][k] < 0 && adj[i][k] != INF && adj[k][j] != INF) {
            adj[i][j] = -INF;
          }
        }
      }
    }

    // Infinite distances indicate no path exists, regular edges indicate
    // shortest path, and -infinite edges indicate a negative cycle
    for (int i = 0; i < q; i++) {
      int src, target;
      scanf("%d%d", &src, &target);

      int dist = adj[src][target];
      if (dist == INF) {
        printf("Impossible\n");
      }
      else if (dist == -INF) {
        printf("-Infinity\n");
      }
      else {
        printf("%d\n", dist);
      }
    }
    printf("\n");
  }
  return 0;
}
