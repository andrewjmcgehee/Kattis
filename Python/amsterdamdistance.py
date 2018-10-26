# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/amsterdamdistance
# Complexity: O(1)
# Memory: O(1)

import math

def main():
  n, m, r = [float(x) for x in input().split()]
  # number of pie slices
  n = int(n)
  # number of rings
  m = int(m)

  # angle of one pie slice in radians
  seg_angle = math.pi / n
  # length in between each ring
  seg_len = r / m

  a_col, a_row, b_col, b_row = [int(x) for x in input().split()]
  delta_row = abs(a_row - b_row)
  delta_col = abs(a_col - b_col)

  # arc length is angle in radians times the radius
  arc_len_1 = a_row * seg_len * seg_angle * delta_col
  arc_len_2 = b_row * seg_len * seg_angle * delta_col

  # best distance is one of three things:
  #   - handle row, then col
  #   - handle col, then row
  #   - go through the origin of the circle

  dist = arc_len_1 + seg_len * delta_row
  dist = min(dist, arc_len_2 + seg_len * delta_row)
  dist = min(dist, (a_row + b_row) * seg_len)
  print(dist)

if __name__ == '__main__':
  main()
