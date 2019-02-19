# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/dasblinkenlights
# Complexity: O(1)
# Memory: O(1)

def main():
  n, m, s = map(int, input().split())
  a = n
  b = m
  # get gcd by newtons method
  while b > 0:
    a, b = b, a % b
  gcd = a
  # calculate lcm with formula
  lcm = n * m / gcd
  if lcm != 0 and lcm <= s:
    print('yes')
  else:
    print('no')

if __name__ == "__main__":
  main()
