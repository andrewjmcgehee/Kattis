# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/islandhopping
# Complexity: O(V log(E)) for prim's
# Memory: O(V^2) for adjacency matrix

from queue import PriorityQueue

def findMST(adj, m):
  # track edges currently in mst
  mst = set()
  mst.add(0)

  # best weight to use when including vertex i
  # initialized to edge weights from vertex 0
  min_dist = [0 for i in range(m)]
  for i in range(m):
    min_dist[i] = adj[0][i]

  total = 0
  while len(mst) < m:
    # purposefully impossible
    best = float('inf')
    vertex = -1
    # try all other vertices with minimum distances
    for i in range(m):
      if i not in mst and min_dist[i] < best:
        best = min_dist[i]
        vertex = i
    # visit that vertex and add its weights
    # square roots will only be performed V times instead of V^2 times
    mst.add(vertex)
    total += pow(best, 0.5)
    # update weights with best of edges from new vertex or edges
    # from previous vertex
    for i in range(m):
      min_dist[i] = min(min_dist[i], adj[vertex][i])
  return total

def main():
  t = int(input())
  for case in range(t):
    m = int(input())
    # storing tuples of x y coords
    islands = []
    for i in range(m):
      x, y = map(float, input().split())
      islands.append((x, y))
    # no real benefit in using an adjacency list or edge list
    # because the graph is fully connected
    adj = [[0 for j in range(m)] for i in range(m)]
    for i in range(m):
      for j in range(i+1, m):
        ax, ay = islands[i]
        bx, by = islands[j]
        # dont use square roots here, integer math is faster than floating
        # point
        dist = (ax-bx)**2 + (ay-by)**2
        adj[i][j] = dist
        adj[j][i] = dist
    print(findMST(adj, m))


if __name__ == "__main__":
  main()
