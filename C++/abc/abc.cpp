/*
Rating: ~ 1.7 / 10
Link: https://open.kattis.com/problems/abc
Complexity: O(N log(N)) due to sorting N numbers
Memory: O(N) where N is numbers to be sorted
*/

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
    // convert char into an index
    index = c - 'A';
    printf("%i ", nums[index]);
  }
  printf("\n");
  return 0;
}
