from math import gcd, hypot

def rotate(adj, n):
  comp = [0 for i in range(n)]
  q = [0]
  comp[0] = 1
  while q:
    current = q.pop(0)
    for i in range(n):
      if adj[current][i]:
        if comp[i] * comp[current] == 1:
          return (-1, -1)
        if comp[i] == 0:
          q.append(i)
          comp[i] = -1 * comp[current]
  if comp[-1] == 0:
    return (0, 0)
  else:
    return (1, comp[-1])

def main():
  g = int(input())
  uf = [i for i in range(g)]
  gears = []
  for i in range(g):
    x, y, r = map(int, input().split())
    gears.append((x, y, r))

  src = gears[0]
  target = gears[-1]
  adj = [[0 for i in range(g)] for i in range(g)]

  for i in range(g):
    for j in range(i+1, g):
      a = gears[i]
      b = gears[j]
      dist = hypot(a[0] - b[0], a[1] - b[1])
      if a[2] + b[2] == dist:
        adj[i][j] = 1
        adj[j][i] = 1

  a, b = rotate(adj, g)

  if a == 1:
    divisor = gcd(src[2], target[2])
    print(gears[-1][2] // divisor, gears[0][2] * b // divisor)
  else:
    print(a)

if __name__ == '__main__':
  main()


