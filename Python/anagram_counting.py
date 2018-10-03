# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/anagramcounting
# Complexity: O(N) to calculate N! (could be potentially larger due to big integers)
# Memory: O(N) where N is number of characters

import fileinput

# helper for calculating factorial of a number
def factorial(num):
  multiplier = 2
  f = 1
  while multiplier <= num:
    f *= multiplier
    multiplier += 1
  return f

# for non unique values divide by K! where K is the number
# of times that character occurs
def count_anagrams(numerator, char_map):
  denominator = 1
  for val in char_map.values():
    if val > 1:
      denominator *= factorial(val)
  return numerator // denominator

def main():
  for line in fileinput.input():
    char_map = dict()
    num_chars = len(line.strip())
    for char in line:
      if char not in char_map:
        char_map[char] = 0
      char_map[char] += 1
    # numerator is factorial of all characters, denominator is handled
    # specially as defined above
    numerator = factorial(num_chars)
    count = count_anagrams(numerator, char_map)
    print(count)

if __name__ == '__main__':
    main()

