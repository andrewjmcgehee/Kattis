# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/musicalnotation
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
lined = {'F', 'D', 'B', 'g', 'e', 'a'}
score = {k:[] for k in keys}

def main():
  _ = int(input())
  notes = input().split()
  for n in notes:
    if len(n) == 2:
      note = n[0]
      duration = int(n[1])
      if note in lined:
        score[note].append('*' * duration + '-')
      else:
        score[note].append('*' * duration + ' ')
      for k in keys:
        if k != note:
          if k in lined:
            score[k].append('-' * (duration+1))
          else:
            score[k].append(' ' * (duration+1))
    else:
      note = n
      if note in lined:
        score[note].append('*-')
      else:
        score[note].append('* ')
      for k in keys:
        if k != note:
          if k in lined:
            score[k].append('--')
          else:
            score[k].append('  ')
  for k in reversed(keys):
    print(k + ':', ''.join(score[k])[:-1])

if __name__ == "__main__":
  main()
