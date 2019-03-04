# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/esej
# Complexity: O(N) for N words generated
# Memory: O(N) for N words generated

# gets first n permutations of 4 letters
def get_combinations(n):
  words = []
  letters = ['a', 'a', 'a', 'a']
  for i in range(26):
    letters[0] = chr(97 + i)
    for j in range(26):
      letters[1] = chr(97 + j)
      for k in range(26):
        letters[2] = chr(97 + k)
        for l in range(26):
          letters[3] = chr(97 + l)
          words.append(''.join(letters))
          if len(words) == n:
            return words

def main():
  a, b = map(int, input().split())
  # just use permutations of 4 letter strings because 26^4 > 100,000
  # so all words will be unique

  # must take max of a and b / 2 because a could be greater
  n = max(a, b // 2)
  words = get_combinations(n)
  print(' '.join(words))


if __name__ == "__main__":
  main()
