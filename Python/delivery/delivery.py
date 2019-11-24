# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/delivery

from collections import deque

def main():
  n, k = map(int, input().split())
  left = deque()
  right = deque()
  for i in range(n):
    x, p = map(int, input().split())
    if x < 0:
      left.append((-x, p))
    else:
      right.append((x, p))
  right.reverse()

  dist = 0
  # handle left
  while left:
    dist += 2 * left[0][0]
    letters = k
    while left and letters:
      x, l = left[0]
      if letters >= l:
        letters -= l
        left.popleft()
      else:
        left[0] = (x, l - letters)
        letters = 0
  while right:
    dist += 2 * right[0][0]
    letters = k
    while right and letters:
      x, l = right[0]
      if letters >= l:
        letters -= l
        right.popleft()
      else:
        right[0] = (x, l - letters)
        letters = 0
  print(dist)


if __name__ == "__main__":
  main()
