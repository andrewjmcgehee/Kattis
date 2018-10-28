def main():
  a, b = [int(x) for x in raw_input().split()]
  m, s = [int(x) for x in raw_input().split()]

  best_rent = 0
  for i in xrange(1, m):
    x = i
    y = m-i
    if (2*x + y) < s:
      continue
    best_rent = max(best_rent, a*x + b*y)
  print best_rent

if __name__ == '__main__':
  main()
