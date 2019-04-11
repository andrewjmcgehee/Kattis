# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/fishmongers
# Complexity: O(N log(N) + K log(K)) for N fish and K mongers
# Memory: O(N + K) for N fish and K mongers

def main():
  # get inputs
  n, m = map(int, input().split())
  fish = [int(x) for x in input().split()]
  # using as a stack so not reversing
  fish.sort()

  mongers = []
  for i in range(m):
    w, v = map(int, input().split())
    # price first, then number of fish
    mongers.append((v, w))
  mongers.sort()

  total = 0
  while True:
    price, number = mongers.pop()
    # sell greedily
    while number and fish:
      total += fish.pop() * price
      number -= 1
    # exit condition, ran out of fish, or no more buying mongers
    if not fish or not mongers:
      break
  print(total)

if __name__ == "__main__":
  main()
