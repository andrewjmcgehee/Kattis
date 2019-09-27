# Rating: ~ 4.8 / 10
# Link: https://open.kattis.com/problems/stringmatching

import sys

def kmp(pattern, string):
  M = len(pattern)
  N = len(string)
  indices = []
  lps = get_lps(pattern, M)
  i = 0
  j = 0
  while i < N:
    if pattern[j] == string[i]:
      i += 1
      j += 1
    if j == M:
      indices.append(str(i-j))
      j = lps[j-1]
    elif i < N and pattern[j] != string[i]:
      if j != 0:
        j = lps[j-1]
      else:
        i += 1
  return indices

def get_lps(pattern, M):
  lps = [0 for i in range(M)]
  # length of the previous longest prefix suffix
  prev_longest = 0
  i = 1
  while i < M:
    if pattern[i] == pattern[prev_longest]:
      prev_longest += 1
      lps[i] = prev_longest
      i += 1
    else:
      if prev_longest != 0:
        prev_longest = lps[prev_longest-1]
      else:
        lps[i] = 0
        i += 1
  return lps

def main():
  lines = sys.stdin.readlines()
  for i in range(0, len(lines), 2):
    pattern = lines[i].strip()
    string = lines[i+1].strip()
    print(" ".join(kmp(pattern, string)))

if __name__ == "__main__":
  main()
