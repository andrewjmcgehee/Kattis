# orderlyclass
# 3.8

from collections import defaultdict

def main():
  a = '.'.join(list(input()))
  b = '.'.join(list(input()))
  diff = []
  for i in range(len(a)):
    if a[i] != b[i]:
      diff.append(i)
  if len(diff) & 1:
    print(0)
    return

  mid = (diff[0] + diff[-1]) // 2
  l = mid
  r = mid

  while True:
    if a[l] == b[r] and a[r] == b[l]:
      l -= 1
      r += 1
    else:
      break
    if l < 0 or r >= len(a):
      break
  l += 1
  r -= 1
  if l > diff[0] or r < diff[-1]:
    print(0)
    return
  total = 0
  for i in range(l, diff[0]+1):
    if a[i] != '.':
      total += 1
  print(total)

if __name__ == '__main__':
  main()
