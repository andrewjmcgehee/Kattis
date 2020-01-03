# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/jurassicjigsaw

class UF:
  def __init__(self, n):
    self.uf = [-1 for i in range(n)]

  def find(self, x):
    if self.uf[x] < 0:
      return x
    self.uf[x] = self.find(self.uf[x])
    return self.uf[x]

  def union(self, x, y):
    x_root = self.find(x)
    y_root = self.find(y)
    if x_root == y_root:
      return 0
    if self.uf[y_root] < self.uf[x_root]:
      self.uf[y_root] += self.uf[x_root]
      self.uf[x_root] = y_root
    else:
      self.uf[x_root] += self.uf[y_root]
      self.uf[y_root] = x_root
    return 1

  def components(self):
    comps = []
    cid = [-1 for i in range(len(self.uf))]
    for i in range(len(self.uf)):
      root = self.find(i)
      if cid[root] == -1:
        cid[root] = len(comps)
        comps.append([])
      comps[cid[root]].append(i)
    return comps

def main():
  n, k = map(int, input().split())
  s = []
  edges = []
  for i in range(n):
    s.append(input())
    for j in range(i):
      cost = 0
      for l in range(k):
        if s[i][l] != s[j][l]:
          cost += 1
      edges.append((cost, i, j))
  uf = UF(n)
  edges.sort()

  cost = 0
  pairs = []
  for e in edges:
    w, u, v = e
    if uf.union(u, v):
      cost += w
      pairs.append((u, v))
  print(cost)
  for p in pairs:
    print(p[1], p[0])

if __name__ == "__main__":
  main()
