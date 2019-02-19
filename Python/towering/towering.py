# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/towering
# Complexity: O(N^3) for N boxes but there are only 6
# Memory: O(N) for N boxes

# helper for building towers
def get_towers(boxes, a, b):
  tower_a = []
  tower_b = []
  # for getting difference of sets
  full_set = set(boxes)
  # small enough sets to just try all of them
  for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
      for k in range(j+1, len(boxes)):
        candidate = boxes[i] + boxes[j] + boxes[k]
        if candidate == a:
          tower_a = set([boxes[i], boxes[j], boxes[k]])
          tower_b = full_set - tower_a
          return (tower_a, tower_b)
        elif candidate == b:
          tower_b = set([boxes[i], boxes[j], boxes[k]])
          tower_a = full_set - tower_b
          return (tower_a, tower_b)

def main():
  boxes = [int(x) for x in input().split()]
  # targets
  a = boxes[6]
  b = boxes[7]
  boxes = boxes[:6]

  tower_a, tower_b = get_towers(boxes, a, b)
  # reverse sort
  tower_a = sorted(tower_a)[::-1]
  tower_b = sorted(tower_b)[::-1]
  # convert to strings
  tower_a = [str(x) for x in tower_a]
  tower_b = [str(x) for x in tower_b]
  # print space separated
  s = ' '.join(tower_a) + ' ' + ' '.join(tower_b)
  print(s)

if __name__ == "__main__":
  main()
