

def main():
  word = input()
  freq = dict()
  for char in word:
    if char not in freq:
      freq[char] = 0
    freq[char] += 1

  if len(freq.keys()) <= 2:
    print(0)
  else:
    chars = [(key, freq[key]) for key in sorted(freq, key=freq.get)]
    letters = 0
    while len(chars) > 2:
      letters += chars[0][1]
      del chars[0]

    print(letters)

if __name__ == '__main__':
  main()
