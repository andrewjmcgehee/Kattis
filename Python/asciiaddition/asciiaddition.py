# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/asciiaddition

mapping = {
  '....x....x....x....x....x....x....x': '1',
  'xxxxx....x....xxxxxxx....x....xxxxx': '2',
  'xxxxx....x....xxxxxx....x....xxxxxx': '3',
  'x...xx...xx...xxxxxx....x....x....x': '4',
  'xxxxxx....x....xxxxx....x....xxxxxx': '5',
  'xxxxxx....x....xxxxxx...xx...xxxxxx': '6',
  'xxxxx....x....x....x....x....x....x': '7',
  'xxxxxx...xx...xxxxxxx...xx...xxxxxx': '8',
  'xxxxxx...xx...xxxxxx....x....xxxxxx': '9',
  'xxxxxx...xx...xx...xx...xx...xxxxxx': '0',
  '.......x....x..xxxxx..x....x.......': '+',
  '0': [
    'xxxxx',
    'x...x',
    'x...x',
    'x...x',
    'x...x',
    'x...x',
    'xxxxx'
  ],
  '1': [
    '....x',
    '....x',
    '....x',
    '....x',
    '....x',
    '....x',
    '....x'
  ],
  '2': [
    'xxxxx',
    '....x',
    '....x',
    'xxxxx',
    'x....',
    'x....',
    'xxxxx'
  ],
  '3': [
    'xxxxx',
    '....x',
    '....x',
    'xxxxx',
    '....x',
    '....x',
    'xxxxx'
  ],
  '4': [
    'x...x',
    'x...x',
    'x...x',
    'xxxxx',
    '....x',
    '....x',
    '....x'
  ],
  '5': [
    'xxxxx',
    'x....',
    'x....',
    'xxxxx',
    '....x',
    '....x',
    'xxxxx'
  ],
  '6': [
    'xxxxx',
    'x....',
    'x....',
    'xxxxx',
    'x...x',
    'x...x',
    'xxxxx'
  ],
  '7': [
    'xxxxx',
    '....x',
    '....x',
    '....x',
    '....x',
    '....x',
    '....x'
  ],
  '8': [
    'xxxxx',
    'x...x',
    'x...x',
    'xxxxx',
    'x...x',
    'x...x',
    'xxxxx'
  ],
  '9': [
    'xxxxx',
    'x...x',
    'x...x',
    'xxxxx',
    '....x',
    '....x',
    'xxxxx'
  ]
}

def main():
  exp = []
  for i in range(7):
    exp.append(input())
  chars = []
  i = 0
  while i < len(exp[0]):
    chars.append([])
    for j in range(7):
      chars[-1].append(exp[j][i:i+5])
    i += 6
  for i in range(len(chars)):
    chars[i] = ''.join(chars[i])
    chars[i] = mapping[chars[i]]
  exp = ''.join(chars)
  ans = str(eval(exp))
  out = [[] for i in range(7)]
  for i in range(len(ans)):
    for j in range(7):
      out[j].append(mapping[ans[i]][j])
  print('\n'.join(['.'.join(row) for row in out]))

if __name__ == "__main__":
  main()
