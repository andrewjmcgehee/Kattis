# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/pokerhand


def main():
  hand = [x[0] for x in input().split()]
  ans = []
  for h in hand:
    ans.append((hand.count(h), h))
  ans.sort(reverse=True)
  print(ans[0][0])

if __name__ == "__main__":
  main()
