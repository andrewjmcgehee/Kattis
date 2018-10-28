# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/4thought
# Complexity: O(N^2) for N queens due to checking pair-wise relationhips
# Memory: O(1) for an 8 by 8 board

def main():
  # get board
  board = [input() for x in range(8)]

  # array of tuples that repesent x, y coords
  queens = []
  num_queens = 0
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == '*':
        queens.append((i, j))
        num_queens += 1

  valid = True
  # quick check
  if num_queens != 8:
    valid = False

  if valid:
    for i in range(len(queens)):
      for j in range(i+1, len(queens)):
        # share the same row
        if queens[i][0] == queens[j][0]:
          valid = False
          break
        # share the same column
        if queens[i][1] == queens[j][1]:
          valid = False
          break
        # are diagonal if and only if same distance x and y apart
        if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
          valid = False
          break
      if not valid:
        break

  if valid:
    print('valid')
  else:
    print('invalid')

if __name__ == '__main__':
    main()
