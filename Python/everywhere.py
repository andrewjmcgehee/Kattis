# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/everywhere
# Complexity: O(N) for N cities
# Memory: O(N) for N cities

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    # handles duplicates
    cities = set()
    for i in range(n):
      city = input()
      cities.add(city)
    print(len(cities))

if __name__ == '__main__':
  main()
