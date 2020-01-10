# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/completingthesquare

import math

def dot(a, b):
  return a[0] * b[0] + a[1] * b[1]

def main():
  A = tuple(map(int, input().split()))
  B = tuple(map(int, input().split()))
  C = tuple(map(int, input().split()))

  AB = math.hypot(A[0]-B[0], A[1]-B[1])
  BC = math.hypot(B[0]-C[0], B[1]-C[1])
  AC = math.hypot(A[0]-C[0], A[1]-C[1])
  hyp = max(max(AB, BC), AC)
  if hyp == AB:
    center = ((A[0]+B[0])/2, (A[1]+B[1])/2)
    d = (2*center[0]-C[0], 2*center[1]-C[1])
  elif hyp == BC:
    center = ((B[0]+C[0])/2, (B[1]+C[1])/2)
    d = (2*center[0]-A[0], 2*center[1]-A[1])
  else:
    center = ((A[0]+C[0])/2, (A[1]+C[1])/2)
    d = (2*center[0]-B[0], 2*center[1]-B[1])
  print(int(d[0]), int(d[1]))

if __name__ == "__main__":
  main()
