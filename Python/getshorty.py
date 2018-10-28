from queue import PriorityQueue

def main():
  while True:
    n, m = map(int, input().split())
    if n == m == 0:
      break

    adj = [[] for i in range(n)]
    for i in range(m):
      a, b, weight = map(float, input().split())
      a = int(a)
      b = int(b)
      adj[a].append((weight, b))
      adj[b].append((weight, a))

    q = PriorityQueue()
    q.put((-1, 0))
    visited = [False for i in range(n)]
    path = [0.0 for i in range(n+1)]
    while not q.empty():
      weight, target = q.get()
      if visited[target]:
        continue
      weight *= -1
      path[target] = weight
      visited[target] = True
      for edge in adj[target]:
        factor = edge[0]
        next_target = edge[1]
        q.put((-1*weight*factor, next_target))
    print("%.4f" % path[n-1])


if __name__ == '__main__':
  main()



