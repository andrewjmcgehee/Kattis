/*
Rating: ~ 3.4 / 10
Link: https://open.kattis.com/problems/boggle
Complexity: O(NK) for N words of max size K to create Trie
Memory: O(K) for Trie storing words of max length K and constan alphabet size
*/

#include <iostream>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

typedef long long ll;

// fast io
void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

// easy Trie
bool valid_prefix[8][26];
unordered_set<string> valid_word;

// helper to check prefixes
bool is_valid_prefix(string chain) {
  for (int i = 0; i < chain.length(); i++) {
    if (!valid_prefix[i][chain[i]-65]) return false;
  }
  return true;
}

// helper to get neighbor indexes in row major form
vector<int> get_neighbors(int location) {
  int r = location / 4;
  int c = location % 4;
  vector<int> neighbors;
  if (r-1 >= 0) {
    neighbors.push_back(4*(r-1) + c);
    if (c-1 >= 0) {
      neighbors.push_back(4*(r-1) + c - 1);
    }
    if (c+1 < 4) {
      neighbors.push_back(4*(r-1) + c + 1);
    }
  }
  if (r+1 < 4) {
    neighbors.push_back(4*(r+1) + c);
    if (c-1 >= 0) {
      neighbors.push_back(4*(r+1) + c - 1);
    }
    if (c+1 < 4) {
      neighbors.push_back(4*(r+1) + c + 1);
    }
  }
  if (c-1 >= 0) {
    neighbors.push_back(4*r + c - 1);
  }
  if (c+1 < 4) {
    neighbors.push_back(4*r + c + 1);
  }
  return neighbors;
}

// dfs from each start
void dfs(vector<string> board, int s, string chain, set<string> &found) {
  // treat like a stack
  vector<int> stack;
  // track which elements are already in chain
  vector<bool> vis(16, false);
  stack.push_back(s);
  while (stack.size() > 0) {
    int current = stack.back();
    // seen before
    if (vis[current]) {
      chain = chain.substr(0, chain.length()-1);
      vis[current] = false;
      stack.pop_back();
    }
    else {
      vis[current] = true;
      // convert to row and col
      int r = current / 4;
      int c = current % 4;
      // add to chain
      chain += board[r][c];
      // new word
      if (valid_word.find(chain) != valid_word.end()) {
        found.insert(chain);
      }
      // longer word is possible
      if (chain.length() < 9 && is_valid_prefix(chain)) {
        for (int n : get_neighbors(current)) {
          if (!vis[n] && is_valid_prefix(chain + board[n/4][n%4])) {
            stack.push_back(n);
          }
        }
      }
    }
  }
}

int main() {
  fast();
  string word;
  int w;
  cin >> w;
  cin >> ws;
  for (int i = 0; i < w; i++) {
    getline(cin, word);
    // add to dictionary
    valid_word.insert(word);
    for (int j = 0; j < word.length(); j++) {
      char c = word[j];
      // build prefixes
      valid_prefix[j][c-65] = true;
    }
  }
  cin >> ws;
  int b;
  cin >> b;
  cin >> ws;
  // 4 rows of 4 chars
  vector<string> board(4);
  for (int i = 0; i < b; i++) {
    string row;
    for (int r = 0; r < 4; r++) {
      getline(cin, board[r]);
    }
    if (i != b-1) cin >> ws;
    set<string> found;
    // dfs from each index
    for (int start = 0; start < 16; start++) {
      dfs(board, start, "", found);
    }
    string longest = "";
    // scores for words of any length
    int scores[] = {0, 0, 0, 1, 1, 2, 3, 5, 11};
    int score = 0;
    // calculate longest and score
    for (string word : found) {
      // set is sorted so first found will always be lexicographically smallest
      if (word.length() > longest.length()) {
        longest = word;
      }
      score += scores[word.length()];
    }
    cout << score << ' ' << longest << ' ' << found.size() << '\n';
  }
  return 0;
}
