# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/fridge
# Complexity: O(N) for N characters
# Memory: O(1) only ten digits

def main():
  line = input()
  chars = {i:0 for i in range(10)}
  # count frequency of chars
  for char in line:
    chars[int(char)] += 1

  # treat 1-9 as if they have a leading 0
  chars[0] += 1

  # purposefully impossible
  worst = float('inf')
  worst_char = '10'
  for k, v in chars.items():
    # track worst number of occurences and corresponding char
    if v < worst or int(k) < int(worst_char):
      worst_char = str(k)
      worst = v
  # will be some power of 10
  if worst_char == '0':
    out = '1' + ('0' * worst)
  # will be a repetition of least frequent character
  else:
    out = worst_char * (worst+1)
  print(out)

if __name__ == "__main__":
  main()
