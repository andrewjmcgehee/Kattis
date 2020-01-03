# Rating: ~ 4.0 / 10
# Link: https://open.kattis.com/problems/muddyhike

from heapq import heappop, heappush

def main():
  r, c = map(int, input().split())
  board = []
  for i in range(r):
    board.append([int(x) for x in input().split()])
  q = []
  moves = {(0,1), (1,0), (0,-1), (-1,0)}
  visited = dict()
  for i in range(r):
    heappush(q, (board[i][0], c-1, i, 0))
    visited[(i, 0)] = board[i][0]
  while q:
    depth, dist_remaining, row, col = heappop(q)
    if dist_remaining == 0:
      print(depth)
      return
    for i, j in moves:
      if row+i >= 0 and row+i < r and col+j >= 0 and col+j < c:
        new_depth = max(depth, board[row+i][col+j])
        if (row+i,col+j) not in visited or new_depth < visited[(row+i,col+j)]:
          visited[(row+i,col+j)] = new_depth
          new_dist = c-(col+j)-1
          heappush(q, (new_depth, new_dist, row+i, col+j))

if __name__ == "__main__":
  main()
