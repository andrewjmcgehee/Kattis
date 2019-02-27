# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/redistribution
# Complexity: O(N log(N)) for N rooms
# Memory: O(N) for N rooms

class Room:
  def __init__(self, exams, index):
    self.exams = exams
    # for easy formatting later
    self.index = str(index+1)

  # for sorting
  def __lt__(self, other):
    return self.exams < other.exams

def main():
  n = int(input())
  exams = [int(x) for x in input().split()]
  rooms = []
  for i in range(n):
    rooms.append(Room(exams[i], i))
  # simply visit rooms with most exams first, then proceed to rooms
  # with least exams
  rooms.sort(reverse=True)

  # number of exams excluding first room
  total = 0
  for i in range(1, len(rooms)):
    total += rooms[i].exams

  # no safe order because there will be at least 1 exam which has
  # not been redistributed from the first room
  if rooms[0].exams > total:
    print('impossible')
  else:
    out = []
    for i in range(n):
      out.append(rooms[i].index)
    print(' '.join(out))


if __name__ == "__main__":
  main()
