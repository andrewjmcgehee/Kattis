# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/glitchbot

moves = {'Forward', 'Left', 'Right'}

def turn(t, d):
  if t[0] == 'L':
    d -= 1
    if d < 0:
      d += 4
    return d
  d += 1
  d = d % 4
  return d

def move(d):
  if d == 0:
    return (0,1)
  if d == 1:
    return (1,0)
  if d == 2:
    return (0,-1)
  return (-1,0)

def main():
  tx, ty = map(int, input().split())
  n = int(input())
  cmds = []
  for _ in range(n):
    cmds.append(input())
  for i in range(n):
    x, y = 0,0
    d = 0
    j = 0
    while j < i:
      c = cmds[j]
      if c[0] == 'F':
        x += move(d)[0]
        y += move(d)[1]
      else:
        d = turn(c, d)
      j += 1
    for m in moves:
      if m == cmds[i]:
        continue
      tmp_x, tmp_y = x, y
      tmp_d = d
      old = cmds[i]
      cmds[i] = m
      j = i
      while j < len(cmds):
        c = cmds[j]
        if c[0] == 'F':
          tmp_x += move(tmp_d)[0]
          tmp_y += move(tmp_d)[1]
        else:
          tmp_d = turn(c, tmp_d)
        j += 1
      if tmp_x == tx and tmp_y == ty:
        print(i+1, m)
        return
      else:
        cmds[i] = old

if __name__ == "__main__":
  main()
