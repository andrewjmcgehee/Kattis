from math import *

nums = []
num_primes = 0
primes = []
start = -1
end = -1

def generate(n, val):
  global nums, num_primes, primes, start, end
  if n == num_primes:
    if val >= start and val <= end:
      nums.append(val)
  else:
    p = primes[n]
    limit = int(ceil(log(end) / log(p))) + 1
    for i in xrange(limit):
      val *= pow(p, i)
      if val <= end:
        generate(n+1, int(val))
        val = val / pow(p, i)


def main():
  global nums, num_primes, primes, start, end
  while True:
    num_primes = input()
    if num_primes == 0:
      break

    primes = [int(x) for x in raw_input().split()]
    start, end = map(int, raw_input().split())
    nums = []

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

