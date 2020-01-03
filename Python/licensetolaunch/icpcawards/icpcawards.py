# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/icpcawards

def main():
  n = int(input())
  winners = []
  used = set()
  for i in range(n):
    uni, team = input().split()
    if uni in used:
      continue
    used.add(uni)
    winners.append(' '.join([uni, team]))
    if len(winners) == 12:
      break
  for w in winners:
    print(w)

if __name__ == "__main__":
  main()
