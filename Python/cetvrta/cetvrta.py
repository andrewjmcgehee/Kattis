# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/cetvrta
# Complexity: O(1)
# Memory: O(1)

def main():
  p1 = input().split()
  p2 = input().split()
  p3 = input().split()

  # x coordinate must be the one that is not repeated twice
  if p1[0] == p2[0]:
    p4x = p3[0]
  elif p1[0] == p3[0]:
    p4x = p2[0]
  else:
    p4x = p1[0]

  # same for y
  if p1[1] == p2[1]:
    p4y = p3[1]
  elif p1[1] == p3[1]:
    p4y = p2[1]
  else:
    p4y = p1[1]

  print(p4x, p4y)

if __name__ == '__main__':
  main()
