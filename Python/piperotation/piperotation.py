# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/piperotation

def main():
  h, w = map(int, input().split())
  board = [input() for _ in range(h)]
  right = [[False for _ in range(w)] for _ in range(h)]
  down = [[False for _ in range(w)] for _ in range(h)]

  for col in range(w):
    for row in range(h):
      if col > 0:
        r = right[row][col-1]
      else:
        r = False
      if row > 0:
        b = down[row-1][col]
      else:
        b = False
      piece = board[row][col]
      if piece == 'A':
        if r or b:
          print('Impossible')
          return
        right[row][col] = False
        down[row][col] = False
      elif piece == 'B':
        if r == b:
          print('Impossible')
          return
        right[row][col] = r
        down[row][col] = b
      elif piece == 'C':
        right[row][col] = not r
        down[row][col] = not b
      elif piece == 'D':
        if not (r and b):
          print('Impossible')
          return
        right[row][col] = True
        down[row][col] = True
  for col in range(w):
    if down[h-1][col]:
      print('Impossible')
      return
  for row in range(h):
    if right[row][w-1]:
      print('Impossible')
      return
  print('Possible')


if __name__ == "__main__":
  main()
