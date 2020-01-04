# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/videospeedup

def main():
  n, p, k = map(int, input().split())
  if n == 1:
    t = int(input())
    if k > t:
      time = t + (1+p)*(k-t)
    else:
      time = t
    print(time)
    return
  p /= 100
  t = [int(x) for x in input().split()]
  while t[-1] >= k:
    t.pop()
  t.append(k)
  t = [0] + t
  speed = 1 + (len(t)-2)*p
  time = 0
  for i in range(len(t)-1,0,-1):
    time += (t[i]-t[i-1])*speed
    speed -= p
  print(time)

if __name__ == "__main__":
  main()
