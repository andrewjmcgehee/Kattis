table = [
  {
    'q': 0,
    'w': 1,
    'e': 2,
    'r': 3,
    't': 4,
    'y': 5,
    'u': 6,
    'i': 7,
    'o': 8,
    'p': 9
  },
  {
    'a': 0,
    's': 1,
    'd': 2,
    'f': 3,
    'g': 4,
    'h': 5,
    'j': 6,
    'k': 7,
    'l': 8
  },
  {
    'z': 0,
    'x': 1,
    'c': 2,
    'v': 3,
    'b': 4,
    'n': 5,
    'm': 6
  }
]


def main():
  n = int(raw_input())

  for i in range(n):
    output = []
    word1, m = (raw_input().split())
    for i in xrange(int(m)):
      word2 = raw_input()
      distance = get_distance(word1, word2)
      output.append((distance, word2))
    output.sort()
    for i in output:
      print i[1], i[0]

def get_distance(a, b):
  distance = 0
  for i in xrange(len(a)):
    distance += distance_helper(a[i], b[i])
  return distance

def distance_helper(a, b):
  a_row = -1
  b_row = -1
  for i in xrange(3):
    if a in table[i]:
      a_row = i
    if b in table[i]:
      b_row = i
  return abs(table[a_row][a] - table[b_row][b]) + abs(a_row - b_row)

if __name__ == '__main__':
  main()
