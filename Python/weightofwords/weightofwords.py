# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/weightofwords
# Complexity: O(N) for N characters in length
# Memory: O(N) for N character in length

def get_weight(arr):
  weight = 0
  for char in arr:
    weight += ord(char)-96
  return weight

def main():
  l, weight = map(int, input().split())
  # trivial case
  if weight > 26*l:
    print('impossible')
    return

  # greedy strategy
  # use 'z' until unable to do so anymore
  ans = []
  length = l
  for i in range(l):
    if weight - 26 < length:
      break
    ans.append('z')
    weight -= 26
    length -= 1

  # there will be one transitional character such that the remaining
  # characters will be equal to the remaining weight (if possible)
  j = 1
  length -= 1
  possible = False
  while True:
    if j > 26:
      break
    if weight - j == length:
      possible = True
      break
    j += 1

  # unable to find a weight which causes number of characters remaining
  # to be equivalent to weight
  if not possible:
    print('impossible')
    return

  ans.append(chr(97+j-1))
  # append 'a' for remaining characters
  for i in range(length):
    ans.append('a')
  print(''.join(ans))

if __name__ == "__main__":
  main()
