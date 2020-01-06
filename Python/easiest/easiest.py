# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/easiest

def main():
  while True:
    n = int(input())
    if n == 0:
      break
    nsum = sum([int(x) for x in list(str(n))])
    p = 11
    while True:
      k = n*p
      psum = sum([int(x) for x in list(str(k))])
      if psum == nsum:
        print(p)
        break
      p += 1

if __name__ == "__main__":
  main()
