# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/dicecup

from collections import defaultdict

def main():
  a, b = map(int, input().split())
  freq = defaultdict(int)
  for i in range(1, a+1):
    for j in range(1, b+1):
      freq[i+j] += 1
  max_val = max(freq.values())
  keys = []
  for k in freq.keys():
    if freq[k] == max_val:
      keys.append(k)
  keys.sort()
  for k in keys:
    print(k)


if __name__ == "__main__":
  main()
