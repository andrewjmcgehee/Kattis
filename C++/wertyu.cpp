/*
Rating: ~ 3.0 / 10
Link: https://open.kattis.com/problems/wertyu
Complexity: O(n) where n is number of chars in string
Memory: O(k) where k is size of given alphabet to be remapped
*/
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main() {
  // remap the alphabet - yikes...
  map <char, char> m;
  m.insert({'2', '1'});
  m.insert({'3', '2'});
  m.insert({'4', '3'});
  m.insert({'5', '4'});
  m.insert({'6', '5'});
  m.insert({'7', '6'});
  m.insert({'8', '7'});
  m.insert({'9', '8'});
  m.insert({'0', '9'});
  m.insert({'-', '0'});
  m.insert({'=', '-'});
  m.insert({'W', 'Q'});
  m.insert({'E', 'W'});
  m.insert({'R', 'E'});
  m.insert({'T', 'R'});
  m.insert({'Y', 'T'});
  m.insert({'U', 'Y'});
  m.insert({'I', 'U'});
  m.insert({'O', 'I'});
  m.insert({'P', 'O'});
  m.insert({'[', 'P'});
  m.insert({']', '['});
  m.insert({92, ']'});
  m.insert({'S', 'A'});
  m.insert({'D', 'S'});
  m.insert({'F', 'D'});
  m.insert({'G', 'F'});
  m.insert({'H', 'G'});
  m.insert({'J', 'H'});
  m.insert({'K', 'J'});
  m.insert({'L', 'K'});
  m.insert({';', 'L'});
  m.insert({39, ';'});
  m.insert({'X', 'Z'});
  m.insert({'C', 'X'});
  m.insert({'V', 'C'});
  m.insert({'B', 'V'});
  m.insert({'N', 'B'});
  m.insert({'M', 'N'});
  m.insert({',', 'M'});
  m.insert({'.', ','});
  m.insert({'/', '.'});
  m.insert({' ', ' '});

  string s;
  while (getline(cin, s)) {
      vector <char> v;

      // translate char by char
      for (int i = 0; i < s.length(); i++) {
          v.push_back(m[s.at(i)]);
      }
      for (int i = 0; i < s.length(); i++) {
          cout << v[i];
      }
      cout << '\n';
  }
  return 0;
}
