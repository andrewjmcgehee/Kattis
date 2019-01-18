# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/awkwardparty
# Complexity: O(N) for N people at the table
# Memory: O(N) for N people in the table

def main():
  n = input()
  table = [int(x) for x in input().split()]
  # logest starts as all people and then is minimized
  shortest = len(table)

  # DP table which stores index of last time a language was seen
  last = dict()
  for i, val in enumerate(table):
    # first time to see it
    if val not in last:
      last[val] = i
      continue
    else:
      # repeat, so update shortest
      sequence = i - last[val]
      shortest = min(shortest, sequence)
      # update last seen index
      last[val] = i
  print(shortest)

if __name__ == "__main__":
  main()
