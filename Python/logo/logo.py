# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/logo
# Complexity: O(N) for N commands
# Memory: O(1)

import math

def main():
  cases = int(input())
  for _ in range(cases):
    commands = int(input())
    # start is arbitrary
    x = 0
    y = 0
    theta = 0
    for i in range(commands):
      cmd, val = input().split()
      val = int(val)
      # handle the command
      if cmd[0] == 'f':
        # r cos theta and r sin theta
        x += val * math.cos(math.radians(theta))
        y += val * math.sin(math.radians(theta))
      elif cmd[0] == 'b':
        # negative magnitude
        val *= -1
        x += val * math.cos(math.radians(theta))
        y += val * math.sin(math.radians(theta))
      elif cmd[0] == 'l':
        theta += val
      else:
        theta -= val
    # round the distance (which is just the hypotenuse)
    dist = math.hypot(x, y)
    print(round(dist))

if __name__ == "__main__":
  main()
