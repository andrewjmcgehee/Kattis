# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/listgame
# Complexity: O(K) where K is the number of prime factors of a given number
# Memory: O(1)

from math import ceil

def main():
  n = int(input())
  num_factors = 0
  factor = 2
  # check if num is greater than square root of number
  while (factor**2 <= n):
    # divide if possible
    if (n % factor == 0):
      n /= factor
      num_factors += 1
    else:
      factor += 1

  # exactly one factor will always be left over
  num_factors += 1
  print(num_factors)

if __name__ == '__main__':
    main()
