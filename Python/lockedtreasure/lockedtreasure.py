# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/lockedtreasure

nck = [[0 for i in range(32)] for j in range(32)]
for i in range(31):
  nck[i][1] = 1
for i in range(1, 32):
  for j in range(1, i+1):
    nck[i][j] = nck[i-1][j-1] + nck[i-1][j]

def main():
  t = int(input())
  for _ in range(t):
    n, m = map(int, input().split())
    if m == 1:
      print(1)
      continue
    print(nck[n+1][m])

if __name__ == "__main__":
  main()
