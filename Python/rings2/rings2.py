# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/rings2
# Complexity: O(NK) for an N x K grid
# Memory: O(NK) for an N x K grid

# helper function for getting valid cardinal neighbors
def get_neighbors(r, c, grid):
  # no need to store duplicates
  neighbors = set()
  if r-1 >= 0:
    neighbors.add(grid[r-1][c])
  if c-1 >= 0:
    neighbors.add(grid[r][c-1])
  if r+1 < len(grid):
    neighbors.add(grid[r+1][c])
  if c+1 < len(grid[0]):
    neighbors.add(grid[r][c+1])
  return neighbors


def main():
  # get dimensions
  r, c = map(int, input().split())

  # pad the grid with zeroes (eliminates first ring edge / corner cases)
  # leading row of zeroes
  grid = [[0] * (c+2)]
  # bounds change from 0 to r-1 to 1 to r inclusive
  for i in range(1, r+1):
    grid.append([])
    # leading zero
    grid[i].append(0)
    line = input()
    for j in range(c):
      # convert empty space to 0
      if line[j] == '.':
        grid[i].append(0)
      else:
        grid[i].append('T')
    # trailing zero
    grid[i].append(0)
  # trailing row of zeroes
  grid.append([0] * (c+2))

  # flag to track if there are any remaining T's
  finished = False
  # counter to track ring depth
  ring = 0
  while not finished:
    finished = True
    for i in range(r+2):
      for j in range(c+2):
        # no need to process already determined numbers
        if grid[i][j] == 'T':
          finished = False
          neighbors = get_neighbors(i, j, grid)
          # found an outermost T
          if ring in neighbors:
            grid[i][j] = ring + 1
    # don't increase ring if no T's found
    if not finished:
      ring += 1

  ans = []
  # remove padding
  for i in range(1, r+1):
    ans.append(grid[i][1:c+1])

  # convert 0s and format
  for i in range(r):
    for j in range(c):
      # formatting condition for more than 9 rings
      if ring >= 10:
        if ans[i][j] == 0:
          ans[i][j] = '...'
        # double digit number
        elif ans[i][j] > 9:
          ans[i][j] = '.' + str(ans[i][j])
        # single digit number
        else:
          ans[i][j] = '..' + str(ans[i][j])
      else:
        if ans[i][j] == 0:
          ans[i][j] = '..'
        else:
          ans[i][j] = '.' + str(ans[i][j])
  # concatenate rows
  for row in ans:
    print(''.join(row))

if __name__ == "__main__":
  main()
