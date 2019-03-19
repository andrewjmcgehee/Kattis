# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/throwns
# Complexity: O(N) for N operations
# Memory: O(N) for stack

def main():
  n, m = map(int, input().split())

  # get commands
  commands = input().split()
  egg = 0
  i = 0
  # used for undos
  stack = []
  while i < len(commands):
    # undo operation
    if commands[i].startswith('u'):
      total = 0
      # start at next int and pop from stack
      for j in range(int(commands[i+1])):
        total += stack.pop()
      # undo so subtraction
      egg -= total
      # fix index to be between 0 and n exclusive
      while egg < 0:
        egg += n
      while egg >= n:
        egg -= n
      # increment by 2 since undo has two parts to operation
      i += 2
    else:
      # track for later
      stack.append(int(commands[i]))
      # add since not undoing
      egg += int(commands[i])
      # fix index to be between 0 and n exclusive
      while egg < 0:
        egg += n
      while egg >= n:
        egg -= n
      i += 1
  print(egg)


if __name__ == "__main__":
  main()
