# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/humancannonball

import math
from queue import PriorityQueue

class Node:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def get_time(start, end, nodes):
  dist = math.hypot(nodes[start].x-nodes[end].x, nodes[start].y-nodes[end].y)
  if start == 0:
    return dist / 5
  else:
    return 2 + abs(dist-50) / 5

def main():
  ax, ay = map(float, input().split())
  bx, by = map(float, input().split())
  if ax == bx and ay == by:
    print(0)
    return

  n = int(input())
  nodes = [None] * (n+2)
  nodes[0] = Node(ax, ay)
  nodes[-1] = Node(bx, by)
  for i in range(1, n+1):
    x, y = map(float, input().split())
    node = Node(x, y)
    nodes[i] = node

  pq = PriorityQueue()
  visited = set()
  pq.put((0,0))
  while not pq.empty():
    curr_time, curr_node = pq.get()
    if curr_node == len(nodes)-1:
      time = curr_time
      break
    if curr_node not in visited:
      visited.add(curr_node)
      for i in range(len(nodes)):
        if curr_node != i:
          ntime = get_time(curr_node, i, nodes) + curr_time
          pq.put((ntime, i))
  print(time)


if __name__ == "__main__":
  main()
