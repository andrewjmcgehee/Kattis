# Rating: ~ 3.6 / 10
# Link: https://open.kattis.com/problems/selfsimilarstrings
# Complexity: O(N^2) for N characters in string
# Memory: O(N) for N tokens of length K in string of N characters

import fileinput

def main():
  for line in fileinput.input():
    length = len(line)
    # the maximum degree of self similarity
    max_degree = 0
    similar = True
    while similar:
      # try next highest degree
      degree = max_degree + 1
      # track frequency of substrings
      tokens = dict()
      # try each sub string of that length
      for i in range(length - degree):
        token = line[i:i+degree]
        if token not in tokens:
          tokens[token] = 0
        tokens[token] += 1
      for val in tokens.values():
        # not repeated at least once
        if val < 2:
          similar = False
          break
      if similar:
        max_degree = degree
    print(max_degree)

if __name__ == '__main__':
    main()
