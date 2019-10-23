# Rating: ~ 4.3 / 10
# Link: https://open.kattis.com/problems/swaptosort

import sys

def union(uf, a, b):
  uf[find(uf, a)] = find(uf, b)

def find(uf, a):
  if uf[a] == a:
    return a
  else:
    uf[a] = find(uf, uf[a])
  return uf[a]

def main():
  data = sys.stdin.readlines()
  n, k = map(int, data.pop(0).strip().split())
  uf = [i for i in range(n+1)]
  for i in range(k):
    a, b = map(int, data[i].strip().split())
    union(uf, a, b)

  half = n // 2
  works = True
  for i in range(1, half+1):
    a_root = find(uf, i)
    b_root = find(uf, n-i+1)
    if a_root != b_root:
      works = False
      break
  if works:
    print('Yes')
  else:
    print('No')

if __name__ == "__main__":
  main()
