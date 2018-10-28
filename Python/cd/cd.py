# Rating: ~ 4.8 / 10
# Link: https://open.kattis.com/problems/cd
# Complexity: O(N) for N cds
# Memory: O(N) for N cds

def main():
  while True:
    n, m = [int(x) for x in input().split()]
    if n == 0 and m == 0:
      break

    # represent jacks collection as a set
    jack = set()
    for i in range(n):
      cd = input()
      jack.add(cd)
    # no need to represent jills collection, simply check jacks
    common = 0
    for i in range(m):
      cd = input()
      if cd in jack:
        common += 1
    print(common)

if __name__ == '__main__':
  main()
