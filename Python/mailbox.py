# Rating: ~ 2.1 / 10 (arguably much harder than a 2.1)
# Link: https://open.kattis.com/problems/mailbox
# Complexity: O(NK^2) where N is number of mailboxes and K is number of firecrackers
# Memory: O(NK^2) where N is number of mailboxes and K is number of firecrackers

def main():
  INF = 1000000
  MAX_FC = 101
  MAX_MAILBOX = 10

  # memo array where i represents number of mailboxes, j represents highest safe mailbox
  # and k represents lowest exploded mailbox
  memo = [[[0 for k in range(MAX_FC+1)] for j in range(MAX_FC+1)] for i in range(MAX_MAILBOX+1)]

  # if only 1 mailbox, then num of firecrackers is
  # (j(j + 1)) / 2 - sum of 1 through j
  for j in range(MAX_FC):
    for k in range(j+1, MAX_FC+1):
      cost = 0
      for fc in range(j+1, k):
        cost += fc
      memo[1][j][k] = cost

  # no matter how many mailboxes, if highest safe  == lowest explode + 1, then
  # then 0 firecrackers are needed because we already no that highest safe is the answer
  for i in range(2, MAX_MAILBOX+1):
    for j in range(MAX_FC):
      memo[i][j][j+1] = 0

  # fill in rest of table for 2 < mailboxes < 11, such that highest safe < firecrackers <
  # lowest explode
  for i in range(2, MAX_MAILBOX+1):
    for j in range(MAX_FC-1, -1, -1):
      for k in range(j+2, MAX_FC+1):
        best = INF

        for fc in range(j+1, k):
          cost = fc + max(memo[i-1][j][fc], memo[i][fc][k])
          best = min(best, cost)
        memo[i][j][k] = best


  t = int(input())
  for _ in range(t):
    n, m = map(int, input().split())
    # start with 0 as highest safe and m + 1 as lowest exploded
    print(memo[n][0][m+1])


if __name__ == '__main__':
    main()
