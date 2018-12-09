# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/alldifferentdirections
# Complexity: O(N) for N different sets of directions
# Memory: O(N) for N destinations

import math

def main():
  while True:
    # break case
    n = int(input())
    if n == 0:
      break

    # all destinations
    total_x = []
    total_y = []

    for i in range(n):
      line = input().split()
      x, y = map(float, line[:2])
      theta = float(line[3])
      i = 4
      while i < len(line):
        if line[i] == 'walk':
          # r
          dist = float(line[i+1])
          # x = r cos theta (in radians)
          x += dist * math.cos(theta * math.pi / 180)
          # y = r sin theta (in radians)
          y += dist * math.sin(theta * math.pi / 180)
        elif line[i] == 'turn':
          # update theta (in degrees)
          theta += float(line[i+1])
        # all queries have 2 parts
        i += 2
      total_x.append(x)
      total_y.append(y)

    # get averages
    avg_x = sum(total_x) / len(total_x)
    avg_y = sum(total_y) / len(total_y)

    # best distance is 0
    worst = 0
    for i in range(len(total_x)):
      dist = math.hypot(total_x[i] - avg_x, total_y[i] - avg_y)
      worst = max(dist, worst)
    print(avg_x, avg_y, worst)

if __name__ == "__main__":
  main()
