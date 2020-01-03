# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/encodedmessage

def main():
  n = int(input())
  for _ in range(n):
    line = input()
    length = int(len(line)**0.5)
    out = []
    count = length-1
    while count >= 0:
      for i in range(length):
        tmp = line[i*length:(i+1)*length]
        out.append(tmp[count])
      count -= 1
    print(''.join(out))

if __name__ == "__main__":
  main()
