# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/pieceofcake2

def main():
  n, h, v = map(int, input().split())
  d = 4
  w = [n-h, h]
  l = [n-v, v]
  best = -1
  for i in w:
    for j in l:
      best = max(best, 4*i*j)
  print(best)

if __name__ == "__main__":
  main()
