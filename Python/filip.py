# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/filip
# Complexity: O(N) where N is length of longer string
# Memory: O(1)

def main():
  args = [x for x in input().split()]

  # reverse strings and convert to nums
  num1 = int(args[0][::-1])
  num2 = int(args[1][::-1])

  if num1 > num2:
    print(num1)
  else:
    print(num2)

if __name__ == '__main__':
    main()
