# Rating: ~ 4.2 / 10
# Link: https://open.kattis.com/problems/digits

import sys
import math

def main():
  data = [l.strip() for l in sys.stdin.readlines()]
  out = []
  for line in data:
    if line == 'END':
      break
    # can be long, don't convert to int
    x0 = line
    # can be max of 1000000
    x1 = len(x0)
    # trivial cases - single digit
    if x1 == 1:
      # safe to convert to int now
      if int(x0) == 1:
        out.append('1')
      else:
        out.append('2')
      continue
    # only need 4 levels to check worst case
    # 0: x0
    # 1: 1000000
    # 2: 7
    # 3: 1
    # 4: 1
    x2 = int(math.log10(x1))+1
    x3 = int(math.log10(x2))+1
    x4 = int(math.log10(x3))+1
    if x2 == x1:
      out.append('2')
    elif x3 == x2:
      out.append('3')
    elif x4 == x3:
      out.append('4')
  print('\n'.join(out))

if __name__ == '__main__':
  main()
