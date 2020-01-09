# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/warehouse

from collections import defaultdict

def main():
  cases = int(input())
  for c in range(cases):
    n = int(input())
    freq = defaultdict(int)
    for i in range(n):
      name, val = input().split()
      freq[name] += int(val)
    ans = sorted(freq.items(), key=lambda k: (-k[1],k[0]))
    print(len(freq))
    for i in range(len(ans)):
      print(ans[i][0], ans[i][1])


if __name__ == "__main__":
  main()
