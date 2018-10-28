HEX = {
  '0', '1', '2', '3',
  '4', '5', '6', '7',
  '8', '9', 'a', 'b',
  'c', 'd', 'e', 'f'
}

def main():
  while True:
    try:
      line = input()
    except EOFError:
      break

    i = 0
    while i < len(line)-1:
      if line[i:i+2].lower() == '0x':
        j = i + 2
        while j < len(line):
          if line[j].lower() in HEX:
            j += 1
          else:
            break
        if line[i:j].lower() != '0x':
          print(line[i:j], int(line[i:j], 0))
        i = j
        continue
      i += 1

if __name__ == '__main__':
  main()

