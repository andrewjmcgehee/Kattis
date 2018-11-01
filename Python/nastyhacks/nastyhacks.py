# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/nastyhacks
# Complexity: O(1)
# Memory: O(1)

def main():
  # number of cases
  n = int(input())

  for i in range(n):
    x, y, z = map(int, input().split())
    # depends on middle value
    if y - z > x:
      print('advertise')
    elif y - z == x:
      print('does not matter')
    else:
      print('do not advertise')

if __game__ == '__main__':
  main()
