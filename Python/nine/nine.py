# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/nine
# Complexity: O(log(N)) for geometric series
# Memory: O(log(N)) for recursive overhead

mod = 1000000007

def solve(n):
  # trivial cases
  if n == 0:
    return 1
  if n == 1:
    return 9
  # the intuition is this:
  # if we have 7 digits, this is the same as having 9 * 6 digits because
  # the leading digit can be 1-9 but not 0

  # but if we have 6 digits remaining with the leading digit already considered
  # we have 10 options (0-9) for each digit so we have 10^6 options
  # but 10^6 can be written at 10^3 * 10^3 or (10^3)^2, so we can simply calculate
  # as if we have 3 digits instead of 6, then we can square the result and
  # multiple by 9 and get the same result. that results in the following
  # geometric series

  # if number of digits is odd the geometric series follows this formula
  if n & 1:
    tmp = solve((n - 1) // 2)
    return 9 * tmp**2 % mod
  # if number of digits is even the geometric series follows this formula
  else:
    tmp = solve(n // 2)
    return tmp**2 % mod

def main():
  t = int(input())
  for i in range(t):
    n = int(input())
    # multiplied by 8 for single digit positives without a 9
    print(8 * solve(n-1) % mod)

if __name__ == '__main__':
  main()
