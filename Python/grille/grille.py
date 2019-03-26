# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/grille
# Complexity: O(N^2) for an N^2 grid
# Memory: O(N^2) for an N^2 grid

# helper to rotate the grille 90 degrees
def rotate_grille(grille):
  # use stack to convert rows to cols
  stack = []
  new_grille = [[] for i in range(len(grille))]
  for i in range(len(grille)):
    stack.extend(list(grille[i]))
    row = 0
    while stack:
      new_grille[row].append(stack.pop())
      row += 1
  # rejoin rows
  new_grille = [''.join(row) for row in new_grille]
  return new_grille

def main():
  n = int(input())
  grille = [input() for i in range(n)]
  # storing holes is more efficient than storing grids and searching each time
  holes = [[] for i in range(4)]
  # track which squares are allowed to be seen through holes
  represented = set()
  # rotate 4 times, more is redundant
  for i in range(4):
    grille = rotate_grille(grille)
    # store for later
    for j in range(n):
      for k in range(n):
        # if its a hole add to represented
        if grille[j][k] == '.':
          holes[i].append(n*j + k)
          represented.add(n*j + k)
    # sort holes in reverse row major order because thats the opposite
    # order they were visited when encrypting
    holes[i].sort(reverse=True)
  # all holes should be represented exactly once
  num_holes = len(holes[0])
  if len(represented) != n**2 or num_holes * 4 != n**2:
    print('invalid grille')
    return
  # rebuild original message
  cipher = [['' for j in range(n)] for i in range(n)]
  line = input()
  for rotation in range(4):
    hole_group = holes[rotation]
    # get enough characters for holes
    end = list(line[-1*num_holes:])
    # trim line array
    line = line[:-1*num_holes]
    for hole in hole_group:
      # convert from row major back to row col
      r, c = hole // n, hole % n
      cipher[r][c] = end.pop()
  # join cipher back together and print
  cipher = [''.join(row) for row in cipher]
  cipher = ''.join(cipher)
  print(cipher)


if __name__ == "__main__":
  main()
