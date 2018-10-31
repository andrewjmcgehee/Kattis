# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/iboard
# Complexity: O(N) for N characters
# Memory: O(1)

def main():
  while True:
    try:
      line = input()
    except EOFError:
      break

    # int which acts as a bit vector
    pressed = 0
    for char in line:
      # get numeric version of char
      num = ord(char)
      for i in range(9):
        # check the ith bit
        bit = (num>>i) & 1
        # flip 2nd bit if 1
        if bit == 1:
          pressed ^= (1<<1)
        # flip 1st if 0
        else:
          pressed ^= 1
    # if pressed is anything but 0, then we are trapped
    if pressed:
      print("trapped")
    else:
      print("free")


if __name__ == '__main__':
  main()

