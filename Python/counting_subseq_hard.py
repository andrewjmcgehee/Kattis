# Rating: ~ 3.6 / 10
# Link: https://open.kattis.com/problems/subseqhard
# Complexity: O(N) where N is the number of items in the array
# Memory: O(N) for the memo table

def main():
  t = int(input())
  for _ in range(t):
    # get rid of white space
    ws = input()
    n = int(input())
    arr = [0] + [int(x) for x in input().split()]

    # this will store the number of sequences we have seen that
    # sum to a given number
    memo = dict()
    memo[0] = 1

    # this calculates all the prefix sums 0 through n inclusive
    for i in range(1, n+1):
      arr[i] += arr[i-1]

    num_interesting = 0
    for i in range(1, n+1):
      # we want to know the difference between our current subsequence
      # and a sequence that would sum to 47
      diff = arr[i] - 47

      # for every sequence we have seen that sums to that difference, we
      # can exclude that sequence from the current one and get a new
      # sequence that sums to exactly 47
      if diff not in memo:
        memo[diff] = 0
      num_interesting += memo[diff]

      # we store each item in the dictionary by its prefix sum
      if arr[i] not in memo:
        memo[arr[i]] = 0
      memo[arr[i]] += 1

    print(num_interesting)

if __name__ == '__main__':
  main()
