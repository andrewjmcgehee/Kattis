# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/simplicity
# Complexity: O(N log(N)) to sort N characters in string
# Memory: O(N) for N characters in string

def main():
  word = input()
  # track the freqency of characters
  freq = dict()
  for char in word:
    if char not in freq:
      freq[char] = 0
    freq[char] += 1

  # only 2 unique characters in string
  if len(freq.keys()) <= 2:
    print(0)
  else:
    # get tuples of key and value and sort by values
    chars = [(key, freq[key]) for key in sorted(freq, key=freq.get)]
    letters = 0
    # get rid of fewest chars possible until only 2 unique chars
    while len(chars) > 2:
      # like popping from a queue
      letters += chars[0][1]
      del chars[0]
    print(letters)

if __name__ == '__main__':
  main()
