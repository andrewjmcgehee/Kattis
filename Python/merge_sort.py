# This is not a solution to a kattis problem. This is a python implementation
# of a merge sort

def merge_sort(arr):
  # lists with only one value already sorted
  if len(arr) > 1:
    # determine halves of list
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursive function calls
    merge_sort(left)
    merge_sort(right)

    # keeps track of current index in left half
    i = 0
    # keeps track of current index in right half
    j = 0
    # keeps track of current index in merge list
    k = 0

    while i < len(left) and j < len(right):
      # lower values appended to merged list first
      if left[i] < right[j]:
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1

    # catch remaining values in left and right
    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1
  return arr

