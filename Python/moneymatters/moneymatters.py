# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/moneymatters
# Complexity: O(N log(N)) for union find
# Memory: O(N) for N for N people

# basic union find
class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]

  def connected(self, x, y):
    return self.find(x) == self.find(y)

  def union(self, x, y):
    self.parent[self.find(x)] = self.find(y)

  def find(self, x):
    if self.parent[x] == x:
      return x
    self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

def main():
  # num people, num connections
  n, m = (int(x) for x in input().split())

  # stores the ledger of debts
  owed = []
  for i in range(n):
    owed.append(int(input()))

  # unions the connected people
  uf = UnionFind(n)
  for i in range(m):
    a, b = (int(x) for x in input().split())
    uf.union(a, b)

  # initially 0 debt for each
  debts = [0 for i in range(n)]
  # for each debt, find the representative node, and add the debt
  for i in range(n):
    debts[uf.find(i)] += owed[i]

  # if any debt is non zero, impossible
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


