# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/happyprime
# Complexity: O(sqrt(N) * E) for checking primality and where E is number of items in summing sequence
# Memory: O(1)

def is_happy(x):
  # happy is the sum of all the squares of its digits eventually hits 1
  # get all digits
  arr = [int(c) for c in str(x)]
  seen = set()
  num = x
  # if we get to a number weve seen before, its an infinite cycle
  while num not in seen:
    seen.add(num)
    # sum squares of digits
    new_num = 0
    for i in arr:
      new_num += i**2
    # get each digits
    arr = [int(c) for c in str(new_num)]
    num = new_num
  # once we reach the infinite bit, the num is either 1 or its not
  if num == 1:
    return True
  return False

def is_prime(x):
  # base cases
  if x == 0 or x == 1:
    return False
  # check all factors up to square root
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
    # check happy and prime
    if is_happy(k) and is_prime(k):
      res = 'YES'
    else:
      res = 'NO'
    print(m, k, res)

if __name__ == '__main__':
  main()
