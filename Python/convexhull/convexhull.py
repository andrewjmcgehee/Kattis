# Rating: ~ 6.0 / 10
# Link: https://open.kattis.com/problems/convexhull
# Complexity: O(N log(N)) for graham scan
# Memory: O(N) for N points

# helper function for cross product of three points
# gives rotation. > 0 indicates counter clockwise, < 0 indicates
# clockwise, 0 indicates collinear
def cross(a, b, c):
  # calculate u and v vectors
  u = (b[0] - a[0], b[1] - a[1])
  v = (c[0] - b[0], c[1] - b[1])
  return u[0] * v[1] - u[1] * v[0]

def grahamscan(arr):
  # eliminate duplicate points if any
  arr = set(arr)
  n = len(arr)

  # for < 3 points no need for scan
  if n <= 2:
    return arr

  # points sorted by x and then y
  p = sorted(arr)
  # beginning of upper hull
  u = [p[0], p[1]]
  # beginning of lower hull
  l = [p[-1], p[-2]]

  # eliminate all counter clockwise and collinear
  for i in range(2, n):
    while len(u) > 1 and cross(p[i], u[-1], u[-2]) >= 0:
      u.pop()
    u.append(p[i])
  for i in range(n-2, -1, -1):
    while len(l) > 1 and cross(p[i], l[-1], l[-2]) >= 0:
      l.pop()
    l.append(p[i])

  # end of upper hull will be beginning of lower hull and vice versa
  hull = u[:-1] + l[:-1]
  # reverse hull
  hull[::-1]
  return hull

def main():
  while True:
    num_points = int(input())
    if num_points == 0:
      break
    points = []
    for i in range(num_points):
      x, y = map(int, input().split())
      points.append((x, y))

    # find hull
    hull = grahamscan(points)

    print(len(hull))
    for x, y in hull:
      print(x, y)

if __name__ == '__main__':
  main()
