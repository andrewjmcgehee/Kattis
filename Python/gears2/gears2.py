# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/gears2
# Complexity: O(V) for V gears
# Memory: O(V^2) for adjacency matrix

from math import gcd, hypot

# determines the rotation of a given gear
def rotate(adj, n):
  # visited array which tracks rotation
  vis = [0 for i in range(n)]
  q = [0]
  # 1 signifies rotating clockwise
  vis[0] = 1
  while q:
    current = q.pop(0)
    for i in range(n):
      # try all neighboring gears
      if adj[current][i]:
        # alternating gears should never have positive product
        if vis[i] * vis[current] == 1:
          # stuck
          return (-1, -1)
        # havent visited gear yet
        if vis[i] == 0:
          q.append(i)
          # initial state should be alternate rotation from current
          # gear
          vis[i] = -1 * vis[current]
  # last gear not connected
  if vis[-1] == 0:
    return (0, 0)
  else:
    return (1, vis[-1])

def main():
  g = int(input())
  gears = []
  for i in range(g):
    # coords and radius
    x, y, r = map(int, input().split())
    gears.append((x, y, r))

  src = gears[0]
  target = gears[-1]
  # adjacenecy matrix for gears which touch - problem gives that none
  # overlap
  adj = [[0 for i in range(g)] for i in range(g)]

  # create edges
  for i in range(g):
    for j in range(i+1, g):
      a = gears[i]
      b = gears[j]
      dist = hypot(a[0] - b[0], a[1] - b[1])
      # must be exactly tangent, could improve accuracy by keep values
      # as integers instead of floating point
      if a[2] + b[2] == dist:
        adj[i][j] = 1
        adj[j][i] = 1

  # numerator and denominator
  num, denom = rotate(adj, g)
  # possible
  if num == 1:
    # reduce fraction
    divisor = gcd(src[2], target[2])
    # rotation given by denominator
    print(gears[-1][2] // divisor, gears[0][2] * denom // divisor)
  # impossible
  else:
    print(num)

if __name__ == '__main__':
  main()


