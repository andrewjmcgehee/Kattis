# Rating: ~ 3.3 / 10
# Link: https://open.kattis.com/problems/industrialspy
# Complexity: O(k!) where k is number of digits (less than or equal to 7)
# Memory: O(PI(n)) where PI(n) is the function representing number of primes less than n


from math import ceil
from itertools import permutations

MAX = 10000000

def main():
    is_prime = [True] * MAX
    is_prime[0] = False
    is_prime[1] = False

    i = 2
    while i**2 <= MAX:
      if is_prime[i]:
        for j in range(i*i, MAX, i):
          is_prime[j] = False
      i += 1

    num_cases = int(input())
    for t in range(num_cases):
      num = raw_input().strip()
      num = ''.join(sorted(num))
      primes = set()

      p = permutations(num)
      while True:
        try:
          s = ''.join(next(p))

          for j in range(1, len(s)+1):
            sub = s[0:j]
            n = int(sub)

            if is_prime[n]:
              primes.add(n)
        except StopIteration:
          break

      print len(primes)

if __name__ == '__main__':
    main()
