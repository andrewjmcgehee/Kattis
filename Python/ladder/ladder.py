# Rating: ~ 1.3
# Link: https://open.kattis.com/problems/ladder
# Complexity: O(1)
# Memory: O(1)

import math

def main():
  # just trig
  r, theta = map(int, input().split()
  print(int(r / math.sin(math.radians(theta))) + 1)

if __name__ == '__main__':
  main()
