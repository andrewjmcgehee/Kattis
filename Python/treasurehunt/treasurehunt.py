# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/treasurehunt
# Complexity: O(NK) for an N x K map
# Memory: O(NK) for an N x K map

def main():
  # get dimensions
  rows, cols = map(int, input().split())
  treasure_map = []
  steps = 0
  # current row
  r = 0
  # current col
  c = 0
  # visited set of tuples (row, column)
  vis = set()
  vis.add((0, 0))

  # build map
  for i in range(rows):
    treasure_map.append(input())

  # try to follow the path
  while True:
    if treasure_map[r][c] == 'N':
      r -= 1
    elif treasure_map[r][c] == 'S':
      r += 1
    elif treasure_map[r][c] == 'W':
      c -= 1
    elif treasure_map[r][c] == 'E':
      c += 1
    # found treasure
    elif treasure_map[r][c] == 'T':
      print(steps)
      break
    # out of bounds
    if r < 0 or c < 0 or r >= rows or c >= cols:
      print('Out')
      break
    # found cycles
    if (r, c) in vis:
      print('Lost')
      break
    steps += 1
    vis.add((r, c))

if __name__ == '__main__':
  main()

