# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/vote

from sys import stdin

def main():
  n = int(input())
  for i in range(n):
    c = int(input())
    votes = []
    for j in range(c):
      votes.append(int(input()))
    total = sum(votes)
    majority = total / 2
    best = max(votes)
    if votes.count(best) > 1:
      print('no winner')
      continue
    winner = votes.index(best)
    if best > majority:
      print('majority winner {}'.format(winner+1))
    else:
      print('minority winner {}'.format(winner+1))


if __name__ == "__main__":
  main()
