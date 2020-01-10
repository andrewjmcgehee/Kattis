# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/triangleornaments

import math

def angle(a, b, c):
  return math.acos((b**2 + c**2 - a**2)/(2*b*c))

def width(a, b, c):
  a_angle = angle(a, b, c)
  b_angle = angle(b, c, a)
  A = (-a*math.cos(b_angle), a*math.sin(b_angle))
  B = (b*math.cos(a_angle), b*math.sin(a_angle))
  C = (0,0)
  centr_x = (A[0] + B[0] + C[0])/3
  centr_y = (A[1] + B[1] + C[1])/3
  ang = math.atan2(centr_y, centr_x)
  ang -= math.pi/2
  return c * math.cos(ang)

def main():
  n = int(input())
  total = 0
  for _ in range(n):
    a, b, c = map(float, input().split())
    total += width(a, b, c)
  print(total)

if __name__ == "__main__":
  main()
