#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> nums;
  int tmp;
  for (int i = 0; i < 3; i++) {
    scanf("%i ", &tmp);
    nums.push_back(tmp);
  }
  sort(nums.begin(), nums.end());

  char c;
  int index;
  for (int i = 0; i < 3; i++) {
    scanf("%c", &c);
    index = c - 'A';
    printf("%i ", nums[index]);
  }
  printf("\n");
  return 0;
}
