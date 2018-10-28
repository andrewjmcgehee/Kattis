# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/acm
# Complexity: O(N) to process N lines of input
# Memory: O(N) for N problems to solve

def main():
  solved = dict()
  finished = set()
  num_solved = 0
  total_time = 0

  while True:
    line = input().split()
    time = int(line[0])

    if time == -1:
      break

    prob = line[1]
    result = line[2]

    if prob in solved:
      # correct on nth attempt
      if result[0] == 'r':
        if prob not in finished:
          finished.add(prob)
          solved[prob][0] = time
      # incorrect, add an attempt
      else:
        solved[prob][1] += 1
    else:
      # correct on first attempt
      if result[0] == 'r':
        finished.add(prob)
        solved[prob] = [time, 0]
      # incorrect
      else:
        solved[prob] = [-1, 1]

  # calculate num solved and penalty time
  for prob in solved:
    if solved[prob][0] != -1:
      total_time += (solved[prob][0] + 20*solved[prob][1])
      num_solved += 1
  print(num_solved, total_time)

if __name__ == '__main__':
    main()
