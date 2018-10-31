# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/bela
# Complexity: O(N) for N cards
# Memory: O(N) for N cards

def main():
  # map cards to dominant and non dominant values
  cards = {
    'A': (11, 11),
    'K': (4, 4),
    'Q': (3, 3),
    'J': (20, 2),
    'T': (10, 10),
    '9': (14, 0),
    '8': (0, 0),
    '7': (0, 0)
  }

  line = input().split()
  n = int(line[0])
  dominant = line[1]
  score = 0

  for i in range(4*n):
    # add appropriate value based on if dominant or not
    val, suit = list(input())
    if suit == dominant:
      score += cards[val][0]
    else:
      score += cards[val][1]
  print(score)

if __name__ == '__main__':
  main()
