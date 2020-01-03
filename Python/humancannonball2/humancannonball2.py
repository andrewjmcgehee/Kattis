# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/humancannonball2

import math

def main():
  n = int(input())
  for i in range(n):
    v, th, x, h1, h2 = map(float, input().split())
    th = math.radians(th)
    # x component of velocity
    vx = v * math.cos(th)
    tx = x / vx
    y = v * tx * math.sin(th) - 0.5*9.81*(tx**2)
    if y < h2-1 and y > h1+1:
      print('Safe')
    else:
      print('Not Safe')

if __name__ == "__main__":
  main()
