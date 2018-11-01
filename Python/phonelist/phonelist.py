# Rating: ~ 4.2 / 10
# Link: https://open.kattis.com/problems/phonelist
# Complexity: O(NK) where N is number of strings and K is length of longest string
# Memory: O(NK^2) where N is number of strings and K is length of longest string

def main():
  t = int(input())
  for _ in range(t):
    # num strings
    n = int(input())
    # sort by length - longest first
    nums = sorted([input() for i in range(n)], key=len)[::-1]
    # basically a very lazy prefix tree
    prefixes = set()
    possible = True
    for num in nums:
      if num in prefixes:
        possible = False
        break
      # add all prefixes of given string
      for i in range(1, len(num)+1):
        prefixes.add(num[:i])
    if possible:
      print("YES")
    else:
      print("NO")

if __name__ == '__main__':
  main()

