# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/hangingout

def main():
  n, m = map(int, input().split())
  ppl = 0
  denied = 0
  for i in range(m):
    cmd, num = input().split()
    num = int(num)
    if cmd == 'enter':
      if num + ppl > n:
        denied += 1
      else:
        ppl += num
    else:
      ppl -= num
  print(denied)


if __name__ == "__main__":
  main()
