# Rating: ~ 5.5 / 10
# Link: https://open.kattis.com/problems/10kindsofpeople
# Complexity: O(N log(N)) due to union find and where N is number of cells in row-major form
# Memory: O(Rows * Columns) for union find in row-major form

import sys
sys.setrecursionlimit(10**6)

# light weight union find representation
def unite(uf, x, y):
  xroot = find(uf, x)
  yroot = find(uf, y)
  if xroot == yroot:
    return
  uf[xroot] = yroot

def find(uf, x):
  if uf[x] == x:
    return x
  uf[x] = find(uf, uf[x])
  return uf[x]

def main():
  row, col = map(int, input().split())
  uf = [i for i in range(row * col)]
  board = []

  # build board
  for i in range(row):
    board.append(input())

  # unite all elements of same type
  for i in range(row):
    for j in range(col):
      if j < col - 1 and board[i][j] == board[i][j+1]:
        unite(uf, i*col + j, i*col + j+1)
      if i < row - 1 and board[i][j] == board[i+1][j]:
        unite(uf, i*col + j, (i+1)*col + j)

  # queries have a path between them if they return the same representative
  # element

  m = int(input())
  for _ in range(m):
    r1, c1, r2, c2 = [int(x)-1 for x in input().split()]

    if find(uf, r1*col + c1) == find(uf, r2*col + c2):
      if board[r1][c1] == '1':
        print('decimal')
      else:
        print('binary')
    else:
      print('neither')

if __name__ == '__main__':
  main()
