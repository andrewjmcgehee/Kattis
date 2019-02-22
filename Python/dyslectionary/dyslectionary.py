# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/dyslectionary
# Complexity: O(N log(N) + NK) to reverse N words of length K and sort them
# Memory: O(N) for N words

# helper function to format words correctly for output
def dyslect(words):
  # need maximum length to determine padding for spaces
  max_len = 0
  for word in words:
    max_len = max(max_len, len(word))
  # words are already reversed so padding will go on the end (which will
  # become the beginning
  for i, word in enumerate(words):
    word += ' ' * (max_len - len(word))
    words[i] = word[::-1]
  return words

def main():
  words = []
  while True:
    try:
      # remove previous result
      words.clear()
      while True:
        word = input()
        # new line so next case
        if not word:
          break
        words.append(word[::-1])
      words.sort()
      words = dyslect(words)
      print('\n'.join(words))
      # new line in between cases
      print()
    except EOFError:
      # handle final case at EOF
      words.sort()
      words = dyslect(words)
      print('\n'.join(words))
      break

if __name__ == "__main__":
  main()
