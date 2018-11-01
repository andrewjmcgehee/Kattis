# Rating: ~ 1.7 / 10
# Link: https://open.kattis.com/problems/keytocrypto
# Complexity: O(
# Memory: O(


def main():
  # maps character to integer
  shifts = { chr(i+65):i for i in range(26) }
  cipher = input()
  # will progressively append to end
  keytxt = list(input())

  # will join at end
  ans = []
  for i in range(len(cipher)):
    # shift char
    res = ord(cipher[i]) - shifts[keytxt[i]]
    # check shifted to far
    if res < ord('A'):
      res += 26
    # add to key and to answer
    keytxt.append(chr(res))
    ans.append(chr(res))
  print(''.join(ans))

if __name__ == '__main__':
    main()
