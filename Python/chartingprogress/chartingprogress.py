# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/chartingprogress
# Complexity: O(NK) for a board that is N x K
# Memory: O(NK) for a board that is N x K

import fileinput

# helper function to determine number of asterisks in a row
def count_asts(row):
  count = 0
  for item in row:
    if item == '*':
      count += 1
  return count

def main():
  # will hold all results to print at end
  charts = [[]]
  fig_num = 0
  for line in fileinput.input():
    # new line denotes new figure
    if line.isspace():
      charts.append([])
      fig_num += 1
      continue
    # regular row
    charts[fig_num].append(list(line.strip()))

  # shift all the asterisks as far right as possible
  for index, board in enumerate(charts):
    # pointer keeping track of max right index in previous row
    max_right = len(board[0])
    for i in range(len(board)):
      num_asts = count_asts(board[i])
      # place to begin asterisks is max right minus the number of asterisks
      # in the row
      start = max_right - num_asts
      for j in range(len(board[i])):
        # only the indices in the range should be asterisks; all others
        # should become dots
        if j >= start and j < max_right:
          board[i][j] = '*'
        else:
          board[i][j] = '.'
      # update max right
      max_right -= num_asts
      # join into string
      board[i] = ''.join(board[i])
    # join into coniguous figure
    charts[index] = '\n'.join(board)
  # join final new line separated figures
  print('\n\n'.join(charts))


if __name__ == '__main__':
  main()
