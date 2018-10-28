# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/ada
# Complexity: O(N^2) in worst case as it may take N derivatives to get to constant
# Memory: O(N^2) in worst case as ragged array will store N(N-1) / 2 values

def main():
  # trash first value
  arr = [int(x) for x in input().split()][1:]

  n = 0
  # a ragged array holding each row of differences
  diffs = []
  # initial row is unaltered
  diffs.append(arr)

  while True:
    vals = set()
    order_diffs = []
    # there will always be n-1 differences for a row of n values
    for i in range(1, len(diffs[n])):
      val = diffs[n][i] - diffs[n][i-1]
      order_diffs.append(val)
      vals.add(val)
    diffs.append(order_diffs)
    n += 1
    # if we have only seen one value in the set, we have hit the constant derivative
    if len(vals) == 1:
      break

  # continue the sequence by extending the constant derivative with one more
  # occurence of its value and calculate the upstream differences
  for i in range(n, 0, -1):
    diffs[i-1].append(diffs[i-1][-1] + diffs[i][-1])

  # length will be one less because original 0th order derivative is not included
  # next value will be last value in first row of the differences ragged array
  print(len(diffs)-1, diffs[0][-1])

if __name__ == '__main__':
  main()
