# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/mixedfractions
# Complexity: O(1)
# Memory: O(1)

def main():
  while True:
    n, m = map(int, input().split())
    if n == m == 0:
      break

    # base is found by integer division
    base = n // m
    # remaining is modulo
    rem = n % m
    print(base, rem, '/', m)

if __name__ == '__main__':
  main()
