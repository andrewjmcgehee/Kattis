# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/kitchen

from heapq import heappop, heappush

visited = dict()

def get_neighbors(poured, state, capacities):
  global visited
  states = []
  for i, vol1 in enumerate(state):
    if vol1 > 0:
      for j, vol2 in enumerate(state):
        if i != j and vol2 < capacities[j]:
          new_state = list(state)
          available = capacities[j] - vol2
          new_pour = min(vol1, available)
          new_state[i] -= new_pour
          new_state[j] += new_pour
          new_state = tuple(new_state)
          if new_state not in visited or (new_state in visited and new_pour < visited[new_state]):
            states.append((poured + new_pour, new_state))
            visited[new_state] = new_pour
  return states

def main():
  global visited
  arr = [int(x) for x in input().split()]
  buckets = arr[0]
  goal = arr[-1]
  capacities = arr[1:buckets+1]

  state = tuple([capacities[0]] + [0 for i in range(buckets-1)])
  pq = [(0,state)]
  visited[state] = 0
  while pq:
    poured, state = heappop(pq)
    if state[0] == goal:
      print(poured)
      return
    for neighbor in get_neighbors(poured, state, capacities):
      heappush(pq, neighbor)
  print('impossible')


if __name__ == "__main__":
  main()
