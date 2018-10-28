# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/jollyjumpers
# Complexity: O(N) for N numbers
# Memory: O(N) for N numbers

def main():
  while True:
    try:
      line = [int(x) for x in input().split()][1:]
      # 1 element always jolly
      if len(line) == 1:
        print('Jolly')
        continue

      # stores all the differences
      diffs = set()
      for i in range(1, len(line)):
        diffs.add(abs(line[i] - line[i-1]))
      # range 1 through n - 1
      seq = set(range(1, len(line)))
      # intersect of sets
      if (diffs & seq) == seq:
        print('Jolly')
      else:
        print('Not jolly')
    except EOFError:
      break

if __name__ == '__main__':
  main()
