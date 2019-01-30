mod = 1000000007

def solve(n):
  if n == 0:
    return 1
  if n == 1:
    return 9
  if n & 1:
    tmp = solve((n - 1) // 2) % mod
    return (9 * tmp**2 % mod) % mod
  else:
    tmp = solve(n // 2) % mod
    return tmp**2 % mod

def main():
  t = int(input())
  for i in range(t):
    n = int(input())
    print(8 * solve(n-1) % mod)

if __name__ == '__main__':
  main()
