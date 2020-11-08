# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/equilibrium

from collections import deque, defaultdict

def parse(s):
  tokens = deque([''])
  for c in s:
    if c == '[':
      tokens.append('[')
      tokens.append('')
    elif c == ']':
      tokens.append(']')
      tokens.append('')
    elif c == ',':
      tokens.append('')
    else:
      tokens[-1] += c
  return tokens

def solve():
  s = input()
  depth = 0
  freq = defaultdict(int)
  tokens = parse(s)
  nums = 0
  for t in tokens:
    if t == '[':
      depth += 1
    elif t == ']':
      depth -= 1
    elif t == '':
      pass
    else:
      value = int(t)
      freq[value << depth] += 1
      nums += 1
  most = max(freq.values())
  print(nums - most)

def main():
  N = int(input())
  for i in range(N):
    solve()

if __name__ == "__main__":
  main()
