# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/rafting
# Complexity: O(NK) for N inner points and K outer points
# Memory: O(N + K) for N inner points and K outer points

import math

# distance from a point p to a line segment
def seg_dist(px, py, x1, y1, x2, y2):
  # line segment x component
  x = x2 - x1
  # line segment y component
  y = y2 - y1
  # the line segment is a point, return distance between points
  if x == y == 0:
    return math.hypot(px - x1, py - y1)
  # first vector
  ux, uy = (px - x1, py - y1)
  # second vector
  vx, vy = (x, y)
  # projection of vector onto another vector
  scalar = (ux * vx + uy * vy) / (vx**2 + vy**2)

  # projection is outside point 1
  if scalar < 0:
    dx = ux
    dy = uy
  # projection is outside point 2
  elif scalar > 1:
    dx = px - x2
    dy = py - y2
  # projection is inside the two points - get normal vector
  else:
    near_x = x1 + scalar * x
    near_y = y1 + scalar * y
    dx = px - near_x
    dy = py - near_y
  return math.hypot(dx, dy)

def main():
  t = int(input())
  for _ in range(t):
    # num points
    n = int(input())

    # get inner boundaries
    inner = []
    for i in range(n):
      point = tuple(int(x) for x in input().split())
      inner.append(point)
    # get outer boundaries
    m = int(input())
    outer = []
    for i in range(m):
      point = tuple(int(x) for x in input().split())
      outer.append(point)

    # start with impossibly high value
    max_diameter = 1000000
    for i in range(m):
      # consider each outer line segment
      # always safe in python because of negative indexes
      p0x, p0y = outer[i-1]
      p1x, p1y = outer[i]

      # get closest point on each inner line segment
      for j in range(n):
        p2x, p2y = inner[j-1]
        p3x, p3y = inner[j]

        # consider distances for each of the 4 points
        dist = seg_dist(p0x, p0y, p2x, p2y, p3x, p3y)
        dist = min(dist, seg_dist(p1x, p1y, p2x, p2y, p3x, p3y))
        dist = min(dist, seg_dist(p2x, p2y, p0x, p0y, p1x, p1y))
        dist = min(dist, seg_dist(p3x, p3y, p0x, p0y, p1x, p1y))
        max_diameter = min(max_diameter, dist)
    print(max_diameter / 2)

if __name__ == '__main__':
  main()

