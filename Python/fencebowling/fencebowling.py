# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/fencebowling

import math

def get_final_pos(k, l, w, alpha):
  if alpha == 90:
    return 0
  if alpha == 0:
    return float('inf')
  alpha = math.radians(alpha)
  adj = w/2
  horizontal = 0
  while True:
    dist = adj * math.tan(alpha)
    if l - dist <= 0:
      break
    l -= dist
    horizontal += adj
    alpha = math.atan(2 * math.tan(alpha))
    adj = w
  cross = l / math.tan(alpha)
  return horizontal + cross

def main():
  k, w, l = map(int, raw_input().split())
  goal = w * k
  lo = 0
  hi = 90
  angle = None
  while abs(lo - hi) > 1e-6:
    angle = (lo + hi)/2
    res = get_final_pos(k, l, w, angle)
    if res < goal:
      hi = angle
    elif res > goal:
      lo = angle
    else:
      break
  print(angle)

if __name__ == "__main__":
  main()
