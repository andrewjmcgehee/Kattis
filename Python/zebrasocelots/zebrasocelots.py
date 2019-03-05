# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/zebrasocelots
# Complexity: O(N) for N characters in binary string
# Memory: O(N) for N characters in binary string

import sys

def main():
  N = int(input())
  tower = []
  for line in sys.stdin:
    # follows pattern of binary down counter where 0s are Zebras
    # and 1s are Ocelots
    if line.strip() == 'Z':
      tower.append('0')
    else:
      tower.append('1')
  tower = ''.join(tower)
  # conver binary to int
  print(int(tower, 2))


if __name__ == "__main__":
  main()
