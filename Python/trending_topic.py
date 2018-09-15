# Rating: ~ 5.8 / 10
# Link: https://open.kattis.com/problems/trendingtopic
# Complexity: O(n) to read in and update words
# Memory: O(n) where n is number of unique words

def main():
  day = 0
  words = [[] for i in range(7)]
  freq = dict()
  trending = dict()

  while True:
    # exit on EOF
    try:
      s = input()
    except EOFError:
      break

    if s == "<text>":
      for word in words[day]:
        if word in freq:
          freq[word] -= 1
        if freq[word] == 0:
          del freq[word]
      words[day] = []

      line = input()
      while line != "</text>":
        line = line.split()
        for word in line:
          if len(word) < 4:
            continue
          # add to given day
          words[day].append(word)
          # increment frequency of word
          if word not in freq:
            freq[word] = 0
          freq[word] += 1
        line = input()
      # cycle through days array
      day = (day+1) % 7
    elif s.startswith("<top"):
      n = int(s.split()[1])
      trending.clear()

      # map a frequency to a set of words
      for key in freq:
        value = freq[key]
        if value > 0:
          if value not in trending:
            trending[value] = set()
          trending[value].add(key)

      num_seen = 0
      print("<top %i>" % n)
      keys = sorted(trending.keys())[::-1]
      for key in keys:
        if num_seen >= n:
          break
        # tricky wording here. If we have seen more than 5 words, and we are looking for
        # the top 5, we are done - even if we have only seen one distinct frequency.
        # (i.e. if we have 6 words that start appear 2 times, and 1 that appears 1 time
        # we only need to print all 6 of the 2's for the top 5. We have seen at least 5
        # of the top occuring words and it does not matter that we havent seen 5 distinct
        # frequencies
        for word in sorted(trending[key]):
          print("%s %i" % (word, key))
          num_seen += 1
      print("</top>")

if __name__ == '__main__':
  main()

