# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/runningmom
# Complexity: O(N) for N vertices
# Memory: O(N) for N vertices

# for processing until EOF
from sys import stdin

# use dfs to detect cycles; only way the MoM can have an infinite
# run away with finite vertices is if a cycle exists
def dfs(city, edges, visited):
  visited.add(city)
  for neighbor in edges[city]:
    if neighbor in visited:
      return True
    visited.add(neighbor)
    if dfs(neighbor, edges, visited):
      return True
    visited.remove(neighbor)
  return False

def main():
  n = int(input())
  edges = dict()
  # build directed graph
  for i in range(n):
    src, dest = input().split()
    if src not in edges:
      edges[src] = []
    # avoid key errors
    if dest not in edges:
      edges[dest] = []
    edges[src].append(dest)
  for line in stdin:
    city = line.strip()
    res = dfs(city, edges, set())
    if res:
      print(city, "safe")
    else:
      print(city, "trapped")

if __name__ == "__main__":
  main()
