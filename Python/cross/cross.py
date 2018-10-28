# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/cross
# Complexity: O(N^2) where N is length of one side of board, each square is considered maximally 9 times
# Memory: O(N^2) to represent board in 2D array

# hatch function as described by description
def hatch(board, target):
  # keep track of valid rows, cols, and squares
  rows = set(range(9))
  cols = set(range(9))
  squares = set(range(9))

  # check each row and col
  for i in range(9):
    for j in range(9):
      if (board[i][j] == str(target)):
        if i in rows:
          rows.remove(i)
        if j in cols:
          cols.remove(j)
        # row major to check for each square
        square = 3*(i // 3) + (j // 3)
        if square in squares:
          squares.remove(square)

  # return None to signify no possible spaces exist
  if len(rows) == 0 or len(cols) == 0:
    return None

  # for each square get available spaces
  for s in squares:
    sq_rows = {x for x in range(3*(s // 3), 3*(s // 3 + 1)) if x in rows}
    sq_cols = {x for x in range(3*(s % 3), 3*(s % 3 + 1)) if x in cols}
    spots = [(r, c) for r in sq_rows for c in sq_cols if board[r][c] == '.']

    # if no spots available then an error has occured because a square was considered legal for the
    # given target yet has no available space to put the target
    if len(spots) == 0:
      return -1
    # should be exactly one space to put the given target value in the square
    if len(spots) == 1:
      return spots[0]
  # otherwise no available moves denoted by None
  return None

def main():
  # use list instead of strings because lists are mutable and strings arent
  board = [list(input()) for x in range(9)]

  while True:
    # will only be set to false is an available move is found
    done = True
    error = False
    # try every number
    for target in range(1, 10):
      square = hatch(board, target)
      # found an error
      if square == -1:
        error = True
        break
      # found an option
      if square is not None:
        done = False
        row, col = square
        board[row][col] = str(target)
    # exhausted options
    if done:
      if error:
        print('ERROR')
      else:
        # print board
        for row in board:
          output = "".join(row)
          print(output)
      break

if __name__ == '__main__':
    main()
