# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/akcija
# Complexity: O(N log(N)) to sort N books
# Memory: O(N) for N books

def main():
  num_books = int(input())
  books = []
  for i in range(num_books):
    books.append(int(input()))
  # sort books and reverse the order.
  books.sort()
  books.reverse()

  free_books = []
  # grab every 3rd book
  for i in range(num_books):
    if (i+1) % 3 == 0:
      free_books.append(books[i])
  # price is price of books - price of free books
  total = sum(books) - sum(free_books)
  print(total)

if __name__ == '__main__':
    main()
