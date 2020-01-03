# parket
# 2.6

def main():
  r, b = map(int, input().split())
  i = 1
  while i <= b**0.5:
    if b % i == 0:
      l, w = i, b // i
      if 2 * (l+2) + 2 * w == r:
        print(max(l, w)+2, min(l, w)+2)
        break
    i += 1


if __name__ == '__main__':
  main()
