# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/countingstars
# Complexity: O(NK log(NK)) where N and K and dimensions of the board - union find has logarithmic time
# Memory: O(NK) where N and K are dimensions of the board

class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]

  def union(self, x, y):
    self.parent[self.find(x)] = self.find(y)

  def find(self, x):
    if self.parent[x] == x:
      return x
    self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

# helper function to check board bounds
def is_safe(i, j, board):
  n = len(board)
  m = len(board[0])
  if i < 0 or j < 0:
    return False
  if i >= n or j >= m:
    return False
  return True

def main():
  case = 1
  # handle EOF input
  while True:
    try:
      n, m = map(int, input().split())
      size = n * m
      # total size of uf is total 'area' of board
      uf = UnionFind(size)

      board = []
      for i in range(n):
        # strings behave as immutable arrays
        board.append(input())

      for i in range(n):
        for j in range(m):
          if board[i][j] == '-':
            # row major index form
            current = i*m + j
            # check neighbors and union if same type
            if is_safe(i-1, j, board) and board[i-1][j] == '-':
              uf.union(current, (i-1)*m + j)
            if is_safe(i+1, j, board) and board[i+1][j] == '-':
              uf.union(current, (i+1)*m + j)
            if is_safe(i, j-1, board) and board[i][j-1] == '-':
              uf.union(current, i*m + (j-1))
            if is_safe(i, j+1, board) and board[i][j+1] == '-':
              uf.union(current, i*m + (j+1))

      # eliminate duplicates
      components = set()
      for i in range(n):
        for j in range(m):
          if board[i][j] == '-':
            # get representative element of star and add to set
            components.add(uf.find(i*m + j))
      print("Case %i: %i" % (case, len(components)))
      case += 1
    except EOFError:
      break

if __name__ == '__main__':
  main()





