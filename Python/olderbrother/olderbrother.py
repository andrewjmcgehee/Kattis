# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/olderbrother
# Complexity: O(log(N)) for sieve prime factorization
# Memory: O(N) for N prime factors

def main():
  t = int(input())
  # trivial case, 1 not prime
  if t == 1:
    print('no')
    return

  factors = set()
  i = 2
  # check up through sqrt(t)
  while i**2 <= t:
    # divide if possible and add factor
    if t % i == 0:
      t /= i
      factors.add(i)
    else:
      i += 1
  # if t is not 1, there is one prime factor remaining
  if t != 1:
    factors.add(t)

  # if no factors, then t itself is prime, otherwise factors
  # must only contain 1 value
  if not factors or len(factors) == 1:
    print('yes')
  else:
    print('no')

if __name__ == "__main__":
  main()
