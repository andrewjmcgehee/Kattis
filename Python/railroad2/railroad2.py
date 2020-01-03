# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/railroad2

def main():
  x, y = map(int, input().split())
  if y & 1:
    print('impossible')
  else:
    print('possible')

if __name__ == "__main__":
  main()
