def main():
  test = 1
  while True:
    try:
      line = input().split()
    except EOFError:
      break
    ops = {'+', '-', '*'}
    res = []
    while line:
      x = line.pop()
      if x in ops:
        try:
          a = int(res[-1])
          b = int(res[-2])
          res.pop()
          res.pop()
          if x == '*':
            c = a * b
            res.append(str(c))
          elif x == '+':
            c = a + b
            res.append(str(c))
          else:
            c = a - b
            res.append(str(c))
        except:
          res.append(x)
      else:
        res.append(x)
    print("Case %i: %s" % (test, ' '.join(res[::-1])))
    test += 1

if __name__ == '__main__':
  main()


