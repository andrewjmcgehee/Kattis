# Rating: ~ 3.9 / 10 (not really in python)
# Link: https://open.kattis.com/problems/grandpabernie
# Complexity: O(K * N log(N)) for K keys and N elements in the array at that key
# Memory: O(KN) for K keys and N elements in the largest array at a key

def main():
  n = int(input())
  # store trips in a hashmap
  trips = dict()
  for i in range(n):
    trip = input().split()
    country = trip[0]
    year = int(trip[1])
    # check for key error
    if country not in trips:
      trips[country] = []
    # add year
    trips[country].append(year)
  # sort array at each key
  for country in trips:
    trips[country].sort()

  # handle query
  q = int(input())
  for i in range(q):
    query = input().split()
    country = query[0]
    time = int(query[1]) - 1
    print(trips[country][time])

if __name__ == '__main__':
  main()
