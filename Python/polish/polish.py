# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/polish
# Complexity: O(N) for N operands
# Memory: O(N) for N operands

def main():
  test = 1
  while True:
    try:
      line = input().split()
    except EOFError:
      break
    ops = {'+', '-', '*'}
    # stack to simulate post fix notation (very similar)
    res = []
    while line:
      # could be operand or operation
      x = line.pop()
      if x in ops:
        try:
          # apply operation to next two operands
          a = int(res[-1])
          b = int(res[-2])
          res.pop()
          res.pop()
          # put new representation of the number on the result
          if x == '*':
            c = a * b
            res.append(str(c))
          elif x == '+':
            c = a + b
            res.append(str(c))
          else:
            c = a - b
            res.append(str(c))
        # if both operands can't be popped, we may only have one operand left
        except:
          res.append(x)
      else:
        res.append(x)
    print("Case %i: %s" % (test, ' '.join(res[::-1])))
    test += 1

if __name__ == '__main__':
  main()


