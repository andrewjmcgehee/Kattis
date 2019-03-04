# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/hardwoodspecies
# Complexity: O(N log(N)) for sorting N species
# Memory: O(N) for N species

# faster io
from sys import stdin, stdout

def main():
  freq = dict()
  # load all lines into memory
  lines = stdin.readlines()
  # total trees is number of lines
  total = len(lines)
  for species in lines:
    # get rid of new line chars
    species = species.strip()
    # traq frequency of occurence
    if species not in freq:
      freq[species] = 0
    freq[species] += 1
  # sort and output
  for key in sorted(freq.keys()):
    stdout.write(key + ' ' + '%.6f' % (freq[key] / total * 100) + '\n')

if __name__ == "__main__":
  main()
