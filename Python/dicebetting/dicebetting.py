# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/dicebetting
# Complexity: O(N) for N throws
# Memory: O(NK) for N throws and K distinct values to see

n, s, k = map(int, raw_input().split())
memo = [[None for j in xrange(s+1)] for i in xrange(n+1)]

def prob(throws, seen):
  # already seen enough values to win
  if seen >= k:
    return 1.0
  # no throws remaining, 0 probability of seeing new value
  if throws == 0:
    return 0.0
  # pre-calculated result
  if memo[throws][seen]:
    return memo[throws][seen]

  # number of distinct numbers we've seen divided by the number of sides of the die
  old_prob = float(seen) / s
  # DeMorgan's law
  new_prob = 1.0 - old_prob

  # calculate probability of seeing a new number and not seeing a new number
  result = (old_prob * prob(throws-1, seen)) + (new_prob * probability(throws-1, seen+1))
  # store the result
  memo[throws][seen] = result
  return memo[throws][seen]


def main():
  # initially seen 0 and have n throws remaining
  print(prob(n, 0))

if __name__ == '__main__':
  main()
