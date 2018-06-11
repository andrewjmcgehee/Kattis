#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    getline(cin, s);
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
