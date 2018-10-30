# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/zigzag
# Complexity: O(1)
# Memory: O(1)

def main():
  n = int(input())
  # maximum difference is 25. this tells us the number of chars we need
  num_chars = (n-1) // 25 + 2
  # always start on a. starting on any other letter has an equivalent
  # which starts on a
  ans = ['a']

  # trivial case
  if num_chars == 2:
    ans.append(chr(97 + n))
  # even number of letters
  elif num_chars & 1 == 0:
    # second character starts at z
    second = 25
    # last character starts a distance away from a
    last = (n-1) % 25 + 1
    # second must be at least b
    while second > 0 and last < 24:
      # for every 1 that we decrement second, last gains 2
      second -= 1
      last += 2
    # build the string
    ans.append(chr(97 + second))
    for i in range(2, num_chars-1):
      if i & 1:
        ans.append('z')
      else:
        ans.append('a')
    ans.append(chr(97 + last))
  else:
    # second starts at z
    second = 25
    # last starts a distance away from z
    last = 25 - ((n-1) % 25 + 1)
    while second > 0 and last > 1:
      # for every 1 that we decrement second, last loses 2
      second -= 1
      last -= 2
    # build the string
    ans.append(chr(97 + second))
    for i in range(2, num_chars-1):
      if i & 1:
        ans.append('z')
      else:
        ans.append('a')
    ans.append(chr(97 + last))
  print(''.join(ans))

if __name__ == '__main__':
  main()
