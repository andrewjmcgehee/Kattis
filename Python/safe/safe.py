# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/safe

from collections import deque

mapping = {'0':'1', '1':'2', '2':'3', '3':'0'}

def get_neighbors(s):
  neighbors = []
  s = list(s)
  for button in range(9):
    state = [
      s[:3],
      s[3:6],
      s[6:]
    ]
    row = button // 3
    col = button % 3
    for i in range(3):
      num = state[row][i]
      state[row][i] = mapping[num]
    for i in range(3):
      if i != row:
        num = state[i][col]
        state[i][col] = mapping[num]
    neighbors.append(''.join([''.join(row) for row in state]))
  return neighbors

def main():
  safe = ''
  for i in range(3):
    safe += ''.join([x for x in input().split()])
  if safe == '000000000':
    print(0)
    return
  visited = set()
  visited.add(safe)
  q = deque([safe, None])
  pushed = 0
  while q:
    state = q.popleft()
    if state is None:
      pushed += 1
      if not q:
        break
      q.append(None)
      continue
    if state == '000000000':
      print(pushed)
      return
    for n in get_neighbors(state):
      if n not in visited:
        visited.add(n)
        q.append(n)
  print(-1)


if __name__ == "__main__":
  main()
