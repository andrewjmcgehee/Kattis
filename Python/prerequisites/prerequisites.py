# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/prerequisites
# Complexity: O(N) for N courses
# Memory: O(N) for N courses

def main():
  while True:
    line = [int(x) for x in input().split()]
    if line[0] == 0:
      break
    # get courses as a set
    courses = set(input().split())
    can_grad = True
    for i in range(line[1]):
      course = input().split()
      # tracks number of remaining requirements for a category
      num_reqs = int(course[1])
      for j in range(2, len(course)):
        if course[j] in courses:
          num_reqs -= 1
      # only illegal state is if there are
      if num_reqs > 0:
        can_grad = False
    if can_grad:
      print('yes')
    else:
      print('no')

if __name__ == "__main__":
  main()
