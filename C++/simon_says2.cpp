/*
Rating: ~ 1.6 / 10
Link: https://open.kattis.com/problems/simonsays
Complexity: O(n) where n is number of strings
Memory: O(1)
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int cases;
  cin >> cases;
  cin >> ws;
  // find simon says
  for (int i = 0; i < cases; i++) {
    string s;
    getline(cin, s);

    int pos = s.find("Simon says ");

    // if at the start, print it
    if (pos == 0) {
      cout << s.substr(11) << '\n';
    }
  }
  return 0;
}
