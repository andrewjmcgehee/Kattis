/*
Rating: ~ 1.3 / 10
Link: https://open.kattis.com/problems/judgingmoose
Complexity: O(1)
Memory: O(1)
*/

#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
  int a, b, tines;
  scanf("%i %i", &a, &b);
  // don't care about smaller number
  tines = max(a, b) * 2;

  if (a + b == 0) {
    printf("Not a moose\n");
  }
  // balanced
  else if (a == b) {
    printf("Even %i\n", tines);
  }
  // not balanced
  else {
    printf("Odd %i\n", tines);
  }
  return 0;
}
