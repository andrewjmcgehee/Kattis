/*
Rating: ~ 1.2 / 10
Link: https://open.kattis.com/problems/trik
Complexity: O(N) where N is number of chars in string
Memory: O(1)
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
  string s;
  getline(cin, s);

  int position = 1;
  for (int i = 0; i < s.length(); i++) {
    char c = s[i];

    // simple switch statement to manipulate position
    switch(c) {
      case 'A':
        if (position == 1) {
          position = 2;
        }
        else if (position == 2) {
          position = 1;
        }
        break;
      case 'B':
        if (position == 2) {
          position = 3;
        }
        else if (position == 3) {
          position = 2;
        }
        break;
      case 'C':
        if (position == 1) {
          position = 3;
        }
        else if (position == 3) {
          position = 1;
        }
        break;
    }
  }
  cout << position << '\n';
  return 0;
}
