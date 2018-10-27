/*
Rating: ~ 1.2 / 10
Link: https://open.kattis.com/problems/pet
Complexity: O(N) where N is number of students
Memory: O(1)
*/

#include <iostream>
using namespace std;

int main() {
  int a, b, c, d;
  int sum;
  int pos = -1;
  int max = -1;

  // basic scan
  for (int i = 1; i <= 5; i++) {
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    sum = a + b + c + d;
    max = (max > sum) ? max : sum;
    pos = (max > sum) ? pos : i;
  }
  cout << pos << " " << max << '\n';
  return 0;
}
