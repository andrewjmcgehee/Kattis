# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/okvir

def main():
  n, m = map(int, input().split())
  u, l, r, d = map(int, input().split())

  board = [['' for j in range(m + l + r)] for i in range(n + u + d)]
  for i in range(n + u + d):
    for j in range(m + l + r):
      if (i + j) & 1:
        board[i][j] = '.'
      else:
        board[i][j] = '#'
  for i in range(u, u+n):
    word = input()
    for j in range(m):
      board[i][l+j] = word[j]
  print('\n'.join([''.join(row) for row in board]))


if __name__ == "__main__":
  main()
