# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/cakeymccakeface
# Complexity: O(NM) for N entry points and M exit points
# Memory: O(N + M) for N entry points and M exit points

def main():
  # inputs
  n = int(input())
  m = int(input())
  entry = [int(x) for x in input().split()]
  exit = [int(x) for x in input().split()]
  # track frequency of time differences
  best_times = dict()
  for i in entry:
    for j in exit:
      if i <= j:
        if j-i not in best_times:
          best_times[j-i] = 0
        best_times[j-i] += 1
  # intentionally impossible
  best = float('inf')
  freq = 0
  for k, v in best_times.items():
    # take most frequent
    if v > freq:
      freq = v
      best = k
    # break tie with lower time
    elif v == freq and k < best:
      best = k
  if best != float('inf'):
    print(best)
  # not sure if this edge case is described in the problem description
  # but it fixed things.
  else:
    print(0)


if __name__ == "__main__":
  main()
