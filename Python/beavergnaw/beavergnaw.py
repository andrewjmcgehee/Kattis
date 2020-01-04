# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/beavergnaw

import math

def main():
  while True:
    D, V = map(int, input().split())
    if D == V == 0:
      break
    r = D / 2
    vol = D * math.pi * r**2 - V
    cones = math.pi * r**2 * D / 3
    shape = vol - cones
    cyl = shape * 1.5
    r = (cyl / (2 * math.pi))**(1/3)
    print(2*r)

if __name__ == "__main__":
  main()
