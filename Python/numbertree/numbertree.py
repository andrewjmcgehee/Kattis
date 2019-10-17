# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/numbertree

def main():
  line = input().split()
  n = int(line[0])
  # full tree
  num_nodes = 2**(n+1) - 1
  # trivial case
  if len(line) == 1:
    print(num_nodes)
    return
  instructs = line[1]
  index = 0
  # left children stored at 2i + 1 and right at 2i + 2
  for char in instructs:
    if char == 'L':
      index = 2*index + 1
    else:
      index = 2*index + 2
  print(num_nodes - index)

if __name__ == "__main__":
  main()
