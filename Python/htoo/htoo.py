# Rating: ~ 4.2 / 10
# Link: https://open.kattis.com/problems/htoo
# Complexity: O(N + K) for a string of N chars and a string of K chars
# Memory: O(N + K) for dictionaries representing each string of N and K chars

# helper function to parse a single complete number in the character sequence
def get_number(seq, i):
  num = []
  index = i
  while index < len(seq):
    # stop on first non number char
    if not seq[index].isnumeric():
      break
    num.append(seq[index])
    index += 1
  num = int(''.join(num))
  # need to know how far forard we moved in the sequence
  return (num, index)

# converts a sequence to an array of tuples representing elements and frequency
def convert_seq(seq, num_molecules):
  res = []
  i = 0
  while i < len(seq):
    # always on a single char
    curr = seq[i]
    if i+1 < len(seq) and seq[i+1].isnumeric():
      # process number after atom
      num_atoms, i = get_number(seq, i+1)
      res.append((curr, num_atoms * num_molecules))
      continue
    # no number following so we treat as if a 1 followed it
    res.append((curr, num_molecules))
    i += 1
  return res

def main():
  seq, num = input().split()
  num = int(num)
  target = input()

  # convert materials to a dictionary of total amounts available
  atoms = convert_seq(seq, num)
  materials = dict()
  for atom in atoms:
    # avoid key errors
    if atom[0] not in materials:
      materials[atom[0]] = 0
    materials[atom[0]] += atom[1]

  # convert target sequence to a dictionary of total amounts required
  atoms = convert_seq(target, 1)
  molecule = dict()
  for atom in atoms:
    if atom[0] not in molecule:
      molecule[atom[0]] = 0
    molecule[atom[0]] += atom[1]

  # will always find a min lower
  curr_min = float('inf')
  for element in molecule:
    required = molecule[element]
    # need an element which wasnt in given materials
    if element not in materials:
      curr_min = 0
      break
    available = materials[element]
    # will be the bounded by the maximum we can make with the worst case (min) atom
    curr_min = min(curr_min, available // required)
  print(curr_min)

if __name__ == "__main__":
  main()
