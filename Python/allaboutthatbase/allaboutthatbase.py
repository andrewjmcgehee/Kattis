# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/allaboutthatbase
# Complexity: O(
# Memory: O(

# populate mapping of bases
bases = dict()
for i in range(10):
  bases[str(i)] = i
# 97 = 'a' in ASCII
for i in range(97, 97+26):
  bases[chr(i)] = i - 87

def main():
  t = int(input())
  for _ in range(t):
    expr = input().split()
    # operation symbol
    op = expr[1]
    # terms in different base
    terms = [expr[0], expr[2], expr[4]]

    # minimum base require is 1 greater than the highest symbol in the number
    min_base = 1
    # get unique symbols
    symbols = set()
    for term in terms:
      for char in term:
        symbols.add(char)
        min_base = max(min_base, bases[char])
    if len(symbols) != 1:
      min_base += 1

    # try every base
    valid_bases = []
    for i in range(min_base, 37):
      base = i
      # term 1
      a = 0
      term = terms[0]
      for j in range(len(term)-1, -1, -1):
        a += bases[term[j]] * (base**(len(term)-j-1))

      # term 2
      b = 0
      term = terms[1]
      for j in range(len(term)-1, -1, -1):
        b += bases[term[j]] * (base**(len(term)-j-1))
      # solution
      c = 0
      term = terms[2]
      for j in range(len(term)-1, -1, -1):
        c += bases[term[j]] * (base**(len(term)-j-1))

      # check validity of expression
      if op == '+':
        if a + b == c:
          valid_bases.append(base)
      elif op == '-':
        if a - b == c:
          valid_bases.append(base)
      elif op == '*':
        if a * b == c:
          valid_bases.append(base)
      else:
        if a / b == c:
          valid_bases.append(base)

    # print valid bases
    if valid_bases:
      for i in range(len(valid_bases)):
        base = valid_bases[i]
        if base < 10:
          valid_bases[i] = str(base)
        elif base == 36:
          valid_bases[i] = '0'
        else:
          valid_bases[i] = chr(base + 87)
      print(''.join(valid_bases))
    else:
      print('invalid')

if __name__ == '__main__':
  main()
