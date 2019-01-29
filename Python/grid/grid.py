# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/grid
# Complexity: O(NK) for an NxK grid
# Memory: O(NK) for an NK grid and the BFS queue

# helper function to return candidate neighbors given a jump length
def get_neighbors(r, c, jump, grid):
  neighbors = []
  if r - jump >= 0:
    neighbors.append((r-jump, c))
  if r + jump < len(grid):
    neighbors.append((r+jump, c))
  if c - jump >= 0:
    neighbors.append((r, c-jump))
  if c + jump < len(grid[0]):
    neighbors.append((r, c+jump))
  return neighbors

def main():
  row, col = map(int, input().split())

  # get grid
  grid = []
  for i in range(row):
    grid.append(input())

  # start location of BFS
  start = (0, 0)
  # using none as sentinel value to determine depth of BFS
  q = [start, None]
  # flag for valid path found
  found = False
  # keep track of visited locations
  visited = set()
  visited.add(start)
  path_length = 0
  # target
  end = (row-1, col-1)

  # BFS
  while q:
    # pop head of q
    loc = q[0]
    del q[0]

    # entered new level of BFS
    if loc is None:
      # if q is non-empty then candidate paths still exist
      if q:
        q.append(None)
        path_length += 1
        continue
      # otherwise no candidates remain
      else:
        break
    # found it
    if loc == end:
      found = True
      break

    # row column
    r, c = loc
    jump = int(grid[r][c])
    # check neighbors
    for neighbor in get_neighbors(r, c, jump, grid):
      if neighbor not in visited:
        q.append(neighbor)
        visited.add(neighbor)
  # if not found, print -1
  if found:
    print(path_length)
  else:
    print(-1)

if __name__ == "__main__":
  main()
