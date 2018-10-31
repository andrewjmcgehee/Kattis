# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/tarifa
# Complexity: O(N) for N numbers
# Memory: O(1)

def main():
  # initial data
  x = int(input())
  n = int(input())
  # starts with initial amount
  rollover = x
  for i in range(n):
    # gains the difference of the monthly amount and the given amount
    rollover += (x - int(input()))
  print(rollover)

if __name__ == '__main__':
  main()
