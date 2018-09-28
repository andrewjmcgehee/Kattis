# Rating: ~ 4.0 / 10
# Link: https://open.kattis.com/problems/alicedigital
# Complexity: O(N) where N is number of elements
# Memory: O(N) worst case for storing locations of designated M

def main():
  cases = int(input())
  for _ in range(cases):
    n, m = [int(x) for x in input().split()]

    arr = [int(x) for x in input().split()]
    pos = []

    # get points of interest
    for i in range(n):
      if arr[i] == m:
        pos.append(i)

    # worst possible sum is 0
    best = 0
    for p in pos:
      # grow sums outward from m value
      i = p-1
      j = p+1
      i_good = True
      j_good = True
      # current sum will always start with min value of m
      current = m
      while True:
        # out of bounds
        if i < 0:
          i_good = False
        if j >= n:
          j_good = False
        if not i_good and not j_good:
          break

        if i_good:
          # only add element and grow range if m is still minumum value
          if arr[i] > m:
            current += arr[i]
            # grow leftward
            i -= 1
          else:
            i_good = False
        if j_good:
          if arr[j] > m:
            current += arr[j]
            # grow rightward
            j += 1
          else:
            j_good = False
      best = max(best, current)
    print(best)

if __name__ == '__main__':
  main()

