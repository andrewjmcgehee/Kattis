# Rating: ~ 2.3 / 10
# Link: https://open.kattis.com/problems/toilet
# Complexity: O(N) for N characters
# Memory: O(1)

def main():
  line = input()
  up = 0
  down = 0
  found = 0

  # always leave it up
  for i in range(1, len(line)):
    # handle first case
    if i == 1:
      # initially up, second prefers down but must put back up
      if line[0] == 'U' and line[1] == 'D':
        up += 2
      # initially down, does not matter what second prefers
      # 1 switch required
      elif line[0] == 'D':
        up += 1
    # add two for all remaining D's
    elif line[i] == 'D':
      up += 2
  # always leave it down
  # same as up but in switch the cases
  for i in range(1, len(line)):
    if i == 1:
      if line[0] == 'D' and line[1] == 'U':
        down += 2
      elif line[0] == 'U':
        down += 1
    elif line[i] == 'U':
      down += 2
  # leave it how you prefer it
  # one switch required per change
  for i in range(1, len(line)):
    if line[i] != line[i-1]:
      found += 1
  print(up)
  print(down)
  print(found)

if __name__ == '__main__':
    main()
