# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/teacherevaluation

import math

def main():
  n, p = map(int, input().split())
  total = 0
  total = sum(map(int, input().split()))
  if p == 100 and total / n != 100:
    print('impossible')
  elif p == 100:
    print(0)
  else:
    print(math.ceil((p*n - total) / (100 - p)))

if __name__ == "__main__":
  main()
