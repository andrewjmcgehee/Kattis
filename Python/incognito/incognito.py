# Rating: ~ 2.9
# Link: https://open.kattis.com/problems/incognito
# Complexity: O(N) for N articles of clothing
# Memory: O(N) for N articles of clothing

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())

    # stored types of clothing
    categories = dict()
    # add all clothing to map
    for i in range(n):
      piece, cat = input().split()
      if cat not in categories:
        # only track distinct items
        categories[cat] = set()
      categories[cat].add(piece)
    # initial 1 so we can multiply
    num = 1
    for k, v in categories:
      # add 1 to length to signify not wearing that item
      num *= (len(v) + 1)
    # subtract 1 from earlier
    num -= 1
    print(num)

if __name__ == '__main__':
  main()

