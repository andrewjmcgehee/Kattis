# Rating: ~ 4.1 / 10
# Link: https://open.kattis.com/problems/zipfsong
# Complexity: O(N log(N)) for N songs
# Memory: O(N) for N songs

class Song:
  def __init__(self, factor, index, name):
    self.factor = factor
    self.index = index
    self.name = name

  # define comparator to sort by factor then index
  def __lt__(self, other):
    if self.factor == other.factor:
      return self.index < other.index
    return self.factor > other.factor

def main():
  n, m = map(int, input().split())

  # holds all the songs
  songs = []
  for i in range(1, n+1):
    line = input().split()
    # number of plays
    plays = int(line[0])
    name = line[1]
    # each values weight is i times more weighty
    factor = plays * i
    s = Song(factor, i, name)
    songs.append(s)
  # sort
  songs.sort()
  # print queries
  for i in range(m):
    print(songs[i].name)


if __name__ == '__main__':
  main()
