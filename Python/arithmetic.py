# Rating: ~ 3.7 / 10
# Link: https://open.kattis.com/problems/arithmetic
# Complexity: O(N) for N digits
# Memory: O(N) for N digits

def main():
  num = input()
  digit_arr = [int(char) for char in num]

  binary = ''
  for i in digit_arr:
    # octal can be represented as 3 bits, padded with leading 0s
    # if necessary
    binary += format(i, '03b')

  # format in capital hexadecimal
  print("%X" % int(binary, 2))

if __name__ == '__main__':
    main()
