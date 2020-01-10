# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/tight


def main():
  while True:
    try:
      k, n = map(int, input().split())
    except:
      break
    if k == 0:
      print(100)
      continue
    memo = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for j in range(k+1):
      memo[1][j] = 1
    for i in range(2, n+1):
      memo[i][0] = memo[i-1][0] + memo[i-1][1]
      memo[i][k] = memo[i-1][k] + memo[i-1][k-1]
      for j in range(1, k):
        memo[i][j] = memo[i-1][j-1] + memo[i-1][j] + memo[i-1][j+1]
    total = (k+1)**n
    tight = sum(memo[n][:k+1])
    print(tight / total * 100)

if __name__ == "__main__":
  main()

# 0  0  0
# 1  1  1
# 2  3  2
# 5  7  5
# 12 17 12
# 29 41 29

