# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/textmessaging

def main():
  t = int(input())
  for i in range(t):
    l, k, a = map(int, input().split())
    freq = sorted([int(x) for x in input().split()], reverse=True)
    total = 0
    current = 0
    while current < len(freq):
      mult = current // k + 1
      total += mult * freq[current]
      current += 1
    print('Case #{}: {}'.format(i+1, total))

if __name__ == "__main__":
  main()
