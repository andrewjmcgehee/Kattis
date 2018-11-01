# Rating: ~ 3.9 / 10 (not really, just lots of wrong submits)
# Link: https://open.kattis.com/problems/meowfactor
# Complexity: O(log (N)) base 9
# Memory: O(1)

def solve(n):
  # start at maximum possible 9th root and decrement
  for i in range(int(n**(1/9.0)) + 1, 0, -1):
    # if divides evenly return
    if n % i**9 == 0:
      return i

def main():
  t = int(input())
  print(solve(t))

if __name__ == '__main__':
  main()
