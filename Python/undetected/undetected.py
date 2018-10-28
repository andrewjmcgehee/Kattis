# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/undetected
# Complexity: O(N^2) due to checking pair-wise relationships
# Memory: O(N)

from math import sqrt

class UnionFind:
  def __init__(self, n):
    self.parent = [int(i) for i in range(n+2)]

  def union(self, x, y):
    if self.find(x) == self.find(y):
      return
    self.parent[self.find(x)] = self.find(y)

  def find(self, x):
    if self.parent[x] == x:
      return x
    else:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

def main():
  n = int(input())

  # note the constructor of our union find initializes 2 extra spaces
  # the left and right walls
  uf = UnionFind(n)

  circles = []
  for i in range(n):
    x, y, r = [int(i) for i in input().split()]
    circles.append((x, y, r))


  # we must check each circle with the left bound, and the right bound
  # as well as with all previous circles.
  num_circles = 0
  for i in range(len(circles)):
    xf, yf, rf = circles[i]

    # union with left bound if x value less than radius
    if xf < rf:
      # note the circles location in the union find is i+1
      uf.union(0, i+1)

    # union with right bound if 200 - x value less than radius
    if 200 - xf < rf:
      uf.union(i+1, len(uf.parent)-1)

    # check other circles
    for j in range(i):
      x0, y0, r0 = circles[j]
      dist = sqrt((xf - x0)**2 + (yf - y0)**2)

      # if distance less than sum of both radii, union
      if dist < rf + r0:
        uf.union(j+1, i+1)

    # if left bound and right bound have same representative element
    # the entire horizontal has been covered
    if uf.find(0) != uf.find(-1):
      num_circles += 1
    else:
      break
  print(num_circles)

if __name__ == '__main__':
  main()


