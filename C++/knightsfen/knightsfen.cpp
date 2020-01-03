/*
Rating: ~ 3.1 / 10
Link: https://open.kattis.com/problems/knightsfen
*/

#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <vector>
using namespace std;

typedef long long ll;

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

typedef vector<vector<char>> state;

int main() {
  state board = {
    {'1','1','1','1','1'},
    {'0','1','1','1','1'},
    {'0','0',' ','1','1'},
    {'0','0','0','0','1'},
    {'0','0','0','0','0'}
  };
  queue<state> q;
  q.push(board);
  map<state, int> memo;
  memo[board] = 0;
  vector<pair<int, int>> moves = {
    {1,2}, {-1,2}, {1,-2}, {-1,-2},
    {2,1}, {-2,1}, {2,-1}, {-2,-1}
  };

  while (!q.empty()) {
    state s = q.front();
    q.pop();
    if (memo[s] == 10) break;
    int blankx, blanky;
    bool found = false;
    for (int i = 0; i < 5; i++) {
      for (int j = 0; j < 5; j++) {
        if (s[i][j] == ' ') {
          blankx = i;
          blanky = j;
          found = true;
          break;
        }
      }
      if (found) break;
    }
    state cpy = s;
    for (auto i : moves) {
      int nextx = blankx + i.first;
      int nexty = blanky + i.second;
      if (nextx >= 0 && nextx < 5 && nexty >= 0 && nexty < 5) {
        swap(cpy[blankx][blanky], cpy[nextx][nexty]);
        if (memo.count(cpy) == 0) {
          memo[cpy] = memo[s] + 1;
          q.push(cpy);
        }
        swap(cpy[blankx][blanky], cpy[nextx][nexty]);
      }
    }
  }
  
  int cases;
  cin >> cases;
  while (cases--) {
    for (int i = 0; i < 5; i++) {
      cin.ignore();
      for (int j = 0; j < 5; j++) {
        board[i][j] = getchar();
      }
    }
    if (memo.count(board) > 0) {
      cout << "Solvable in " << memo[board] << " move(s).\n";
    } else {
      cout << "Unsolvable in less than 11 move(s).\n";
    }
  }
  return 0;
}
