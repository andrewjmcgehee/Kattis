# Rating: ~ 3.7 / 10
# Link: https://open.kattis.com/problems/kastenlauf
# Complexity: O(N^2) due to pair-wise checks where N is number of stops
# Memory: O(N) where N is number of stops

class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]

  def union(self, x, y):
    self.parent[self.find(x)] = self.find(y)

  def find(self, x):
    if self.parent[x] == x:
      return x
    else:
      self.parent[x] = self.find(self.parent[x])
      return self.parent[x]


def main():
  n = int(input())
  for _ in range(n):
    m = int(input())

    # source
    x, y = (int(x) for x in input().split())
    stops = [(x, y)]

    # stores
    for i in range(m):
      x, y = (int(x) for x in input().split())
      stops.append((x, y))

    # target
    x, y = [int(x) for x in input().split()]
    stops.append((x, y))

    # note that source is at index 0 and target is at index -1

    # 20 bottles of beer, 1 bottle every 50 meters gives that no distance
    # can be > 1000 meters

    # simply consider all pairwise relationships and union if less than 1000 meters
    # apart by manhattan distance
    uf = UnionFind(len(stops))
    for i in range(len(stops)):
      for j in range(i+1, len(stops)):
        a = stops[i]
        b = stops[j]
        if abs(a[0] - b[0]) + abs(a[1] - b[1]) <= 1000:
          uf.union(i, j)

    if uf.find(0) == uf.find(len(stops)-1):
      print("happy")
    else:
      print("sad")


if __name__ == '__main__':
  main()
