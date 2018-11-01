# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/maximumrent
# Complexity: O(M) for constraint M given in problem
# Memory: O(1)

def main():
  # get coefficients
  a, b = [int(x) for x in raw_input().split()]
  m, s = [int(x) for x in raw_input().split()]

  best_rent = 0
  for i in xrange(1, m):
    # x + y <= m so y <= m - x
    x = i
    y = m-i
    # 2x + y must be >= S
    if (2*x + y) < s:
      continue
    # try this configuration and take the max
    best_rent = max(best_rent, a*x + b*y)
  print best_rent

if __name__ == '__main__':
  main()
