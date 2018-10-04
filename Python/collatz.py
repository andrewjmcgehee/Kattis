# Rating: ~ 4.6 / 10
# Link: https://open.kattis.com/problems/collatz
# Complexity: O(N + K) where N is length of first collatz sequence and K is length of second
# Memory: O(N + K) where N is length of first collatz sequence and K is length of second

def main():
  while True:
    x, y = map(int, input().split())
    if x == y == 0:
      break

    x_list = [x]
    y_list = [y]

    # generate x sequence
    while x != 1:
      if x % 2 == 0:
        # avoid floating point
        x = x // 2
        x_list.append(x)
      else:
        x *= 3
        x += 1
        x_list.append(x)
    # generate y sequence
    while y != 1:
      if y % 2 == 0:
        y = y // 2
        y_list.append(y)
      else:
        y *= 3
        y += 1
        y_list.append(y)
    # compare each index starting from the back and see where they diverge
    index = -1
    while x_list[index] == y_list[index]:
      # if at the beginning of either sequence, break
      if x_list[index] == x_list[0] or y_list[index] == y_list[0]:
        index -= 1
        break
      index -= 1

    print('%i needs %i steps, %i needs %i steps, they meet at %i'
          % (x_list[0], len(x_list[:index+1]),
             y_list[0], len(y_list[:index+1]),
             x_list[index+1]))

if __name__ == '__main__':
    main()
