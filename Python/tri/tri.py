# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/tri

def main():
  a, b, c = map(int, input().split())
  u, v, w = str(a), str(b), str(c)
  if a + b == c:
    print(u + '+' + v + '=' + w)
  elif a - b == c:
    print(u + '-' + v + '=' + w)
  elif a * b == c:
    print(u + '*' + v + '=' + w)
  elif a / b == c:
    print(u + '/' + v + '=' + w)
  elif a == b + c:
    print(u + '=' + v + '+' + w)
  elif a == b - c:
    print(u + '=' + v + '-' + w)
  elif a == b * c:
    print(u + '=' + v + '*' + w)
  elif a == b / c:
    print(u + '=' + v + '/' + w)

if __name__ == "__main__":
  main()
