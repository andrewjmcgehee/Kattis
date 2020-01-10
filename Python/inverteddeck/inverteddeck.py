# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/inverteddeck

def main():
  _ = int(input())
  cards = [int(x) for x in input().split()]
  s = sorted(cards)
  l = 0
  r = len(cards)-1
  while l < len(cards) and cards[l] == s[l]:
    l += 1
  if l == len(cards):
    l, r = 0, 0
  else:
    while r >= l and cards[r] == s[r]:
      r -= 1
    mid = cards[l:r+1]
    mid = mid[::-1]
    new = cards[:l] + mid + cards[r+1:]
    if new != s:
      print('impossible')
      return
  print(l+1, r+1)

if __name__ == "__main__":
  main()
