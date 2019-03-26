# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/imagedecoding
# Complexity: O(N) for N lines to be handled
# Memory: O(N) for N lines stored in arrays

def main():
  # store final output
  total_out = []
  while True:
    n = int(input())
    # EOF
    if n == 0:
      break
    # each image result
    res = []
    # for checking decode error
    lengths = set()
    for i in range(n):
      line = input().split()
      # first char
      char = line[0]
      # lengths of each expansion
      vals = [int(x) for x in line[1:]]
      # total length of line is sum of the values
      lengths.add(sum(vals))
      curr_line = []
      while vals:
        current = vals.pop(0)
        # expand character
        curr_line.append(char * current)
        # alternate character
        if char == '#':
          char = '.'
        else:
          char = '#'
      # add image
      res.append(''.join(curr_line))
    # handle decoding error
    if len(lengths) != 1:
      res.append('Error decoding image')
    # add entire result to total output
    total_out.append('\n'.join(res))
  # this avoids having that annoying new line at the end -_-
  print('\n\n'.join(total_out))

if __name__ == "__main__":
  main()
