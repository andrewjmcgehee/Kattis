# Rating: ~ 2.5 / 10
# Link: https://open.kattis.com/problems/artichoke
# Complexity: O(N) for N iterations on the function
# Memory: O(1)

import math

def main():
  ins = [int(i) for i in input().split()]
  # get inputs
  p = ins[0]
  a = ins[1]
  b = ins[2]
  c = ins[3]
  d = ins[4]
  n = ins[5]

  # follow given formulas for k = 1
  peak = p * (math.sin(a+b) + math.cos(c+d) + 2)
  # initial decline is 0
  decline = 0.0

  k = 2
  while k <= n:
    # calculate new price
    valley = peak
    tmp = p * (math.sin(a*k+b) + math.cos(c*k+d) + 2)
    tmp_decline = 0
    # find minimum valley
    while tmp <= peak and k <= n:
      valley = min(tmp, valley)
      tmp_decline = peak - valley
      k += 1
      tmp = p * (math.sin(a*k+b) + math.cos(c*k+d) + 2)
    peak = tmp
    # maximize decline
    decline = max(tmp_decline, decline)
    k += 1
  print(decline)

if __name__ == '__main__':
    main()
