# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/cookingwater

def main():
  n = int(input())
  possible = None
  for i in range(n):
    a, b = map(int, input().split())
    if i == 0:
      possible = set(range(a, b+1))
    else:
      possible &= set(range(a, b+1))
  if possible:
    print('gunilla has a point')
  else:
    print('edward is right')

if __name__ == "__main__":
  main()
