# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/george

from collections import defaultdict
from queue import PriorityQueue

def main():
  n, m = map(int, input().split())
  a, b, k, g = map(int, input().split())
  g_path = [int(x) for x in input().split()]

  adj_list = [[] for i in range(1001)]
  times = [0 for i in range(1001)]
  for _ in range(m):
    u, v, w,  = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

  george = dict()
  for i in range(g-1):
    for edge in adj_list[g_path[i]]:
      if edge[0] == g_path[i+1]:
        times[i+1] = times[i] + edge[1]
        george[(g_path[i], g_path[i+1])] = (times[i], times[i+1])
        george[(g_path[i+1], g_path[i])] = (times[i], times[i+1])
        break

  pq = PriorityQueue()
  dist = [-1 for i in range(n+1)]
  dist[a] = k
  pq.put((k, a))
  while not pq.empty():
    current, u = pq.get()
    if current != dist[u]:
      continue
    for edge in adj_list[u]:
      v, w  = edge
      time = current + w
      if (u,v) in george:
        if current >= george[(u,v)][0]:
          time = max(time, george[(u,v)][1] + w)
      if dist[v] == -1 or time < dist[v]:
        dist[v] = time
        pq.put((dist[v], v))
  print(dist[b]-k)

if __name__ == "__main__":
  main()
