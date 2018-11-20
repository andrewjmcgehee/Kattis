# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/rationalarithmetic
# Complexity: O(N) for N queries
# Memory O(1)

from fractions import Fraction

def main():
  t = int(input())
  for _ in range(t):
    # get fractions
    a, b, op, c, d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    # automatically reduced
    f1 = Fraction(a, b)
    f2 = Fraction(c, d)
    # handle each operation
    if op == "+":
      ans = f1 + f2
    elif op == "-":
      ans = f1 - f2
    elif op == "*":
      ans = f1 * f2
    else:
      # same as flipping and multiplying
      ans = f1 * Fraction(d, c)
    print(ans.numerator, '/', ans.denominator)

if __name__ == "__main__":
  main()
