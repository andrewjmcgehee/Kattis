# Rating: ~ 1.7 / 10
# Link: https://open.kattis.com/problems/bookingaroom
# Complexity: O(N) for N rooms
# Memory: O(N) for N rooms

def main():
  args = [int(x) for x in input().split()]
  r = args[0]
  n = args[1]

  # always too late if all rooms booked
  if r == n:
    print('too late')

  else:
    available = set(x for x in range(1, r+1))
    taken = set()

    for i in range(n):
      room = int(input())
      taken.add(room)

    # remove intersect of sets
    available -= taken
    # print any available room
    print(available.pop())

if __name__ == '__main__':
    main()
