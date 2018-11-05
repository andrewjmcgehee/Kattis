# Rating: ~ 6.1 / 10
# Link: https://open.kattis.com/problems/primes
# Complexity: O(
# Memory: O(

from math import *

# holds candidate numbers
nums = []
# number of primes we can use as factors
num_primes = 0
# holds the primes we can use as factors
primes = []
# starting range
start = -1
# end of range
end = -1

# use backtracking to generate candidates for primes
def generate(n, val):
  global nums, num_primes, primes, start, end
  # if we have used
  if n == num_primes:
    if val >= start:
      nums.append(val)
  else:
    p = primes[n]
    # number of times we can multiple by a given factor before exceeding
    # the end range
    limit = int(ceil(log(end) / log(p))) + 1
    # try each power of that number
    for i in xrange(limit):
      val *= pow(p, i)
      # generate another candidate
      if val <= end:
        generate(n+1, int(val))
        # backtrack
        val = val / pow(p, i)

def main():
  global nums, num_primes, primes, start, end
  while True:
    num_primes = input()
    if num_primes == 0:
      break

    # get prime factors
    primes = [int(x) for x in raw_input().split()]
    # get range
    start, end = map(int, raw_input().split())
    # clear nums
    nums = []
    # generate candidates
    generate(0, 1)
    ans = []
    if nums:
      for val in sorted(nums):
        ans.append(str(val))
      print ','.join(ans)
    else:
      print 'none'

if __name__ == '__main__':
  main()

