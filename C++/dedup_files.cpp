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

        int collisions = 0;
        for (auto const& k1 : files) {
            string file1 = k1.first;
            int num1 = k1.second;
            char hash1 = get_hash(file1);
            for (auto const& k2 : files) {
                string file2 = k2.first;
                int num2 = k2.second;
                // if strings are exactly equal, we don't consider it a hash collision
                if (file1.compare(file2) != 0) {
                    char hash2 = get_hash(file2);
                    if (hash1 == hash2) {
                        // there n*k collisions when considered in both directions
                        collisions += num1*num2;
                    }
                }
            }
        }
        // divided by two because we are only considering pairwise relationships
        collisions /= 2;
        cout << files.size() << " " << collisions << '\n';
    }
    return 0;
}
