# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/prozor

import sys

def main():
  data = sys.stdin.readlines()
  r, s, k = map(int, data.pop(0).strip().split())
  data = [list(line.strip()) for line in data]
  best_start = (0, 0)
  best_flies = 0
  # scan window
  for i in range(r-k+1):
    for j in range(s-k+1):
      num_flies = 0
      # strictly inside swatter
      for x in range(1, k-1):
        for y in range(1, k-1):
          if data[i+x][j+y] == '*':
            num_flies += 1
      if num_flies > best_flies:
        best_start = (i, j)
        best_flies = num_flies
  # handle output
  r, c = best_start
  data[r][c] = '+'
  data[r][c+k-1] = '+'
  data[r+k-1][c] = '+'
  data[r+k-1][c+k-1] = '+'
  for i in range(r+1, r+k-1):
    data[i][c] = '|'
    data[i][c+k-1] = '|'
  for i in range(c+1, c+k-1):
    data[r][i] = '-'
    data[r+k-1][i] = '-'
  print(best_flies)
  print('\n'.join([''.join(line) for line in data]))


if __name__ == "__main__":
  main()
