/*
Rating: ~ 4.5 / 10
Link: https://open.kattis.com/problems/deduplicatingfiles
Complexity: O(N^2) where N is number of files in hash map
Memory: O(N) where N is number of files in hash map
*/

#include <iostream>
#include <map>
#include <string>
using namespace std;

// hash function as defined in problem statement
char get_hash(string s) {
  char c = char(0);
  for (int i = 0; i < s.length(); i++) {
    c ^= s[i];
  }
  return c;
}

int main() {
  while (true) {
    int n;
    cin >> n;
    if (n == 0) {
      break;
    }
    cin >> ws;

    // create hash map keeping track of how many occurences of a given string
    // there are
    map<string, int> files;
    for (int i = 0; i < n; i++) {
      string s;
      getline(cin, s);

      if (files.find(s) == files.end()) {
        files[s] = 0;
      }
      files[s] += 1;
    }

    // iterates through hashmap twice considering all pairwise relationships
    // (EVEN identity pairs)
    int collisions = 0;
    for (auto const& k1 : files) {
      string file1 = k1.first;
      int num1 = k1.second;
      char hash1 = get_hash(file1);
      for (auto const& k2 : files) {
        string file2 = k2.first;
        int num2 = k2.second;
        if (file1.compare(file2) != 0) {
          char hash2 = get_hash(file2);
          // if the hashes match and the strings are different then
          // the collision occurs with every occurence of each
          // duplicate string. Imagine a "rectangle." The area is height
          // times the length.
          if (hash1 == hash2) {
            collisions += num1*num2;
          }
        }
      }
    }
    // collisions can be int divided by 2 because the pairwise relationships
    // can be modeled as an adjacency matrix. the diagonal includes all the
    // identity pairs (every string is a hash collision with itself) and
    // each half of the rectangle will be symmetrical because if string a
    // collides with string b, string b will also collide with string a.
    collisions /= 2;
    cout << files.size() << " " << collisions << '\n';
  }
  return 0;
}

