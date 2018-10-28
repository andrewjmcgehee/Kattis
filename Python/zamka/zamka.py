# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/zamka
# Complexity: O(NK) for N numbers to check with K digits to sum
# Memory: O(1)

# helper function for summing digits of a number
def get_sum(num):
  # list digits and convert to ints
  digs = [int(x) for x in str(num)]
  return sum(digs)

def main():
  lo = int(input())
  hi = int(input())
  target = int(input())
  # will hold smallest value with sum equal to target
  small = float('inf')
  # will hold large value wth sum equal to target
  large = -1
  for i in range(lo, hi+1):
    guess = get_sum(i)
    if guess == target:
      small = min(small, i)
      large = max(large, i)
  print(small)
  print(large)

if __name__ == '__main__':
    main()
