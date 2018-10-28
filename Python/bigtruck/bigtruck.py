# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/bigtruck
# Complexity: O(V^2) for dijkstra's
# Memory: O(V^2) for adjacency matrix

from queue import PriorityQueue
INF = -1

def main():
  # vertices
  m = int(input())
  # number of items at each stop
  items = [int(x) for x in input().split()]
  # num edges
  n = int(input())
  # adjacency matrix initially unconnected
  adj = [[INF for j in range(m)] for i in range(m)]
  # a and b must be converted to 0 index
  for i in range(n):
    a, b, weight = map(int, input().split())
    a -= 1
    b -= 1
    # symmetric
    adj[a][b] = weight
    adj[b][a] = weight

  q = PriorityQueue()
  # will hold the optimal path at the end
  path = [0 for i in range(m)]
  # will hold the optimal amount of items at the end
  max_items = [0 for i in range(m)]
  visited = set()
  # sort by weight, then by max number of items
  # multiply by -1 to sort maximum weights
  q.put((0, -1 * items[0], 0))
  while not q.empty():
    weight, num_items, target = q.get()
    num_items *= -1
    if target in visited:
      continue
    # reached the end
    if target == m-1:
      path[target] = weight
      max_items[target] = num_items
      # add target to visited as a flag to detect impossible path
      visited.add(m-1)
      break

    path[target] = weight
    max_items[target] = num_items
    visited.add(target)
    # add neighbor edges
    for i in range(m):
      if adj[target][i] != INF and i not in visited:
        # adding sum of path up to hear plus new weight
        # same for items
        q.put((adj[target][i] + weight, -1 * (items[i] + num_items), i))
  # we didn't get to target
  if m-1 not in visited:
    print('impossible')
  else:
    print(path[m-1], max_items[m-1])

if __name__ == '__main__':
  main()
