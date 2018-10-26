# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/guessinggame
# Complexity: O(N) for N commands
# Memory: O(1)

def main():
  lo = 1
  hi = 10
  while True:
    guess = int(input())
    if guess == 0:
      break

    stan = input()
    if stan == 'too high':
      # only reset highest if narrowing range
      if guess <= hi:
        hi = guess-1
    elif stan == 'too low':
      # only reset lowest if narrowing range
      if guess >= lo:
        lo = guess+1
    else:
      # three bounds to check, inside lowest, outside highest, and impossible range
      if guess < lo or guess > hi or lo > hi:
        print('Stan is dishonest')
      else:
        print('Stan may be honest')
      # reset lo and hi for next game
      lo = 1
      hi = 10

if __name__ == '__main__':
  main()



