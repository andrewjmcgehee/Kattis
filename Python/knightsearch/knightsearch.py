# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/knightsearch
# Complexity: O(V) where V is number of vertices in graph
# Memory: O(NK) for a board N x K

# globals
board = []
TARGET = "ICPCASIASG"
found = False

# helper function for getting neighbors
# checks all L shaped moves for bounds
def get_neighbors(row, col):
  global board
  neighbors = []
  if row-1 >= 0:
    if col-2 >= 0:
      neighbors.append((row-1, col-2))
    if col+2 < len(board):
      neighbors.append((row-1, col+2))
  if row-2 >= 0:
    if col-1 >= 0:
      neighbors.append((row-2, col-1))
    if col+1 < len(board):
      neighbors.append((row-2, col+1))
  if row+1 < len(board):
    if col-2 >= 0:
      neighbors.append((row+1, col-2))
    if col+2 < len(board):
      neighbors.append((row+1, col+2))
  if row+2 < len(board):
    if col-1 >= 0:
      neighbors.append((row+2, col-1))
    if col+1 < len(board):
      neighbors.append((row+2, col+1))
  return neighbors

def dfs(index, row, col):
  global TARGET, board, found
  # if we are at the last letter, we found a path
  if index >= len(TARGET)-1:
    found = True
    return

  # character we are trying to reach
  target = TARGET[index+1]
  neighbors = get_neighbors(row, col)
  # only try neighbors that are actually equal to target
  for neighbor in neighbors:
    new_row, new_col = neighbor
    if board[new_row][new_col] == target:
      dfs(index+1, neighbor[0], neighbor[1])


def main():
  global board, found
  row_size = input()
  # row major board
  line = raw_input()
  # build board
  board = []
  for i in xrange(row_size):
    board.append(line[row_size*i:row_size*(i+1)])

  for i in xrange(len(line)):
    # must start on I
    if line[i] == "I":
      # row major conversion to row col
      row = i // row_size
      col = i % row_size
      dfs(0, row, col)
      if found:
        break
  if found:
    print "YES"
    return
  print "NO"

if __name__ == '__main__':
  main()
