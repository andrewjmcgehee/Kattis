# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/getshorty
# Complexity: O(E + V log(V)) for dijkstras
# Memory: O(E) for edge list

# priority queue for dijkstras
from queue import PriorityQueue

def main():
  while True:
    # halls and intersections
    n, m = map(int, input().split())
    if n == m == 0:
      break

    # edge list
    adj = [[] for i in range(n)]
    for i in range(m):
      a, b, weight = map(float, input().split())
      a = int(a)
      b = int(b)
      adj[a].append((weight, b))
      adj[b].append((weight, a))

    q = PriorityQueue()
    # initial weight 1 to get to 0 - weights multiplied by -1 to
    # sort by max value
    q.put((-1, 0))
    visited = [False for i in range(n)]
    # holds best weight to get to vertex i
    path = [0.0 for i in range(n+1)]
    # dijkstras
    while not q.empty():
      weight, target = q.get()
      # better path already found
      if visited[target]:
        continue
      # get actual weight and visit
      weight *= -1
      path[target] = weight
      visited[target] = True
      # try neighbors
      for edge in adj[target]:
        factor = edge[0]
        next_target = edge[1]
        # new weight will be current weight times previous times -1
        q.put((-1*weight*factor, next_target))
    print("%.4f" % path[n-1])


if __name__ == '__main__':
  main()



