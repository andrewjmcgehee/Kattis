# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/eventplanning

def main():
  n, b, h, w = map(int, input().split())
  hotels = []
  for _ in range(h):
    p = int(input())
    beds = [int(x) for x in input().split()]
    hotels.append((p, beds))
  hotels.sort()

  best = None
  for hotel in hotels:
    price, beds = hotel
    for i in range(w):
      if beds[i] >= n and price * n <= b:
        if best is None:
          best = price*n
        else:
          best = min(best, price*n)
  if best is None:
    print('stay home')
  else:
    print(best)





if __name__ == "__main__":
  main()
