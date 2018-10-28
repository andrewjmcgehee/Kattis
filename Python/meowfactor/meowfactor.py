def solve(n):
  for i in range(int(n**(1/9.0)) + 1, 0, -1):
    if n % i**9 == 0:
      return i

def main():
  t = int(input())
  print(solve(t))

if __name__ == '__main__':
  main()
