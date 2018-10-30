# Rating: ~ 3.3 / 10
# Link: https://open.kattis.com/problems/walkway
# Complexity: O(E + V log(V)) for dijkstra's
# Memory: O(E)

from queue import PriorityQueue

def main():
  while True:
    # num trapezoids
    n = int(input())
    if n == 0:
      break

    # edge list where index represents side a
    edges = [[] for i in range(1001)]
    for i in range(n):
      a, b, h = map(int, input().split())
      # surface area of the trapezoid times 2 cents per square unit
      weight = 0.02 * h * 0.5 * (a + b)
      # must append edge going in both directions from a to b and b to a
      edges[a].append((weight, b))
      edges[b].append((weight, a))

    start, end = map(int, input().split())
    # trivial case
    if start == end:
      print(0)
      continue

    visited = [False for i in range(1001)]
    # will hold least cost to get to node at index i
    path = [0 for i in range(1001)]
    q = PriorityQueue()
    # 0 cost to get to start size
    q.put((0, start))
    while not q.empty():
      weight, target = q.get()
      # already found least cost path to target
      if visited[target]:
        continue
      # visit it and note its path cost
      visited[target] = True
      path[target] = weight
      # add neighbors
      for edge in edges[target]:
        next_weight = edge[0]
        next_target = edge[1]
        if not visited[next_target]:
          # new weight can be thought of as new edge which is sum of
          # previous weight plus neighbor edge weight
          q.put((next_weight + weight, next_target))
    # least cost path will be stored in index 'end'
    print(path[end])

if __name__ == '__main__':
  main()
