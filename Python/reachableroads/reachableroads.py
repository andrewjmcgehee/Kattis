# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/reachableroads
# Complexity: O(N log N) for union find
# Memory: O(N) for N cities

# classic union find problem
class UnionFind:
  def __init__(self):
    self.parent = [i for i in range(1005)]

  def union(self, x, y):
    self.parent[self.find(y)] = self.find(x)

  def find(self, x):
    if self.parent[x] == x:
      return x
    # path compression done iteratively for recursion depth RTE
    indices = []
    while self.parent[x] != x:
      indices.append(x)
      x = self.parent[x]
    while indices:
      i = indices.pop()
      self.parent[i] = x
    return x

def main():
  n = int(input())
  for i in range(n):
    m = int(input())
    uf = UnionFind()
    r = int(input())
    for j in range(r):
      # union roads
      a, b = map(int, input().split())
      uf.union(a, b)

    # number of connected components
    comps = set()
    for j in range(m):
      # finding compresses path
      comps.add(uf.find(j))
    # for n cities, there are n-1 roads
    print(len(comps)-1)


if __name__ == "__main__":
  main()
