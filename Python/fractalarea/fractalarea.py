# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/fractalarea

import math

def main():
  t = int(input())
  for _ in range(t):
    r, n = map(int, input().split())
    if n == 1:
      print(math.pi * r**2)
    elif n == 2:
      print(math.pi * r**2 + 4 * math.pi * r**2 / 4)
    else:
      initial = 2 * math.pi * r**2
      n -= 2
      num_circles = 12
      radius = r/4
      for i in range(n):
        initial += num_circles * math.pi * radius**2
        radius /= 2
        num_circles *= 3
      print(initial)

if __name__ == "__main__":
  main()
