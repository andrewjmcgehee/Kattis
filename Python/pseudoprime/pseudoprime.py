# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/pseudoprime

def prime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

def main():
  while True:
    p, a = map(int, input().split())
    if p == a == 0:
      break
    if not prime(p) and pow(a, p, p) == a:
      print('yes')
    else:
      print('no')

if __name__ == "__main__":
  main()
