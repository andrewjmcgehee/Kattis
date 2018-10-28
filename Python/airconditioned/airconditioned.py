# Rating: ~ 4.6 / 10
# Link: https://open.kattis.com/problems/airconditioned
# Complexity: O(N log(N)) for sorting
# Memory: O(N) for N minions

def main():
  # num minions
  n = int(input())
  minions = []
  # minion represented as tuple of (hi temp, lo temp)
  for i in range(n):
    lo, hi = map(int, input().split())
    minions.append((hi, lo))
  # sort minions, this will put the minions with the lowest high temp first
  minions.sort()
  # track rooms used
  rooms = set()
  for m in minions:
    has_room = False
    # try all the rooms in the range
    for i in range(m[1], m[0]+1):
      # if a room exists that satisfies this minion do nothing
      if i in rooms:
        has_room = True
        break
    # otherwise choose the highest room this minion will tolerate (greedy)
    if not has_room:
      rooms.add(m[0])
  print(len(rooms))


if __name__ == '__main__':
  main()
