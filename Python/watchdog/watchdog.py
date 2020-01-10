# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/watchdog

import math

def main():
  n = int(input())
  for _ in range(n):
    s, h = map(int, input().split())
    hatches = []
    hatch_set = set()
    for i in range(h):
      x, y = map(int, input().split())
      hatches.append((x, y))
      hatch_set.add((x, y))
    hatches.sort()
    found = None
    for x in range(s+1):
      for y in range(s+1):
        if (x, y) in hatch_set:
          continue
        worst = -1
        for h1 in hatches:
          dist = math.hypot(h1[0] - x, h1[1] - y)
          if dist > worst:
            worst = dist
        if x-worst >= 0 and x+worst <= s and y-worst >= 0 and y+worst <= s:
          found = (x, y)
          break
      if found:
        break
    if found:
      print(found[0], found[1])
    else:
      print('poodle')


if __name__ == "__main__":
  main()
