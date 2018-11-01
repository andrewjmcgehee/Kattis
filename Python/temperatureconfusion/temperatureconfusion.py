# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/temperatureconfusion
# Complexity: O(1)
# Memory: O(1)

def main():
  n = [int(x) for x in input().split('/')]
  a = n[0]
  b = n[1]

  # F = (9/5)C + 32 so if F is a/b then (5(a - 32b)) / 9b = C
  a -= (32*b)
  a *= 5
  b *= 9

  # lazy way to reduce fraction
  for i in range(2, 1001):
    while a % i == 0 and b % i == 0:
      a = a // i
      b = b // i
  # 0 must be reduced to 0 / 1
  if a == 0:
    b = 1
  print(str(a) + '/' + str(b))

if __name__ == '__main__':
  main()


