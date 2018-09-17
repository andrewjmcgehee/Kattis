#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
  int a, b, tines;
  scanf("%i %i", &a, &b);
  tines = max(a, b) * 2;

  if (a + b == 0) {
    printf("Not a moose\n");
  }
  else if (a == b) {
    printf("Even %i\n", tines);
  }
  else {
    printf("Odd %i\n", tines);
  }
  return 0;
}
