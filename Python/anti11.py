# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/anti11
# Complexity: O(N) for N fibonacci numbers
# Memory: O(N) for N fibonacci numbers

# DP to speed up fib calculations
# could have also done it with matrix multiplication to save memory
# and recursion overhead
memo = [0 for i in range(10002)]
memo[1] = 1
memo[2] = 1

def fib(n):
  if n == 0:
    return 0
  if n == 1 or n == 2:
    return 1
  if memo[n]:
    return memo[n]
  # modulo 10 billion 7 as in problem statement
  memo[n] = fib(n-1) + fib(n-2) % (10**9 + 7)
  return memo[n]


def main():
  # calculte fibs in chunks of 500 to avoid recursion depth error
  for i in range(20):
    fib(i*500)
  fib(10001)

  t = int(input())
  for _ in range(t):
    n = int(input())
    # get the n + 2 fib number
    print((memo[n] + memo[n+1]) % (10**9 + 7))

if __name__ == '__main__':
  main()
