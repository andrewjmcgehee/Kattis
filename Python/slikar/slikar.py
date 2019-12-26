# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/slikar

from collections import deque

steps = ((1,0), (-1,0), (0,1), (0,-1))

def main():
  rows, cols = map(int, input().split())
  board = []
  for i in range(rows):
    board.append(input())

  start = None
  flood = deque()
  q = deque()
  flooded = [[1e9 for i in range(cols)] for j in range(rows)]
  times = [[1e9 for i in range(cols)] for j in range(rows)]
  for r in range(rows):
    for c in range(cols):
      if board[r][c] == '*':
        flood.append((r, c, 0))
        flooded[r][c] = 0
      elif board[r][c] == 'S':
        start = (r, c)

  while flood:
    r, c, t = flood.popleft()
    for x, y in steps:
      if r+x < rows and r+x >= 0 and c+y < cols and c+y >= 0:
        next_r, next_c = r+x, c+y
        if flooded[next_r][next_c] == 1e9 and board[next_r][next_c] == '.':
          flooded[next_r][next_c] = t+1
          flood.append((next_r, next_c, t+1))

  time = 1e9
  q.append((start[0], start[1], 0))
  times[start[0]][start[1]] = 0
  while q:
    r, c, t = q.popleft()
    if board[r][c] == 'D':
      time = t
      break
    for x, y in steps:
      if r+x < rows and r+x >= 0 and c+y < cols and c+y >= 0:
        next_r, next_c = r+x, c+y
        if times[next_r][next_c] == 1e9 and board[next_r][next_c] in {'.','D'} and t+1 < flooded[next_r][next_c]:
          times[next_r][next_c] = t+1
          q.append((next_r, next_c, t+1))
  if time == 1e9:
    print('KAKTUS')
  else:
    print(time)


if __name__ == "__main__":
  main()
