# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/geppetto
# Complexity: O(M * 2**N) for a power set with N elements and M pairs
# Memory: O(M) for M pairs that are illegal

# had to use python 2 for speed
def main():
  n, m = map(int, raw_input().split())
  # filter duplicate pairs
  pairs = set()
  for i in xrange(m):
    a, b = map(int, raw_input().split())
    # compensate for 1 indexing
    a -= 1
    b -= 1
    pair = [a, b]
    # avoid duplicate pairs in opposite order
    pair.sort()
    pairs.add(tuple(pair))

  # note that 2*20 is only 1,000,000 and only 400 possible pairs to
  # check for each. This will pass in under 1 sec with brute force
  best = 2**n
  for i in xrange(2**n):
    # null set always valid
    if i == 0:
      continue
    # check each pair
    for j in xrange(len(pairs)):
      a, b = pairs[j]
      # if the ith bit is a 1, then the ith ingredient is used
      a_present = i >> a & 1
      b_present = i >> b & 1
      # illegal pair, so the number i is an illegal combo, check no
      # further
      if a_present and b_present:
        best -= 1
        break
  print best

if __name__ == "__main__":
  main()
