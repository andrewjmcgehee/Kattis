# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/primaryarithmetic
# Complexity: O(N) for N characters in string
# Memory: O(N) for N characters in string

def main():
  while True:
    a, b = input().split()
    # break case
    if a == b == '0':
      break
    # get list of digits
    a = [int(x) for x in a]
    b = [int(x) for x in b]

    # pad with 0s
    while len(a) < len(b):
      a = [0] + a
    while len(b) < len(a):
      b = [0] + b

    # keep track of carry
    carry = 0
    num_carries = 0
    for i in range(len(a)-1, -1, -1):
      # if over ten, carry operation
      if a[i] + b[i] + carry > 9:
        num_carries += 1
        carry = 1
      # reset carry
      else:
        carry = 0
    # handle output cases
    if num_carries == 0:
      print('No carry operation.')
      continue
    if num_carries == 1:
      print('1 carry operation.')
      continue
    print('%i carry operations.' % num_carries)

if __name__ == '__main__':
  main()
