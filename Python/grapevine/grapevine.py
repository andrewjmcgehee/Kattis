# Rating: ~ 7.3 / 10
# Link: https://open.kattis.com/problems/grapevine

from sys import stdin, stdout
from collections import deque

def main():
  lines = deque(stdin.readlines())
  n, m, d = map(int, lines.popleft().strip().split())
  skeptical = dict()
  edges = dict()

  # add skepticism of each person
  for _ in range(n):
    name, weight = lines.popleft().strip().split()
    skeptical[name] = int(weight)
    edges[name] = []

  # add edges
  for _ in range(m):
    a, b = lines.popleft().strip().split()
    edges[a].append(b)
    edges[b].append(a)

  # modified bfs / max flow
  start = lines.pop().strip()
  spreading = deque([start])
  visited = {start}
  for _ in range(d):
    # everyone that is convinced will become new source
    convinced = []
    while spreading:
      # all who are spreading tell everyone in their edge list
      name = spreading.popleft()
      for neighbor in edges[name]:
        visited.add(neighbor)
        skeptical[neighbor] -= 1
        if skeptical[neighbor] == 0:
          convinced.append(neighbor)
    spreading = deque(convinced)
  print(len(visited) - 1)


if __name__ == "__main__":
  main()
