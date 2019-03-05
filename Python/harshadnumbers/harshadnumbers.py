# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/harshadnumbers
# Complexity: O(N) for N characters
# Memory: O(N) for N characters

def main():
  n = int(input())
  while True:
    # convert to list of ints for each digit
    x = [int(x) for x in list(str(n))]
    total = sum(x)
    # trivial
    if n % total == 0:
      break
    n += 1
  print(n)


if __name__ == "__main__":
  main()
