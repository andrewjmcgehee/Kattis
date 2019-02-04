# Rating: ~ 3.6 / 10
# Link: https://open.kattis.com/problems/a1paper
# Complexity: O(N) for N sheet divisions
# Memory: O(N) for N sheet divisions

def main():
  # defined length and width of an A2 paper
  length = pow(2, -3/4)
  width = pow(2, -5/4)

  # dont need in python
  trash = input()
  # get number of papers for each sheet
  papers = [int(x) for x in input().split()]

  # holds tape needed
  tape = 0
  # assuming we were to use 1 A1 paper
  sheets_needed = 1

  for i in range(len(papers)):
    # for each division the number of sheets we need to represent
    # the previous division doubles
    sheets_needed *= 2

    # pretend we are taping the entire perimeter
    perimeter = 2*(length + width)

    # we have enough sheets or more than enough to finish an A1 paper
    if papers[i] >= sheets_needed:
      # add the perimeter needed
      tape += sheets_needed*perimeter
      sheets_needed = 0
    # we need to continue, so greedily use the sheets available
    # and update the number of sheets needed
    else:
      tape += papers[i]*perimeter
      sheets_needed -= papers[i]

    # update dimensions
    updated_len = width
    width = length/2
    length = updated_len

  # we found some way of constructing the paper
  if sheets_needed == 0:
    # we must subtract the perimeter of an A1 sheet which has double
    # the area so 2^(-5/4) becomes 2^(-1/4) and perimeter equals
    # 2*(length + width)
    result = tape - 2*(pow(2, -1/4) + pow(2, -3/4))
    # since we taped the perimeters and not just the edges we needed
    # every interior edge has been taped twice
    result /= 2
    print(result)
  else:
    print('impossible')

if __name__ == "__main__":
  main()
