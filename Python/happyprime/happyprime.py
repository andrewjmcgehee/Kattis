def is_happy(x):
  arr = [int(c) for c in str(x)]
  seen = set()
  num = x
  while num not in seen:
    seen.add(num)
    new_num = 0
    for i in arr:
      new_num += i**2
    arr = [int(c) for c in str(new_num)]
    num = new_num
  if num == 1:
    return True
  return False

def is_prime(x):
  if x == 0 or x == 1:
    return False

  i = 2
  while i*i <= x:
    if x % i == 0:
      return False
    i += 1
  return True

def main():
  n = int(input())
  for _ in range(n):
    m, k = map(int, input().split())
    res = None
    if is_happy(k) and is_prime(k):
      res = 'YES'
    else:
      res = 'NO'
    print(m, k, res)

if __name__ == '__main__':
  main()
