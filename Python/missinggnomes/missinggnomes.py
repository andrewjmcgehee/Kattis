# Rating: ~ 2.3 / 10
# Link: https://open.kattis.com/problems/missinggnomes
# Complexity: O(N) for N gnomes
# Memory: O(N) for N gnomes

# just for speed
from sys import stdin, stdout

def main():
  n, m = map(int, stdin.readline().split())
  # track order
  found = []
  for i in range(m):
    found.append(int(stdin.readline()))
  # track presence in O(1)
  seen = set(found)

  # join is faster than string concat
  out = []
  i = 0
  for num in found:
    # take all numbers less than current number that arent in seen
    while i < num:
      i += 1
      if i not in seen:
        out.append(str(i))
    # take current found gnome
    out.append(str(num))
  # if any gnomes remain add them
  while i < n:
    i += 1
    out.append(str(i))
  stdout.write('\n'.join(out) + '\n')

if __name__ == "__main__":
  main()
