# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/spavanac
# Complexity: O(
# Memory: O(

def main():
  h, m = map(int, input().split())
  # subtract 45 minutes
  m -= 45

  # borrow an hour
  if m < 0:
    m += 60
    h -= 1
    # borrow a day
    if h < 0:
      h = 23
  print(h, m)

if __name__ == '__main__':
  main()
