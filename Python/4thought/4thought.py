# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/4thought
# Complexity: O(N^2) for N queens due to checking pair-wise relationhips
# Memory: O(1) for an 8 by 8 board

expressions = ['4']

for i in range(3):
  temp = []
  for e in expressions:
    temp.append(e + ' * 4')
    temp.append(e + ' + 4')
    temp.append(e + ' - 4')
    temp.append(e + ' / 4')
  expressions = temp

solutions = dict()
for e in expressions:
  tokens = e.split()
  string = ''
  for token in tokens:
    if token == '/':
      string += '//'
    else:
      string += token
  num = eval(string)
  solutions[num] = e

num_cases = int(input())
for i in range(num_cases):
  n = int(input())
  if n in solutions:
    s = solutions[n]
    print(s + ' = ' + str(n))
  else:
    print('no solution')
