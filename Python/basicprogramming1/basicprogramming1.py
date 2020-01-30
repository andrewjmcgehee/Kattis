# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/basicprogramming1

def stats(arr):
  cycle = set()
  j = 0
  status = ''
  while True:
    cycle.add(j)
    if j >= len(arr)-1:
      break
    j = arr[j]
    if j in cycle:
      status = 'Cyclic'
      break
  if status != 'Cyclic':
    if j == len(arr)-1:
      status = 'Done'
    else:
      status = 'Out'
  total = 0
  even_total = 0
  for a in arr:
    if not a & 1:
      even_total += a
    total += a
  return total, even_total, status

def main():
  N, t = map(int, input().split())
  arr = [int(x) for x in input().split()]
  s = ''.join([chr(x % 26 + 97) for x in arr])
  med = sorted(arr[:3])[1]
  total, even_total, status = stats(arr)
  if t == 1:
    print(7)
  elif t == 2:
    if arr[0] > arr[1]:
      print('Bigger')
    elif arr[0] == arr[1]:
      print('Equal')
    else:
      print('Smaller')
  elif t == 3:
    print(med)
  elif t == 4:
    print(total)
  elif t == 5:
    print(even_total)
  elif t == 6:
    print(s)
  elif t == 7:
    print(status)


if __name__ == "__main__":
  main()
