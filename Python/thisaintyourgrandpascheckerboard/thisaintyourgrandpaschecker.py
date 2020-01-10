# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/thisaintyourgrandpascheckerboard

def main():
  s = int(input())
  board = []
  for _ in range(s):
    board.append(input())
  cols = []
  for j in range(s):
    col = ''
    for i in range(s):
      col += board[i][j]
    cols.append(col)

  for row in board:
    if row.count('W') != row.count('B'):
      print(0)
      return
    if row.find('WWW') != -1 or row.find('BBB') != -1:
      print(0)
      return
  for col in cols:
    if col.count('W') != col.count('B'):
      print(0)
      return
    if col.find('WWW') != -1 or col.find('BBB') != -1:
      print(0)
      return
  print(1)


if __name__ == "__main__":
  main()
