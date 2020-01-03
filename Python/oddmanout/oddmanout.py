# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/oddmanout

def main():
  x = int(input())
  for c in range(1, x+1):
    _ = input()
    g = [x for x in input().split()]
    freq = dict()
    for guest in g:
      freq[g.count(guest)] = guest
    print('Case #{}: {}'.format(c, freq[1]))

if __name__ == "__main__":
  main()
