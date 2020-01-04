# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/raggedright

from sys import stdin

def main():
  lines = stdin.read().splitlines()
  max_len = 0
  for l in lines:
    max_len = max(max_len, len(l))

  penalty = 0
  for l in lines[:-1]:
    penalty += (len(l) - max_len)**2
  print(penalty)

if __name__ == "__main__":
  main()
