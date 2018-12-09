# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/anothercandies

def main():
  # num cases
  t = int(input())
  for i in range(t):
    # white space
    ws = input()
    # num children
    c = int(input())
    # total candies
    candies = 0
    for j in range(c):
      # trivial due to python data types
      candies += int(input())
    if candies % c == 0:
      print('YES')
    else:
      print('NO')

if __name__ == "__main__":
  main()
