def main():
  while True:
    try:
      line = input()
    except EOFError:
      break

    pressed = 0
    for char in line:
      num = ord(char)
      for i in range(9):
        bit = (num>>i) & 1
        if bit == 1:
          pressed ^= (1<<1)
        else:
          pressed ^= 1

    if pressed:
      print("trapped")
    else:
      print("free")


if __name__ == '__main__':
  main()

