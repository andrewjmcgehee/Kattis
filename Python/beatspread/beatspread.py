# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/beatspread
# Complexity: O(1)
# Memory: O(1)

def main():
  t = int(input())
  for _ in range(t):
    # sum and difference
    s, d = map(int, input().split())

    # a + b = s and a - b = d
    # therefore 2a = s + d or a = (s + d) / 2
    # int divide because points must be integer value
    a = (s + d) // 2
    b = a - d

    # seems redundant but effectively checks if a was truncated to an int
    # b obviously cannot be negative
    if 2*a == s + d and b >= 0:
      print(a, b)
    else:
      print('impossible')

if __name__ == '__main__':
  main()
