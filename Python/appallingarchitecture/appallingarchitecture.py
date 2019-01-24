# Rating: ~ 3.7 / 10
# Link: https://open.kattis.com/problems/appallingarchitecture
# Complexity: O(NK) for an N x K grid
# Memory: O(NK) for an N x K grid

def main():
  # get dimensions
  r, c = map(int, input().split())
  # build grid
  grid = []
  for i in range(r):
    grid.append(input())

  # used for calculating center of mass
  total_mass = 0
  # non-empty blocks
  blocks = {'/', '\\', '-', '_', '#', '|'}

  # only concerned with the center with respect to columns
  cog_col = 0
  for i in range(r):
    for j in range(c):
      if grid[i][j] in blocks:
        # increase total mass
        total_mass += 1
        # this blocks center is at j + 0.5
        cog_col += j + 0.5

  # formula for center of mass
  cog_col /= total_mass

  # find left most and right most ground
  left_most = None
  right_most = None
  for i, block in enumerate(grid[-1]):
    # must be non-empty
    if block in blocks:
      # first encountered
      if left_most is None:
        left_most = i
      if right_most is None:
        right_most = i
      # minimize left most and maximize right most
      left_most = min(left_most, i)
      right_most = max(right_most, i)

  # strictly less than for left most
  if cog_col < left_most:
    print('left')
  elif cog_col < right_most + 1:
    print('balanced')
  # add one because the index counts as 1 'entire' block
  else:
    print('right')


if __name__ == "__main__":
  main()
