/*
Rating: ~ 1.2 / 10
Link: https://open.kattis.com/problems/hissingmicrophone
Complexity: O(c) where c is number of chars in word
Memory: O(1)
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    getline(cin, s);

    // check for two sequential s characters
    bool found = false;
    for (int i = 0; i < s.length() - 1; i++) {
        if (s[i] == 's' and s[i+1] == 's') {
            cout << "hiss" << '\n';
            found = true;
            break;
        }
    }

    if (!found) {
        cout << "no hiss" << '\n';
    }

    return 0;
}
