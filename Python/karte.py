# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/karte
# Complexity: O(N) for N characters in string
# Memory: O(N) for N 3 character cards in string

def main():
  s = input()
  # tracks uniques
  cards = set()
  # tracks number missing from each suit
  P = 13
  K = 13
  H = 13
  T = 13
  # if we see a duplicate, flips to True
  greska = False

  for i in range(0, len(s), 3):
    # grab chunks of 3
    card = s[i:i+3]
    if card not in cards:
      cards.add(card)
    else:
      greska = True
      break
    if card[0] == 'P':
      P -= 1
    elif card[0] == 'H':
      H -= 1
    elif card[0] == 'K':
      K -= 1
    else:
      T -= 1

  if greska:
    print("GRESKA")
  else:
    print(P, K, H, T)

if __name__ == '__main__':
  main()
