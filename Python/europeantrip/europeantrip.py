# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/europeantrip
# Complexity: depends on precision desired but roughly O(log(E)) where E is epsilon
# Memory: O(1)

import math

# helper to calculate total distance from point to each vertex
def total_dist(A, B, C, x, y):
  dist = 0
  dist += math.hypot(A[0]-x, A[1]-y)
  dist += math.hypot(B[0]-x, B[1]-y)
  dist += math.hypot(C[0]-x, C[1]-y)
  return dist

def main():
  A = tuple(int(x) for x in input().split())
  B = tuple(int(x) for x in input().split())
  C = tuple(int(x) for x in input().split())

  # starting point
  x = (A[0] + B[0] + C[0]) / 3
  y = (A[1] + B[1] + C[1]) / 3

  # store current best
  best = total_dist(A, B, C, x, y)

  # changes in each direction
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  # scalar to modify dx and dy
  eps = 1000

  # set the precision of the algorithm here
  while eps > 0.00001:
    found = False
    # try each direction
    for i in range(4):
      x1 = x + eps * dx[i]
      y1 = y + eps * dy[i]
      # calculate new distance
      dist = total_dist(A, B, C, x1, y1)
      # if better store it
      if (dist < best):
        found = True
        best = dist
        x = x1
        y = y1
    # if not improvements, increase granularity
    if not found:
      eps /= 2

  print("%.5f %.5f" % (x, y))

if __name__ == "__main__":
  main()
