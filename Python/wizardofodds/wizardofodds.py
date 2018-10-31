# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/wizardofodds
# Complexity: O(1) but bounded by number of digits in N
# Memory: O(1)

import math

def main():
  n, k = map(int, input().split())
  # binary search is log base 2
  num_guesses = math.log2(n)
  if num_guesses > k:
    print('You will become a flying monkey!')
  else:
    print('Your wish is granted!')

if __name__ == '__main__':
  main()
