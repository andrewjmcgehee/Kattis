# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/rotatecut
# Complexity: O(N) where N is number of message to process
# Memory: O(1)

def main():
  n = int(input())
  for _ in range(n):
    x, sentence = input().split()
    x = int(x)

    # start with 1 for convenience of knowing odd and even
    for i in range(1, x+1):
      # integer division to eliminate fractional values
      quarter = len(sentence) // 4
      if quarter == 0:
        break

      # if odd cut from beginning
      if i & 1 == 1:
        sentence = sentence[quarter:]
      # otherwise cut from end
      else:
        quarter *= -1
        sentence = sentence[:quarter]
    print(sentence)

if __name__ == '__main__':
  main()
