# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/engineeringenglish
# Complexity: O(N) for N words
# Memory: O(N) for N words

def main():
  # track words used
  used = set()
  lines = []
  # get input to EOF
  while True:
    try:
      line = input()
      lines.append(line)
    except EOFError:
      break
  output = []
  for line in lines:
    # build the new engineered line
    new_line = []
    for word in line.split():
      # make certain the word is added in lowercase to avoid case issues
      if word.lower() not in used:
        used.add(word.lower())
        # but append the unedited word
        new_line.append(word)
      else:
        # seen before so add a dot
        new_line.append('.')
    # space separate word
    output.append(' '.join(new_line))
  # line separate sentences
  print('\n'.join(output))


if __name__ == "__main__":
  main()
