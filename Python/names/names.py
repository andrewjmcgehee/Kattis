# Rating: ~ 3.7 / 10
# Link: https://open.kattis.com/problems/names
# Complexity: O(N^2) for N characters
# Memory: O(1)

def main():
  name = input()
  n = len(name)
  # theoretical worst is to change every char
  best = n
  for i in range(n):
    # pointer to beginning of current range
    left = i
    # pointer to end of current range
    right = n-1
    # starting point - signifies appending the first i chars to
    # end of string in reverse order
    moves = i
    while left < right:
      # change needed to make current range a palindrome
      if name[left] != name[right]:
        moves += 1
      left += 1
      right -= 1
    # keep min result
    best = min(best, moves)
  print(best)

if __name__ == "__main__":
  main()
