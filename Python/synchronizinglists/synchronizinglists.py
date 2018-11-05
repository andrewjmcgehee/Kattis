# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/synchronizinglists
# Complexity: O(N) for N numbers
# Memory: O(N) for N numbers

def main():
  while True:
    n = int(input())
    if n == 0:
      break
    # lists
    a = []
    b = []
    for i in range(n):
      a.append(int(input()))
    for i in range(n):
      b.append(int(input()))
    # sort lists
    c = sorted(a)
    d = sorted(b)
    # stores numbers by their new order
    table = dict()
    for i in range(n):
      table[c[i]] = d[i]
    # print them out in their order
    for i in range(n):
      print(table[a[i]])
    print()

if __name__ == '__main__':
  main()
