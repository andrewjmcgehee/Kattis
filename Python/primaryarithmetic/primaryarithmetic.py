def main():
  while True:
    a, b = input().split()
    if a == b == '0':
      break
    a = [int(x) for x in a]
    b = [int(x) for x in b]

    while len(a) < len(b):
      a = [0] + a
    while len(b) < len(a):
      b = [0] + b

    carry = 0
    num_carries = 0
    for i in range(len(a)-1, -1, -1):
      if a[i] + b[i] + carry > 9:
        num_carries += 1
        carry = 1
      else:
        carry = 0

    if num_carries == 0:
      print('No carry operation.')
      continue
    if num_carries == 1:
      print('1 carry operation.')
      continue
    print('%i carry operations.' % num_carries)

if __name__ == '__main__':
  main()
