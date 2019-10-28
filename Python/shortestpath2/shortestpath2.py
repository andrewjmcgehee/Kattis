# Rating: ~ 4.0 / 10
# Link: https://open.kattis.com/problems/shortestpath2

import heapq
from collections import defaultdict, deque
import sys

def main():
  out = []
  data = deque([line.strip() for line in sys.stdin.readlines()])
  while True:
    n, m, queries, s = map(int, data.popleft().split())
    if n == m == queries == s == 0:
      break
    adj = defaultdict(list)
    best = dict()
    for i in range(m):
      u, v, t, P, d = map(int, data.popleft().split())
      adj[u].add((v, t, P, d))
    q = []
    heapq.heappush(q, (0, s))
    while len(best) < n and q:
      time, target = heapq.heappop(q)
      if target in best and best[target] <= time:
        continue
      best[target] = time
      for edge in adj[target]:
        next_node, t, P, d = edge
        next_time = time
        if time < t:
          next_time = t
        elif P == 0:
          if time != t:
            continue
        elif (time - t) % P != 0:
          offset = P - ((time - t) % P)
          next_time = time + offset
        if edge in best and best[other] <= next_time:
          continue
        heapq.heappush(q, (next_time + d, next_node))
    for i in range(queries):
      end = int(data.popleft())
      if end not in best:
        out.append('Impossible\n')
      else:
        out.append(str(best[end]) + '\n')
    out.append('\n')
  print(''.join(out).strip())

if __name__ == "__main__":
  main()
