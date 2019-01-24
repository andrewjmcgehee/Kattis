# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/basicremains
# Complexity: O(N) for N characters in digit
# Memory: O(1)

# helper to convert base 10 to any base
def to_base(x, b):
  res = ""
  while x:
    res += BASES[x%b]
    x //= b
  if res:
    return res[::-1]
  return '0'

def main():
  while True:
    line = input().split()
    base = int(line[0])
    # end of input
    if base == 0:
      break
    x, y = line[1], line[2]

    # already optimized, dont re-implement the wheel
    a = int(x, base)
    b = int(y, base)

    mod = a % b
    ans = to_base(mod, base)
    print(ans)

if __name__ == "__main__":
  main()
