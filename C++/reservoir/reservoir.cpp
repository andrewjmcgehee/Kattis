/*
Rating: ~ 4.7 / 10
Link: https://open.kattis.com/problems/reservoir
Complexity: O(N + K log(N)) for pre-processing N walls and K queries
Memory: O(N) for N walls
*/

#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

// faster IO
void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  fast();
  // for representing left most wall
  ll INF = 1000000000l;
  int cases;
  cin >> cases;
  for (int c = 0; c < cases; c++) {
    ll n;
    cin >> n;
    // stores x location and height
    vector<ll> coords(n+1);
    vector<ll> height(n+1);
    for (ll i = 1; i <= n; i++) {
      cin >> coords[i];
    }
    for (ll i = 1; i <= n; i++) {
      cin >> height[i];
    }
    // stores previous "rectangle"s height
    vector<pair<ll, ll>> prev_height;
    // left most "wall"
    prev_height.push_back({INF, -1});
    // stores amount of water to pass wall at index i
    vector<ll> water(n+1, 0);
    for (ll i = 1; i <= n ; i++) {
      // every wall requires at least the previous walls water
      water[i] += water[i-1];
      // this walls info
      ll curr_h = height[i];
      ll curr_w = coords[i];
      // stores difference in height between two walls
      ll curr_l = 0;
      while (true) {
        // peek at wall which stopped water most recently
        ll prev_h = prev_height.back().first;
        ll prev_w = prev_height.back().second;
        // trivial case, only goes back to previous wall
        if (prev_h > curr_h) {
          ll h = curr_h - curr_l;
          ll w = curr_w - prev_w - 1;
          water[i] += w * h;
          break;
        }
        // otherwise must find the previous wall
        ll h = curr_h - curr_l;
        ll w = curr_w - prev_w - 1;
        water[i] += w * h;
        // update values and try one wall prior
        curr_l = max(prev_h, curr_l);
        curr_w = prev_w + 1;
        prev_height.pop_back();
      }
      // add this wall
      prev_height.push_back({height[i], coords[i]});
    }
    // handle queries
    ll queries;
    cin >> queries;
    for (int i = 0; i < queries; i++) {
      ll volume;
      cin >> volume;
      // binary search to find index
      auto iter = lower_bound(water.begin(), water.end(), volume);
      // compensate for possibility of -1 index
      int index = max((int) (iter - water.begin()) - 1, 0);
      cout << index << '\n';
    }
  }
  return 0;
}
