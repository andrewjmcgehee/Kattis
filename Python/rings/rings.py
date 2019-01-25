# Rating: ~ 5.8 / 10
# Link: https://open.kattis.com/problems/rings

import math

# union find class
class UnionFind:
  def __init__(self, x):
    self.parent = [i for i in range(x+1)]

  def union(self, x, y):
    self.parent[self.find(x)] = self.find(y)

  def find(self, x):
    if self.parent[x] == x:
      return x
    self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

def main():
  while True:
    t = int(input())
    # break on -1
    if t == -1:
      break

    # first ring is none to avoid 0 indexing
    rings = [None]
    # get ring dimensions
    for i in range(t):
      x, y, r = map(float, input().split())
      rings.append((x, y, r))

    # initialize union find
    uf = UnionFind(t)
    # compute pairwise distances
    for i in range(1, t+1):
      for j in range(i+1, t+1):
        ax, ay, ar = rings[i]
        bx, by, br = rings[j]
        dist = math.hypot(ax-bx, ay-by)
        rads = ar + br
        # if distance is < than radius then circles can overlap
        # but distance apart must also be greater than difference
        # of radii
        if rads > dist and dist > abs(ar - br):
          uf.union(i, j)

    # find all parents and track component size
    comp_sizes = dict()
    for i in range(1, t+1):
      parent = uf.find(i)
      if parent not in comp_sizes:
        comp_sizes[parent] = 0
      comp_sizes[parent] += 1

    # output
    largest = max(comp_sizes.values())
    if largest == 1:
      print('The largest component contains 1 ring.')
    else:
      print('The largest component contains %i rings.' % largest)

if __name__ == "__main__":
  main()
