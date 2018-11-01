# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/kolone
# Complexity: O(N + M) for N and M characters to process
# Memory: O(N + M) for N and M characters

def main():
  # dont need string sizes in python
  ws = input()
  # reverse first because that is the order of the ants
  n = list(input())[::-1]
  m = list(input())
  # number of iterations
  t = int(input())

  # after n + m iterations, string will be fully reversed
  if t >= len(n) + len(m):
    print(''.join(m + n))
  else:
    # stores index of a given char
    indices = dict()
    i = 0
    for char in n:
      indices[char] = i
      i += 1
    for char in m:
      indices[char] = i
      i += 1

    # basically a 'mutable' string
    ans = ['0' for i in range(len(n) + len(m))]

    # after working some examples i saw that after n iterations, the first
    # ant will move n indices, the second n-1, the third n-2, etc.
    i = t
    index = len(n) - 1
    while i and (index + 1):
      char = n[index]
      # the character either moves left n times or moves to its max left position
      # it cannot pass an ant in the same sequence
      indices[char] = min(indices[char] + i, index + len(m))
      i -= 1
      index -= 1

    i = t
    index = 0
    while i and index < len(m):
      char = m[index]
      # same as above but rightward
      indices[char] = max(indices[char] - i, index)
      i -= 1
      index += 1

    for char in indices:
      ans[indices[char]] = char
    print(''.join(ans))

if __name__ == '__main__':
  main()

