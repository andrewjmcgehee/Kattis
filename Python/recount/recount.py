# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/recount

import sys

def main():
  lines = [l.strip() for l in sys.stdin.readlines()]
  # get rid of unnecessary end line
  lines.pop()
  # track votes
  count = dict()
  for line in lines:
    if line not in count:
      count[line] = 0
    count[line] += 1
  # reverse dict to see if recount needed
  tallies = dict()
  max_votes = 0
  for name in count:
    votes = count[name]
    max_votes = max(max_votes, votes)
    # see if non distinct with set
    if votes not in tallies:
      tallies[votes] = set()
    tallies[votes].add(name)
  # output answer
  if len(tallies[max_votes]) == 1:
    name = list(tallies[max_votes]).pop()
    print(name)
  else:
    print("Runoff!")

if __name__ == "__main__":
  main()
