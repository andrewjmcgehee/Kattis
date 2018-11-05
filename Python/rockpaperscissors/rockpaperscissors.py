# Rating: ~ 4.4 / 10
# Link: https://open.kattis.com/problems/rockpaperscissors
# Complexity: O(N) for N matches
# Memory: O(N) for N players

def main():
  while True:
    line = raw_input()
    if line[0] == '0':
      break

    n, k = map(int, line.split())

    if n == 1:
      print '-'
      continue

    wins = dict()
    losses = dict()
    for i in xrange(1, n+1):
      wins[i] = 0
      losses[i] = 0

    for i in xrange(k * n * (n-1) / 2):
      match = raw_input().split()
      # player number
      p1 = int(match[0])
      # get first char of play
      m1 = match[1][0]
      p2 = int(match[2])
      m2 = match[3][0]
      # check each possibility
      # rock
      if m1 == 'r':
        # against paper
        if m2 == 'p':
          wins[p2] += 1
          losses[p1] += 1
        # against scissors
        elif m2 == 's':
          wins[p1] += 1
          losses[p2] += 1
      # paper
      elif m1 == 'p':
        # against scissors
        if m2 == 's':
          wins[p2] += 1
          losses[p1] += 1
        # against rock
        elif m2 == 'r':
          wins[p1] += 1
          losses[p2] += 1
      # scissors
      else:
        # against rock
        if m2 == 'r':
          wins[p2] += 1
          losses[p1] += 1
        # against paper
        elif m2 == 'p':
          wins[p1] += 1
          losses[p2] += 1

    for i in xrange(1, n+1):
      # undefined
      if wins[i] + losses[i] == 0:
        print '-'
        continue
      print "%.3f" % (wins[i] / float(wins[i] + losses[i]))

if __name__ == '__main__':
    main()

