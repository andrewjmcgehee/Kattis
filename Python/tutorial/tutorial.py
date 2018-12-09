# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/tutorial
# Complexity: O(1)
# Memory: O(1)

import math

# helper function for calculating if factorial less than m
def factorial(n, m):
  f = 1
  # allow for early exit
  while f <= m and n > 1:
    f *= n
    n -= 1
  if f <= m:
    return True
  return False

def main():
  m, n, t = map(int, input().split())

  # accepted flag
  AC = False
  # factorial time
  if t == 1:
    if factorial(n, m):
      AC = True
  # 2^n
  elif t == 2:
    if 2**n <= m:
      AC = True
  # n^4
  elif t == 3:
    if n**4 <= m:
      AC = True
  # n^3
  elif t == 4:
    if n**3 <= m:
      AC = True
  # n^2
  elif t == 5:
    if n**2 <= m:
      AC = True
  # n log(n)
  elif t == 6:
    if n * math.log(n, 2) <= m:
      AC = True
  # n
  else:
    if n <= m:
      AC = True
  if AC:
    print('AC')
  else:
    print('TLE')

if __name__ == "__main__":
  main()
