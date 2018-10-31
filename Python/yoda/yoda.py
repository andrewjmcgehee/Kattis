# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/yoda
# Complexity: O(N) for N chars in longer number
# Memory: O(N) for N chars in longer number

def main():
  # get inputs
  first = [int(x) for x in input().strip()]
  last = [int(x) for x in input().strip()]

  # create boolean arrays for tracking fall outs.
  arr1 = [True for x in first]
  arr2 = [True for x in last]

  # larger number keeps all numbers past length of shorter.
  if len(arr1) < len(arr2):
    shorter = arr1
  else:
    shorter = arr2

  # iterate through flipping booleans of fall through values
  i = 1
  while i <= len(shorter):
    if first[-i] < last[-i]:
      arr1[-i] = False
    elif first[-i] == last[-i]:
      i += 1
      continue
    else:
      arr2[-i] = False
    i += 1

  new_first = []
  new_last = []
  # generate new numbers
  for i in range(len(arr1)):
    if arr1[i]:
      new_first.append(str(first[i]))
  for i in range(len(arr2)):
    if arr2[i]:
      new_last.append(str(last[i]))
  # create strings
  new_first = ''.join(new_first)
  new_last = ''.join(new_last)
  # must check if string non empty
  if new_first and int(new_first) == 0:
    new_first = '0'
  if new_last and int(new_last) == 0:
    new_last = '0'
  # if empty string becomes YODA
  if len(new_first) == 0:
    new_first = 'YODA'
  if len(new_last) == 0:
    new_last = 'YODA'
  print(new_first)
  print(new_last)

if __name__ == '__main__':
    main()

