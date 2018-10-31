# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/forests
# Complexity: O(
# Memory: O(

def main():
  p, t = map(int, input().split())
  # array of sets to store opinions
  opinions = [set() for i in range(p)]
  while True:
    try:
      # get all opinions
      op = [int(x) for x in input().split()]
    except EOFError:
      break
    # 0 indexing
    person = op[0] - 1
    tree = op[1]
    # add to set
    opinions[person].add(tree)

  # tracks frequency of given opinion
  freq = dict()
  for i in range(p):
    # sorted tuple to eliminate duplicate keys and so it can be hashed
    opinions[i] = tuple(sorted(opinions[i]))
    # add that opinion
    if opinions[i] not in freq:
      freq[opinions[i]] = True
  # number of keys = number of unique opinions
  print(len(freq.keys()))
if __name__ == '__main__':
  main()


