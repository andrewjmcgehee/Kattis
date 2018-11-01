# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/r2
# Complexity: O(1)
# Memory: O(1)

def main():
  # (r1 + r2) / 2 = S so r2 = 2S - r1
  r1, s = map(int, input().split())
  r2 = 2*s - r1
  print(r2)

if __name__ == '__main__':
  main()
