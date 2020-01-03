# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/multigram

from collections import defaultdict

def solve(g):
  mid = len(g)//2
  for i in range(1, mid+1):
    if len(g) % i != 0:
      continue
    freq = defaultdict(int)
    for c in g[:i]:
      freq[c] += 1
    found = True
    for j in range(i, len(g), i):
      for k in freq:
        if g[j:j+i].count(k) != freq[k]:
          found = False
          break
    if found:
      return g[:i]
  return -1

def main():
  g = input()
  print(solve(g))

if __name__ == "__main__":
  main()
