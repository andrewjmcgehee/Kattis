/*
Rating: ~ 2.3 / 10
Link: https://open.kattis.com/problems/armystrengthhard
Complexity: O(N log N) for sorting N elements where N is the size of the larger array
Memory: O(N + M) where N and M are the sizes of the sorted arrays
*/

#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
  int t;
  scanf("%i", &t);

  while (t--) {
    int n, m;
    scanf("%d%d", &n, &m);

    vector<int> god(n);
    vector<int> mecha(m);

    // read in soldiers
    for (int i = 0; i < n; i++) {
      scanf("%i", &god[i]);
    }
    for (int i = 0; i < m; i++) {
      scanf("%i", &mecha[i]);
    }

    // sort both arrays
    sort(god.begin(), god.end());
    sort(mecha.begin(), mecha.end());

    // i will point to weakest alive soldier in godzillas army
    // j will point to weakest alive soldier in mechas army
    int i = 0;
    int j = 0;
    while (i != god.size() && j != mecha.size()) {
      // only case where godzillas soldier dies is if its strictly less than mechas
      if (god[i] < mecha[j]) {
        i++;
      }
      else {
        j++;
      }
    }

    if (i != god.size()) {
      printf("Godzilla\n");
    }
    else {
      printf("MechaGodzilla\n");
    }
  }
  return 0;
}

