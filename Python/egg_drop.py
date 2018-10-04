# This is not a solution to a kattis problem
#
# This is a general framework for solving the common DP problem of finding
# minimum number of trials for dropping n eggs off of k floors and finding
# the highest safe floor to drop from

INT_MAX = 100000

def egg_drop(n, m):
  # a 2D table where entry memo[n][m] will represent minimum
  # number of trials needed for n eggs and m floors.
  memo = [[0 for j in range(m+1)] for i in range(n+1)]

  # we need 1 trial for 1 floor and 0 trials for 0 floors
  for i in range(1, n+1):
    memo[i][1] = 1
    memo[i][0] = 0

  # we always need n trials for one egg and n floors.
  for j in range(1, m+1):
    memo[1][j] = j

  # fill rest of the entries in table using optimal substructure
  # property
  for i in range(2, n+1):
    for j in range(2, m+1):
      memo[i][j] = INT_MAX
      for k in range(1, j+1):
        # here k represents the lowest safe floor
        # memo[i-1][k-1] represents breaking an egg
        # memo[i][j-k] represents not breaking an egg
        res = 1 + max(memo[i-1][k-1], memo[i][j-k])
        if res < memo[i][j]:
          memo[i][j] = res

  # memo[n][k] holds the result
  return memo[n][m]

if __name__ == '__main__':
  while True:
    n, m = map(int, input().split())
    if n == m == 0:
      break
    print(egg_drop(n, m))
