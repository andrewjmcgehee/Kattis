/*
Rating: ~ 1.8 / 10
Link: https://open.kattis.com/problems/greedilyincreasing
Complexity: O(n) where n is number of ints in sequence
Memory: O(1)
*/

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace  std;

int main() {
  // I/O optimizations
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int numCases;
  cin >> numCases;
  cin >> ws;

  string line;
  getline(cin, line);

  vector<int> collection;

  // must include first number
  int current;
  stringstream ss(line);
  ss >> current;
  collection.push_back(current);

  for (int i = 0; i < numCases - 1; i++) {
    int next;
    ss >> next;
    // only add to vector if greater than current int
    if (next > current) {
      current = next;
      collection.push_back(current);
    }
  }

  // print results
  cout << collection.size() << '\n';
  for (int i = 0; i < collection.size(); i++) {
    cout << collection[i] << " ";
  }
  cout << '\n';
}
