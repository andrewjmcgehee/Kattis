# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/horrorfilmnight

a = [0 for i in range(1000000)]
b = [0 for i in range(1000000)]
def main():
  n, *A = [int(x) for x in input().split()]
  m, *B = [int(x) for x in input().split()]
  for i in A:
    a[i] = 1
  for i in B:
    b[i] = 1

  a_ready = True
  b_ready = True
  total = 0
  for i in range(1000000):
    if a[i] and b[i]:
      a_ready = True
      b_ready = True
      total += 1
    elif a[i] and b_ready:
      a_ready = True
      b_ready = False
      total += 1
    elif b[i] and a_ready:
      a_ready = False
      b_ready = True
      total += 1
  print(total)

if __name__ == "__main__":
  main()
