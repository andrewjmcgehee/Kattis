# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/conundrum

def main():
  count = 0
  s = input().lower()
  t = 'per' * (len(s) // 3)
  for i in range(len(s)):
    if s[i] != t[i]:
      count += 1
  print(count)

if __name__ == "__main__":
  main()
