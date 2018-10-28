import math

def seg_dist(px, py, x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  if dx == dy == 0:
    return math.hypot(px - x1, py - y1)

  t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)

  if t < 0:
    dx = px - x1
    dy = py - y1
  elif t > 1:
    dx = px - x2
    dy = py - y2
  else:
    near_x = x1 + t * dx
    near_y = y1 + t * dy
    dx = px - near_x
    dy = py - near_y

  return math.hypot(dx, dy)

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    inner = []
    for i in range(n):
      point = tuple(int(x) for x in input().split())
      inner.append(point)

    m = int(input())
    outer = []
    for i in range(m):
      point = tuple(int(x) for x in input().split())
      outer.append(point)

    max_radius = 1000000
    for i in range(m):
      # consider each pairwise line segment
      p0 = outer[i-1]
      p1 = outer[i]
      p0x = p0[0]
      p0y = p0[1]
      p1x = p1[0]
      p1y = p1[1]

      for j in range(n):
        p2 = inner[j-1]
        p3 = inner[j]
        p2x = p2[0]
        p2y = p2[1]
        p3x = p3[0]
        p3y = p3[1]

        # consider normal vectors of each of 4 points
        dist = seg_dist(p0x, p0y, p2x, p2y, p3x, p3y)
        dist = min(dist, seg_dist(p1x, p1y, p2x, p2y, p3x, p3y))
        dist = min(dist, seg_dist(p2x, p2y, p0x, p0y, p1x, p1y))
        dist = min(dist, seg_dist(p3x, p3y, p0x, p0y, p1x, p1y))
        max_radius = min(max_radius, dist)
    print(max_radius / 2)

if __name__ == '__main__':
  main()

