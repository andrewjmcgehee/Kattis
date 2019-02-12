# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/kleptography
# Complexity: O(N) for N characters
# Memory: O(N) for N characters

def main():
  n, m = map(int, input().split())
  a = input()
  b = input()
  out = list(b)

  # only need to do n iterations
  for i in range(n):
    # follow a chain to the beginning of the word
    start = m-i-1
    while start >= 0:
      # first case handled differently
      first = True
      if first:
        first = False
        # get distance
        res = ord(b[start]) - ord(a[n-i-1])
        # same effect as mod 26
        if res < 0:
          res += 26
        # move back n letters (the char we just solved for)
        start -= n
        out[start] = chr(97 + res)
      else:
        res = ord(b[start]) - ord(out[start])
        if res < 0:
          res += 26
        start -= n
        out[start] = chr(97 + res)
  # last characters will be unsolved
  for i in range(n):
    out[m-n+i] = a[i]
  print(''.join(out))


if __name__ == "__main__":
  main()
