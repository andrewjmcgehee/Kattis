# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/parsinghex
# Complexity: O(N) for N characters in line
# Memory: O(N) for N characters

# set of possible hex values
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
    # check me and character in front of me
    while i < len(line)-1:
      # find hex beginning
      if line[i:i+2].lower() == '0x':
        j = i + 2
        while j < len(line):
          if line[j].lower() in HEX:
            j += 1
          # break on first non legal char
          else:
            break
        # check if no extra characters were added
        if line[i:j].lower() != '0x':
          # print hex string and hex converted to decimal
          print(line[i:j], int(line[i:j], 0))
        i = j
        continue
      i += 1

if __name__ == '__main__':
  main()

