# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/beekeeper

def main():
  vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
  while True:
    n = int(input())
    if n == 0:
      break
    best = None
    max_count = -1
    for i in range(n):
      line = input()
      if i == 0:
        best = line
      count = 0
      for j in range(1, len(line)):
        if line[j] in vowels and line[j] == line[j-1]:
          count += 1
      if count > max_count:
        max_count = count
        best = line
    print(best)

if __name__ == "__main__":
  main()
