# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/romans
# Complexity: O(1)
# Memory O(1)

def main():
  # get floating point inputs
  n = float(input())
  # multiply by scalar
  n = n * 1000.0 * 5280.0 / 4854.0
  # round
  print(int(n + 0.5))

if __name__ == '__main__':
  main()
