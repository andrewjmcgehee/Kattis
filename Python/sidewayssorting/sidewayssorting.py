# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/sidewayssorting

def main():
  first = True
  while True:
    n, m = map(int, input().split())
    if n == m == 0:
      break
    if not first:
      print()
    first = False
    board = []
    for i in range(n):
      board.append(list(input()))

    cols = []
    for i in range(m):
      word = ''.join([board[row][i] for row in range(n)])
      cols.append(word)
    cols.sort(key=lambda x: x.lower())
    for i in range(n):
      line = ''
      for j in range(m):
        line += cols[j][i]
      print(line)


if __name__ == "__main__":
  main()
