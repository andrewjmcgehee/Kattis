# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/busnumbers2
# Complexity: O(N^2) to try pair wise cubes for N numbers
# Memory: O(1)

# maximum possible number
MAX = 400001

def main():
  m = int(input())
  # will track frequency of numbers which are sums of 2 cubes
  freq = dict()
  i = 1
  while i**3 < MAX:
    a = i**3
    # starting j at i eliminates possibility of counting the same
    # pair of cubes twice (i.e. 1^3 + 3^3 and 3^3 + 1^1 are not distinct)
    j = i
    while a + j**3 < MAX:
      b = j**3
      # add to map
      if a + b not in freq:
        freq[a+b] = 0
      freq[a+b] += 1
      j += 1
    i += 1

  ans = None
  # visit all keys in sorted order essentially
  for i in range(m+1):
    if i in freq and freq[i] >= 2:
      ans = i
  # if one meets the criteria ans will not be None
  if ans:
    print(ans)
    return
  print('none')


if __name__ == '__main__':
  main()




