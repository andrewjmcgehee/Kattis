# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/touchscreenkeyboard
# Complexity: O(N) for N characters
# Memory: O(N) for N chars in keyboard

# maps char to row, col
table = {
  'q': (0, 0),
  'w': (0, 1),
  'e': (0, 2),
  'r': (0, 3),
  't': (0, 4),
  'y': (0, 5),
  'u': (0, 6),
  'i': (0, 7),
  'o': (0, 8),
  'p': (0, 9),
  'a': (1, 0),
  's': (1, 1),
  'd': (1, 2),
  'f': (1, 3),
  'g': (1, 4),
  'h': (1, 5),
  'j': (1, 6),
  'k': (1, 7),
  'l': (1, 8),
  'z': (2, 0),
  'x': (2, 1),
  'c': (2, 2),
  'v': (2, 3),
  'b': (2, 4),
  'n': (2, 5),
  'm': (2, 6)
}

# returns the distance between two words
def get_distance(a, b):
  distance = 0
  for i in range(len(a)):
    r0, c0 = table[a[i]]
    rf, cf = table[b[i]]
    # manhattan distance
    distance += abs(cf - c0) + abs(rf - r0)
  return distance

def main():
  n = int(input())
  # tests
  for _ in range(n):
    output = []
    word1, m = (input().split())
    for i in range(int(m)):
      word2 = input()
      distance = get_distance(word1, word2)
      output.append((distance, word2))
    # sort outputs by distance away
    output.sort()
    for word in output:
      print(word[1], word[0])

if __name__ == '__main__':
  main()
