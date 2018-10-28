def main():
  n = [int(x) for x in input().split('/')]
  a = n[0]
  b = n[1]

  a -= (32*b)

  a *= 5
  b *= 9

  negative = True if a < 0 else False
  if negative:
    a *= -1

  for i in range(2, 1001):
    while a % i == 0 and b % i == 0:
      a = a // i
      b = b // i

  if a == 0:
    b = 1
  if negative:
    a *= -1
  print(str(a) + '/' + str(b))

if __name__ == '__main__':
  main()


