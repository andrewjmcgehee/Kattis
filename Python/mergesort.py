# This is not a solution to a kattis problem. This is a python implementation
# of a merge sort

# test lists [4, 2, 1, 5, 3, 6, 7, 8] and [4, 2, 5, 7, 1, 3, 6]
L1 = [4, 2, 1, 5, 3, 6, 7, 8]
L2 = [4, 2, 5, 7, 1, 3, 6]


def mergeSort(arr):
    # lists with only one value already sorted
    if len(arr) > 1:
        # determine halves of list
        mid_point = len(arr) // 2
        left_sub = arr[:mid_point]
        right_sub = arr[mid_point:]

        # recursive function calls
        mergeSort(left_sub)
        mergeSort(right_sub)

        # keeps track of current index in left half
        left_i = 0
        # keeps track of current index in right half
        right_i = 0
        # keeps track of current index in merge list
        merge_i = 0

        while left_i < len(left_sub) and right_i < len(right_sub):
            # lower values appended to merged list first
            if left_sub[left_i] < right_sub[right_i]:
                arr[merge_i] = left_sub[left_i]
                left_i += 1
            else:
                arr[merge_i] = right_sub[right_i]
                right_i += 1
            merge_i += 1

        # catch remaining values in left and right
        while left_i < len(left_sub):
            arr[merge_i] = left_sub[left_i]
            left_i += 1
            merge_i += 1

        while right_i < len(right_sub):
            arr[merge_i] = right_sub[right_i]
            right_i += 1
            merge_i += 1
    return arr


if __name__ == '__main__':
    print(L1)
    print(L2)
    print(mergeSort(L1))
    print(mergeSort(L2))

