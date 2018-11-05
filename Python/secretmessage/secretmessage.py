# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/secretmessage
# Complexity: O(N) for N characters in message
# Memory: O(N) for N characters in message

def encrypt(message):
  length = len(message)
  side = 1
  # find side length of square board
  while side**2 < length:
    side += 1
  # create initial board
  board = []
  for i in range(side):
    # get side length chunks of string
    board.append(list(message[i*side:(i+1)*side]))
  # pad final row with *
  while len(board[-1]) < side:
    board[-1].append('*')

  # use stack to rotate rows to columns
  stack = []
  # will hold final answer
  ans = []
  # for each column
  for j in range(side):
    # each row
    for i in range(side):
      # add to stack
      stack.append(board[i][j])
    # pop off all elements and add to new array if not *
    while stack:
      char = stack.pop()
      if char != '*':
        ans.append(char)
  return ''.join(ans)

def main():
  cases = int(input())
  for i in range(cases):
    message = input()
    ans = encrypt(message)
    print(ans)

if __name__ == '__main__':
    main()
