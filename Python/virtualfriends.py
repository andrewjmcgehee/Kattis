# Rating: ~ 4.8 / 10
# Link: https://open.kattis.com/problems/virtualfriends
# Complexity: O(N log(N)) due to union find and where N is number of relationships
# Memory: O(N) where N is number of individual people

class UnionFind:
  def __init__(self):
    self.parent = dict()

  def union(self, x, y):
    self.parent[x] = self.find(y)

  def find(self, x):
    if self.parent[x] == x:
      return x
    else:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    uf = UnionFind()

    # this dictionary will track the size of a group by storing its representative
    # element as the key and the size as the value
    group_sizes = dict()

    for i in range(n):
      a, b = input().split()
      # check to avoid key errors
      if a not in uf.parent:
        uf.parent[a] = a
      if b not in uf.parent:
        uf.parent[b] = b

      # find a's and b's parents
      aroot = uf.find(a)
      broot = uf.find(b)

      # if they are share the same parent, they are already united, and the
      # size of their group is already stored
      if aroot == broot:
        print(group_sizes[aroot])
        continue

      # otherwise unite the two groups
      # note that broot will become aroot's parent
      uf.union(aroot, broot)

      # yet again, a check to avoid key errors
      if aroot not in group_sizes:
        group_sizes[aroot] = 1
      if broot not in group_sizes:
        group_sizes[broot] = 1

      # since broot is the parent, we will store the size in it
      group_sizes[broot] += group_sizes[aroot]
      # safe to delete aroot from the sizes table to avoid confusion later
      del group_sizes[aroot]

      print(group_sizes[broot])

if __name__ == '__main__':
  main()

