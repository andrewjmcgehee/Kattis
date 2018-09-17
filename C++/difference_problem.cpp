/*
Rating: ~ 2.2 / 10
Link: https://open.kattis.com/problems/different
Complexity: O(1)
Memory: O(1)
*/

#include <iostream>
#include <cmath>
using namespace std;

// secret sauce is all in which data type you use and taking the absolute value
int main() {
  long long a, b;
  while (cin >> a >> b) {
    long long diff = abs(a - b);
    cout << diff << '\n';
  }
}
