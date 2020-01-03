# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/platforme

def main():
  n = int(input())
  platforms = []
  left = float('inf')
  right = float('-inf')
  for i in range(n):
    y, x1, x2 = map(int, input().split())
    x2 -= 1
    left = min(left, x1)
    right = max(right, x2)
    platforms.append((y, x1, x2))
  platforms.sort()
  prev = [(0, -1, 1e9)]
  total = 0
  for p in platforms:
    y, x1, x2 = p
    left_done = False
    right_done = False
    for pp in reversed(prev):
      yp, xp1, xp2 = pp
      if not left_done:
        if x1 >= xp1 and x1 <= xp2:
          total += y - yp
          left_done = True
      if not right_done:
        if x2 >= xp1 and x2 <= xp2:
          total += y - yp
          right_done = True
    prev.append(p)

  print(total)

if __name__ == "__main__":
  main()
