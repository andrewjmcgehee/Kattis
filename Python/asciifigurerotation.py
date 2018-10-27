# Rating: ~ 3.7 / 10
# Link: https://open.kattis.com/problems/asciifigurerotation
# Complexity: O(NK) for an N x K grid
# Memory: O(NK) for an N x K grid

def main():
  # will store all rotated figures
  figs = []
  while True:
    rows = int(input())
    if rows == 0:
      break

    # will store initial board
    board = []
    # num cols will become num of rows
    cols = 0
    for i in range(rows):
      # use list to avoid string immutability
      board.append(list(input()))
      cols = max(cols, len(board[i]))
    # pad with spaces
    for i in range(len(board)):
      while len(board[i]) < cols:
        board[i].append(' ')

    # will store rotated figure
    rotated = []
    for j in range(cols):
      # use stack to pop chars off in appropriate order for new row
      stack = []
      for i in range(rows):
        stack.append(board[i][j])
      rotated.append([])
      while stack:
        char = stack.pop()
        # translate chars that change when rotated
        if char == '|':
          char = '-'
        elif char == '-':
          char = '|'
        rotated[j].append(char)

    for i in range(len(rotated)):
      # trim trailing space
      rotated[i] = ''.join(row[i]).rstrip()
    figs.append('\n'.join(rotated))
  # join avoids adding extra new line
  print('\n\n'.join(figs))

if __name__ == '__main__':
  main()
