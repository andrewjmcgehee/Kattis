# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/calories

conv = [9,4,4,4,7]

def main():
  while True:
    lines = []
    while True:
      curr = input()
      if curr == '-':
        break
      lines.append(curr)
    if not lines:
      break
    cals = [0, 0, 0, 0, 0]
    for l in lines:
      total = 0
      percent = 0
      index = []
      vals = l.split()
      for i, v in enumerate(vals):
        if v[-1] == 'g':
          vals[i] = float(vals[i][:-1]) * conv[i]
          total += vals[i]
        elif v[-1] == 'C':
          vals[i] = float(vals[i][:-1])
          total += vals[i]
        else:
          percent += float(vals[i][:-1])
          index.append(i)
      total = total / (1 - percent / 100)
      for i in index:
        vals[i] = total * float(vals[i][:-1]) / 100
      cals = [sum(x) for x in zip(cals, vals)]
    print(round(cals[0] / sum(cals) * 100), end='%\n')


if __name__ == "__main__":
  main()
