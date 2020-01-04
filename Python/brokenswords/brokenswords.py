# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/brokenswords

def main():
  n = int(input())
  tblr = [n, n, n, n]
  for _ in range(n):
    s = input()
    for i in range(4):
      if s[i] == '1':
        tblr[i] -= 1
  tb = sum(tblr[:2])
  lr = sum(tblr[2:])
  s = min(tb, lr) // 2
  tb -= s * 2
  lr -= s * 2
  print(s, tb, lr)

if __name__ == "__main__":
  main()
