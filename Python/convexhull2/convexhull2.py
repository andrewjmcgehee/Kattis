# Rating: ~ 7.5 / 10
# Link: https://open.kattis.com/problems/convexhull2
# Complexity: O(N log(N)) for graham scan
# Memory: O(N) for N points

# helper function for cross product of 3 points
# < 0 indicates clockwise rotation, > 0 indicates counter
# clockwise, 0 indicates collinear
def cross(a, b, c):
  # convert 3 points to 2 vectors u and v
  u = (b[0] - a[0], b[1] - a[1])
  v = (c[0] - b[0], c[1] - b[1])
  return u[0] * v[1] - v[0] * u[1]

def grahamscan(arr):
  # eliminate duplicates if any
  arr = set(arr)
  n = len(arr)

  # if only 1 point no need to scan
  if n == 1:
    return pts

  # sorted by x and then y
  p = sorted(arr)
  # upper hull
  u = []
  # lower hull
  l = []
  for point in p:
    # eliminate counter clockwise for upper hull
    while len(u) > 1 and cross(u[-2], u[-1], point) > 0:
      u.pop()
    # eliminate clockwise for lower hull
    while len(l) > 1 and cross(l[-2], l[-1], point) < 0:
      l.pop()
    l.append(point)
    u.append(point)

  # lower hull end will be upper hull beginning and vice versa
  # also reverses the hull
  hull = l + u[1:-1][::-1]
  return hull

def main():
  n = int(input())
  points = []
  for _ in range(n):
    line = input().split()
    # if line included in the hull
    if line[-1] == 'Y':
      points.append((int(line[0]), int(line[1])))
  # simple way to ensure visited in counterclockwise order
  hull = grahamscan(points)

  print(len(hull))
  for p in hull:
    print(p[0], p[1])

if __name__ == '__main__':
  main()
