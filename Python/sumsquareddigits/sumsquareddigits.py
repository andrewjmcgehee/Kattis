# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/sumsquareddigits

def ssd(b, n):
  total = 0
  while n:
    mod = n % b
    total += mod**2
    n = n // b
  return total

def main():
  x = int(input())
  for i in range(x):
    k, b, n = map(int, input().split())
    print(k, ssd(b, n))

if __name__ == "__main__":
  main()
