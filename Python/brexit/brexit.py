# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/brexit

import math
from collections import deque

def main():
  global groups
  c, p, x, l = map(int, input().split())

  adj = dict()
  for i in range(p):
    a, b = map(int, input().split())
    if a not in adj:
      adj[a] = []
    adj[a].append(b)
    if b not in adj:
      adj[b] = []
    adj[b].append(a)

  seen = dict()
  for v in adj:
    seen[v] = math.ceil(len(adj[v]) / 2)

  seen[l] = 0
  queue = deque([l])
  while queue:
    current = queue.popleft()
    for edge in adj[current]:
      seen[edge] -= 1
      if seen[edge] == 0:
        queue.append(edge)

  if seen[x] <= 0:
    print('leave')
  else:
    print('stay')

if __name__ == "__main__":
  main()
