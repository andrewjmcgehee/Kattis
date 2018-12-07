# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/dvds
# Complexity: O(N) for N dvds
# Memory: O(N) for N dvds

def main():
  t = int(input())
  for i in range(t):
    # get inputs
    n = int(input())
    dvds = [int(x) for x in input().split()]

    # just need to find the number of dvds that are in their correct
    # order
    expected = 1
    for i in range(n):
      # if a dvd is in the correct place, the next expected dvd is 1
      # greater than it.
      if expected == dvds[i]:
        expected += 1
    print(n - expected + 1)

if __name__ == "__main__":
  main()
