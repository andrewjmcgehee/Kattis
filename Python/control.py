# Rating: ~ 4.5 / 10
# Link: https://open.kattis.com/problems/control
# Complexity: O(N log(N)) for union find
# Memory: O(N) for N potions

# typical union find
class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n+1)]
    # tracks component sizes
    self.comps = [1 for i in range(n+1)]

  def union(self, x, y):
    xroot = self.find(x)
    yroot = self.find(y)
    if xroot == yroot:
      return
    self.parent[yroot] = xroot
    # only part thats different is that we must also update the size of
    # a component when we union two sets
    self.comps[xroot] += self.comps[yroot]

  def find(self, x):
    if self.parent[x] == x:
      return x
    self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  # returns component size of representative element
  def size(self, x):
    root = self.find(x)
    return self.comps[root]


def main():
  # max size
  uf = UnionFind(500001)
  # number of potions
  p = int(input())
  potions = 0
  for i in range(p):
    q = [int(x) for x in input().split()]
    # ingredients of potion
    ings = q[1:]
    # holds all the required ingredients of the potion
    requires = set()
    for item in ings:
      root = uf.find(item)
      requires.add(root)

    # calculate the total size of all components containing required
    # ingredients
    total = 0
    for req in requires:
      total += uf.size(req)
    # if the total is equivalent to the number of ingredients then
    # its possible to make
    if total == q[0]:
      potions += 1
      # union all the ingredients
      for j in range(1, len(ings)):
        uf.union(ings[0], ings[j])
  print(potions)

if __name__ == '__main__':
  main()

