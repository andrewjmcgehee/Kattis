/*
Rating: ~ 1.2 / 10
Link: https://open.kattis.com/problems/autori
Complexity: O(c) where c is number of chars in string
Memory: O(1)
*/

#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    // I/O optimizations
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    getline(cin, s);
    vector<char> v;

    // always get first char
    v.push_back(s[0]);
    for (int i = 1; i < s.length(); i++) {
        // 45 is ascii value for '-'
        if (s[i] == 45) {
            v.push_back(s[i+1]);
        }
    }

    for (int i = 0; i < v.size(); i++) {
        cout << v[i];
    }
    cout << '\n';
    return 0;
}
