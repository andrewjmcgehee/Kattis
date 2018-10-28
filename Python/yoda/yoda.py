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
    
    # reverse lists to 'right-align' them.
    num1 = first[::-1]
    num2 = last[::-1]

    # iterate through flipping booleans of fall through values.
    for i in range(len(shorter)):
        if num1[i] < num2[i]:
            arr1[i] = False
        elif num1[i] == num2[i]:
            continue
        else:
            arr2[i] = False

    # reverse boolean arrays to match with initial numbers.
    arr1 = arr1[::-1]
    arr2 = arr2[::-1]
    
    new_first = ''
    new_last = ''
    
    # generate new numbers
    for i in range(len(arr1)):
        if arr1[i]:
            new_first += str(first[i])

    for i in range(len(arr2)):
        if arr2[i]:
            new_last += str(last[i])

    if len(new_first) == 0:
        new_first = 'YODA'
    
    if len(new_last) == 0:
        new_last = 'YODA'
    
    zeros = 0
    for i in range(len(new_first)):
        if new_first[i] != '0':
            break
        else:
            zeros += 1
        if zeros == len(new_first):
            new_first = '0'
            break
    
    zeros = 0
    for i in range(len(new_last)):
        if new_last[i] != '0':
            break
        else:
            zeros += 1
        if zeros == len(new_last):
            new_last = '0'
            break

    print(new_first)
    print(new_last)

if __name__ == '__main__':
    main()
    