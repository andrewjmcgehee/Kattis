# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/chess
# Complexity: O(N) for N diagonal squares
# Memory: O(N^2) to represent square board and map to indices

def main():
  # map coordinate to an index
  to_index = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    '8': 0,
    '7': 1,
    '6': 2,
    '5': 3,
    '4': 4,
    '3': 5,
    '2': 6,
    '1': 7
  }
  # map row number from index
  row_from_index = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1'
  }
  # map col letter from index
  col_from_index = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H'
  }

  n = int(input())
  for i in range(n):
    # get inputs
    move = input().split()
    row0 = to_index[move[1]]
    col0 = to_index[move[0]]
    rowF = to_index[move[3]]
    colF = to_index[move[2]]

    # calculate over all translation
    delta_row = abs(rowF - row0)
    delta_col = abs(colF - col0)
    possible = True

    # delta row and delta col must be of same parity
    if not ((delta_row % 2 == 0 and delta_col % 2 == 0)
        or (delta_row % 2 == 1 and delta_col % 2 == 1)):
      possible = False

    if not possible:
      print('Impossible')
      continue
    else:
      # are same square
      if row0 == rowF and col0 == colF:
        print('0 ' + col_from_index[col0]
             + ' ' + row_from_index[row0])
        continue
      # are already diagonal - 1 move
      elif (abs(rowF - row0) == abs(colF - col0)):
        print('1 ' + col_from_index[col0]
             + ' ' + row_from_index[row0]
             + ' ' + col_from_index[colF]
             + ' ' + row_from_index[rowF])
      # can always be done in 2 moves or less
      else:
        found = False
        for i in range(8):
          for j in range(8):
            if ((abs(row0 - i) == abs(col0 - j))
                and (abs(rowF - i) == abs(colF - j))):
              found = True
              rowM = i
              colM = j
              break
          if found:
            break
        # create output
        moves = [
          col_from_index[col0],
          row_from_index[row0],
          col_from_index[colM],
          row_from_index[rowM],
          col_from_index[colF],
          row_from_index[rowF]
        ]

        print('2', ' '.join(moves))

if __name__ == '__main__':
    main()
