# Rating: ~ 4.9 / 10
# Link: https://open.kattis.com/problems/touchdown

def main():
  n = int(input())
  yards = [int(x) for x in input().split()]
  res = 'Nothing'
  pos = 20
  downs = 0
  progress = 0
  for gain in yards:
    pos += gain
    if pos >= 100:
      res = 'Touchdown'
      break
    elif pos <= 0:
      res = 'Safety'
      break
    downs += 1
    progress += gain
    if progress >= 10:
      downs = 0
      progress = 0
    if downs == 4:
      break
  print(res)


if __name__ == "__main__":
  main()
