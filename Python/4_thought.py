# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/4thought
# Complexity: O(1) not including preprocessing which is still 'constant'
# Memory: O(1)

def main():
  expressions = ['4']

  # build expressions
  for i in range(3):
    temp = []
    for e in expressions:
      temp.append(e + ' * 4')
      temp.append(e + ' + 4')
      temp.append(e + ' - 4')
      temp.append(e + ' / 4')
    expressions = temp

  # store expressions in a map that maps the solution to the expression
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

if __name__ == '__main__':
    main()
