# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/persistent

def main():
  while True:
    x = int(input())
    if x == -1:
      break
    if x < 10:
      print(x+10)
      continue
    factors = []
    divisibile = True
    while x >= 10:
      divided = False
      for i in range(9, 2, -1):
        if x % i == 0:
          divided = True
          x //= i
          factors.append(i)
          break
      if not divided:
        divisibile = False
        break
    factors.append(x)
    if not divisibile:
      print('There is no such number.')
    else:
      factors.sort()
      for i in factors:
        print(i, end='')
      print()

if __name__ == "__main__":
  main()
