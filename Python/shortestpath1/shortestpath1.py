# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/shortestpath1
# Complexity: O(E log(E)) for dijkstras with edge list
# Memory: O(E) for E edges

from queue import PriorityQueue

def main():
  # store final outputs
  outputs = []
  while True:
    n, m, q, s = map(int, input().split())
    # exit condition
    if n == m == q == s == 0:
      break
    # created edge list
    adj = {i:[] for i in range(n)}
    for i in range(m):
      u, v, w = map(int, input().split())
      adj[u].append((w, v))
    # all paths initially -1 which signifies impossible
    path = [-1 for i in range(n)]
    pq = PriorityQueue()
    # 0 weight to get from source to itself
    pq.put((0, s))
    visited = set()
    # dijkstras
    while not pq.empty():
      weight, target = pq.get()
      if target in visited:
        continue
      visited.add(target)
      path[target] = weight
      for j in adj[target]:
        w, going_to = j
        if going_to not in visited:
          pq.put((weight + w, going_to))
    # handle queries
    out = []
    for query in range(q):
      target = int(input())
      if path[target] != -1:
        out.append(str(path[target]))
      else:
        out.append('Impossible')
    # store each query as its own contained output
    outputs.append('\n'.join(out))
  # join by new lines
  print('\n\n'.join(outputs))

if __name__ == "__main__":
  main()
