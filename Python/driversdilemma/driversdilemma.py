# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/driversdilemma

def main():
  c, x, m = map(float, input().split())
  c /= 2
  best = -1
  mpgs = []
  for i in range(6):
    _, mpg = map(float, input().split())
    mpgs.append(mpg)

  mph = 80
  for mpg in reversed(mpgs):
    hours = m / mph
    if c - m / mpg - x * hours > 0:
      print('YES', mph)
      return
    mph -= 5
  print('NO')


if __name__ == "__main__":
  main()
