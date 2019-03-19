# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/crosscountry
# Complexity: O(V log(E)) for dijkstras
# Memory: O(E) for E edges

from queue import PriorityQueue

def main():
  n, s, t = map(int, input().split())

  # read in adjacency matrix
  adj = [[int(x) for x in input().split()] for i in range(n)]

  pq = PriorityQueue()
  # zero weight to get to start
  pq.put((0, s))
  # track visited
  visited = set()

  while not pq.empty():
    weight, target = pq.get()
    # visit
    visited.add(target)
    # found it
    if target == t:
      print(weight)
      break
    # check neighbors
    for j in range(n):
      if j not in visited:
        # must sum previous weight for next candidate
        pq.put((weight + adj[target][j], j))


if __name__ == "__main__":
  main()
