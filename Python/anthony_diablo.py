# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/anthonyanddiablo
# Complexity: O(1)
# Memory: O(1)

import math

def main():
  n, m = map(float, input().split())
  # intuition is that circle maximizes area in all directions
  radius = m / (2 * math.pi)

  if math.pi * radius**2 >= n:
    print('Diablo is happy!')
  else:
    print('Need more materials!')

if __name__ == '__main__':
  main()
