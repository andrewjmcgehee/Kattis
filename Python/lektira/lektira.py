# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/lektira
# Complexity: O(N^2) for N letters in string (not including concatenations)
# Memory: O(1)

def main():
  s = input()
  # current best string is the string itself
  best = s
  for i in range(1, len(s)):
    # get first division
    a = s[:i]
    for j in range(i+1, len(s)):
      # get second and third division
      b = s[i:j]
      c = s[j:]
      # check edge case of empty string
      if len(b) == 0 or len(c) == 0:
        continue
      # reverse and join
      tmp = a[::-1] + b[::-1] + c[::-1]
      # take lexicographically smallest
      if tmp < best:
        best = tmp
  print(best)

if __name__ == "__main__":
  main()
