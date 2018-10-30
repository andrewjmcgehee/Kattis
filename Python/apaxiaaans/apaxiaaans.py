# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/apaxiaaans
# Complexity: O(N) for N characters
# Memory: O(N) for N characters

def main():
  s = input()
  # first character always included
  ans = [s[0]]
  for i in range(1, len(s)):
    # check if this character not equal to previous character
    if s[i] != s[i-1]:
      ans.append(s[i])
  print(''.join(ans))

if __name__ == '__main__':
  main()
