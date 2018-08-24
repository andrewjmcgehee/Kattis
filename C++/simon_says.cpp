/*
Rating: ~ 2.2 / 10
Link: https://open.kattis.com/problems/simon
Complexity: O(n) where n is number of strings to parse
Memory: O(1)
*/

#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// helper to split a string by a delimiter
vector<string> split(const string& str, char delimiter) {
    vector<string> tokens;
    string token;
    stringstream ss(str);
    while (getline(ss, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

int main() {
    int cases;
    cin >> cases;
    cin >> ws;

    for (int i = 0; i < cases; i++) {
        string s;
        getline(cin, s);

        vector<string> tokens = split(s, ' ');

        // check for simon says
        if (tokens.size() > 2
                && tokens[0].compare("simon") == 0
                && tokens[1].compare("says") == 0) {
            for (int j = 2; j < tokens.size() - 1; j++) {
                cout << tokens[j] << " ";
            }
            if (tokens.size() != 2) {
                cout << tokens[tokens.size() - 1] << '\n';
            }
            else {
                cout << '\n';
            }
        }
        else {
            cout << '\n';
        }
    }
}

