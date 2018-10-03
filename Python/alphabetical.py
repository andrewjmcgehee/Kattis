# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/alphabet
# Complexity: O(N^2) for N elements
# Memory: O(N) for N elements

def lis(arr):
  n = len(arr)

  # initial longest increasing is 1 for all items
  lis = [1]*n

  # use bottom up DP to store max longest increasing subseq ending at
  # index i
  for i in range (1 , n):
    for j in range(0 , i):
      if arr[i] > arr[j] and lis[i] < lis[j] + 1 :
        lis[i] = lis[j]+1

  # get max of all increasing subsequences
  return max(lis)

def main():
  # 26 minus lis gives number of chars needed to complete increasing alphabet
  print(26 - lis(list(input())))

if __name__ == '__main__':
  main()
