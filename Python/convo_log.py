# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/conversationlog
# Complexity: O(N) for N total words
# Memory: O(N) for N total words

word_freq = dict()
uniques = set()
users = dict()

# custom class to sort tuples by higher frequency and then alphabetically
class Word:
  def __init__(self, freq, word):
    self.freq = freq
    self.word = word

  def __lt__(self, other):
    if self.freq == other.freq:
      return self.word < other.word
    return self.freq > other.freq

def main():
  global uniques, word_freq
  n = int(input())

  for i in range(n):
    line = input().split()
    name = line[0]
    sentence = line[1:]
    # add the user if not seen before
    if name not in users:
      users[name] = set()

    # count frequency of word and add words to set at the users name
    # and uniques set which will contain all words for now
    for word in sentence:
      if word not in word_freq:
        word_freq[word] = 0
      word_freq[word] += 1
      users[name].add(word)
      uniques.add(word)

  # get intersect of universal set and each users set
  for name in users:
    uniques &= users[name]

  # append Word objects for each unique word remaining
  result = []
  for word in uniques:
    val = word_freq[word]
    result.append(Word(val, word))

  # if the array is empty, there were no words used by all
  if result:
    # sorted will use the __lt__ method we defined earlier
    for i in sorted(result):
      print(i.word)
  else:
    print("ALL CLEAR")

if __name__ == '__main__':
  main()
