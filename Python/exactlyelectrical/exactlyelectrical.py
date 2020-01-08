# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/exactlyelectrical

def main():
  a, b = map(int, input().split())
  c, d = map(int, input().split())
  t = int(input())
  manhattan = abs(a-c) + abs(b-d)
  if t < manhattan:
    print('N')
    return
  if t == manhattan:
    print('Y')
    return
  t -= manhattan
  if t & 1:
    print('N')
  else:
    print('Y')


if __name__ == "__main__":
  main()
