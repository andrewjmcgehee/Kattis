# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/oddities
# Complexity: O(N) for N numbers
# Memory: O(1)

def main():
  n = int(input())

  for i in range(n):
    x = int(input())
    # bitwise even check
    if x & 1 == 0:
      print(x, ' is even')
      continue
    print(x, ' is odd')

if __name__ == '__main__':
  main()
