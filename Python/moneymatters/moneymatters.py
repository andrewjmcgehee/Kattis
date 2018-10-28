class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]

  def connected(self, x, y):
    return self.find(x) == self.find(y)

  def union(self, x, y):
    self.parent[self.find(x)] = self.find(y)

  def find(self, x):
    root = x
    while root != self.parent[root]:
      root = self.parent[root]
    # path compression
    while x != root:
      temp = self.parent[x]
      self.parent[x] = root
      x = temp
    return root


def main():
  n, m = (int(x) for x in input().split())

  owed = []
  for i in range(n):
    owed.append(int(input()))

  uf = UnionFind(n)
  for i in range(m):
    a, b = (int(x) for x in input().split())
    uf.union(a, b)

  debts = [0 for i in range(n)]
  for i in range(n):
    debts[uf.find(i)] += owed[i]

  possible = True
  for debt in debts:
    if debt != 0:
      possible = False
      break

  if possible:
    print('POSSIBLE')
  else:
    print('IMPOSSIBLE')

if __name__ == '__main__':
  main()


