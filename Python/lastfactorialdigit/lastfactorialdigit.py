# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/lastfactorialdigit
# Complexity: O(N) for N cases
# Memory: O(1)

def main():
  n = int(input())
  # trivial to determine manually
  arr = [1, 1, 2, 6, 4, 0, 0, 0, 0, 0, 0]

  for i in range(n):
    t = int(input())
    print(arr[t])


if __name__ == "__main__":
  main()
