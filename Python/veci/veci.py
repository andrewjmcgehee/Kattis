# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/veci
# Complexity: O(N!) for N digits
# Memory: O(N!) for N digits (could be reduced with iterator)

import itertools

def main():
  num = input()
  # integer value
  a = int(num)
  # generate all permutations of number - max 6 digits
  perms = [''.join(x) for x in sorted(itertools.permutations(num))]
  for i in perms:
    # find first greater than
    if int(i) > a:
      print(i)
      return
  # found none
  print(0)

if __name__ == '__main__':
  main()



