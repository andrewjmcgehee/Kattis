# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/2048
# Complexity: O(N*K) where N and K are dimensions of board
# Memory: O(N*K) where N and K are dimensions of board

def main():
  # create board
  b = [[int(x) for x in input().split()] for y in range(4)]

  direction = int(input())

  # process for each direction is similar, just changing how
  # i and j behave

  # left
  if direction == 0:
    for j in range(4):
      # we will "lock" some values after they have been merged to prevent merging
      # too much
      locked = set()
      edits = 1
      while edits > 0:
        edits = 0
        for i in range(1, 4):
          # skip over zeros
          if b[j][i] == 0:
            continue
          # move value into zero spot
          if b[j][i-1] == 0:
            b[j][i-1] = b[j][i]
            b[j][i] = 0
            edits += 1
            # lock the spot we just moved into
            if i in locked:
              locked.remove(i)
              locked.add(i-1)
          # if neither of these squares are locked and they are equal, merge them
          # and lock the resulting square
          elif i not in locked and (i-1) not in locked and b[j][i-1] == b[j][i]:
            b[j][i-1] *= 2
            b[j][i] = 0
            locked.add(i-1)
            edits += 1
  # up
  elif direction == 1:
    for i in range(4):
      locked = set()
      edits = 1
      while edits > 0:
        edits = 0
        for j in range(1, 4):
          if b[j][i] == 0:
            continue
          if b[j-1][i] == 0:
            b[j-1][i] = b[j][i]
            b[j][i] = 0
            edits += 1
            if j in locked:
              locked.remove(j)
              locked.add(j-1)
          elif j not in locked and (j-1) not in locked and b[j-1][i] == b[j][i]:
            b[j-1][i] *= 2
            b[j][i] = 0
            locked.add(j-1)
            edits += 1
  # right
  elif direction == 2:
    for j in range(4):
      locked = set()
      edits = 1
      while edits > 0:
        edits = 0
        for i in range(2, -1, -1):
          if b[j][i] == 0:
            continue
          if b[j][i+1] == 0:
            b[j][i+1] = b[j][i]
            b[j][i] = 0
            edits += 1
            if i in locked:
              locked.remove(i)
              locked.add(i+1)
          elif i not in locked and (i+1) not in locked and b[j][i+1] == b[j][i]:
            b[j][i+1] *= 2
            b[j][i] = 0
            locked.add(i+1)
            edits += 1
  # down
  elif direction == 3:
    for i in range(4):
      locked = set()
      edits = 1
      while edits > 0:
        edits = 0
        for j in range(2, -1, -1):
          if b[j][i] == 0:
            continue
          if b[j+1][i] == 0:
            b[j+1][i] = b[j][i]
            b[j][i] = 0
            edits += 1
            if j in locked:
              locked.remove(j)
              locked.add(j+1)
          elif j not in locked and (j+1) not in locked and b[j+1][i] == b[j][i]:
            b[j+1][i] *= 2
            b[j][i] = 0
            locked.add(j+1)
            edits += 1
  # print board
  for row in b:
    line = ""
    for item in row:
      line += str(item)
      line += " "
    print(line.strip())

if __name__ == '__main__':
  main()
