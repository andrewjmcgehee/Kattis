# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/owlandfox

def main():
  x = int(input())
  for _ in range(x):
    num = int(input())
    num_score = sum([int(i) for i in list(str(num))])
    for i in range(num-1, -1, -1):
      score = sum([int(j) for j in list(str(i))])
      if score == num_score - 1:
        print(i)
        break

if __name__ == "__main__":
  main()
