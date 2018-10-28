# Rating: ~ 3.6 / 10
# Link: https://open.kattis.com/problems/elevatortrouble
# Complexity: O(N) for N nodes in BFS
# Memory: O(N) for N floors

INF = (1 << 62)

def main():
  # floors, start, goal, up, down
  f, s, g, u, d = map(int, input().split())
  # correct for 0 indexing
  s -= 1
  g -= 1

  # visited array which tracks the order of floors visited
  vis = [INF for i in range(f)]
  vis[s] = 0

  # queue
  q = []
  q.append(s)
  while q:
    # pythonic way of implementing queue
    floor = q[0]
    del q[0]

    # if the visited array at the target floor is < 1 + the visited array at the current floor
    # it indicates we already found a shorter path to that floor
    # try up
    if floor + u < f and vis[floor] + 1 < vis[floor+u]:
      vis[floor+u] = vis[floor] + 1
      q.append(floor+u)
    # try down
    if floor - d >= 0 and vis[floor] + 1 < vis[floor-d]:
      vis[floor-d] = vis[floor] + 1
      q.append(floor-d)
  # if goal is still infinite, we never made it
  if vis[g] == INF:
    print('use the stairs')
    return
  print(vis[g])

if __name__ == '__main__':
  main()
