# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/planina
# Complexity: O(1)
# Memory: O(1)

def main():
  # sides follow powers of 2 plus 1
  i = int(input())
  side = 2**i + 1
  print(side**2)

if __name__ == '__main__':
  main()

