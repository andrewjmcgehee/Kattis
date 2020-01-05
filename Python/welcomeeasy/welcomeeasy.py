# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/welcomeeasy

def main():
  b = "welcome to code jam"
  c = int(input())
  for case in range(1, c+1):
    a = input()
    m = len(a)
    n = len(b)
    lookup = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(n+1):
      lookup[0][i] = 0
    for i in range(m+1):
      lookup[i][0] = 1

    for i in range(1, m+1):
      for j in range(1, n+1):
        if a[i-1] == b[j-1]:
          lookup[i][j] = lookup[i-1][j-1] + lookup[i-1][j]
        else:
          lookup[i][j] = lookup[i-1][j]
    print('Case #{}: {:04d}'.format(case, lookup[m][n] % 10000))


if __name__ == "__main__":
  main()
