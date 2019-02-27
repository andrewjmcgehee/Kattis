# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/gettowork
# Complexity: O(N * E log(E)) for N cities and sorting E edges
# Memory: O(E) for E edges

def main():
  cases = int(input())
  for c in range(cases):
    n, target_city = map(int, input().split())
    # compensate for 1 indexing
    target_city -= 1
    # edge list noting edges from town H to town T
    adj = [[] for x in range(n)]
    num_employees = int(input())
    for i in range(num_employees):
      home, passengers = map(int, input().split())
      # compensate for 1 indexing
      home -= 1
      # no need to add edges from T to T
      if home != target_city:
        adj[home].append(passengers)

    # will store output
    num_cars = []
    possible = True
    for i in range(n):
      # sort so we can use greedy strategy for picking cars
      adj[i].sort()
      # every employee creates an edge so num edges is num employees
      employees = len(adj[i])
      # employees who have secured a seat
      seats = 0
      # cars needed
      cars = 0
      while seats < employees and adj[i]:
        seats += adj[i].pop()
        cars += 1
      # if we pop every value from the adjacency list, and our num
      # seats is still less than employees, it is impossible
      if seats < employees and not adj[i]:
        possible = False
        break
      num_cars.append(str(cars))
    # handle output
    if possible:
      print('Case #' + str(c+1) + ':', ' '.join(num_cars))
    else:
      print('Case #' + str(c+1) + ':', 'IMPOSSIBLE')

if __name__ == "__main__":
  main()
