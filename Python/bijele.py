# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/bijele
# Complexity: O(1) since number of comparisons can be expressed as a constant
# Memory: O(1)

def main():
  ins = [int(x) for x in input().split()]
  expected = [1, 1, 2, 2, 2, 8]

  # get differences
  for i in range(len(ins)):
    ins[i] = expected[i] - ins[i]

  ins = [str(x) for x in ins]
  print(" ".join(ins))

if __name__ == '__main__':
    main()
