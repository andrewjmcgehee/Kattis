/*
Rating: ~ 3.8 / 10
Link: https://open.kattis.com/problems/addingwords
Complexity: O(k) where k is number of operands
Memory: O(w) where w is number of unique terms in dictionary
*/

#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <iterator>

using namespace std;

int main() {
    // solved with two hash maps that serve to translate back and forth
    string command;
    map<string, int> str_to_int;
    map<int, string> int_to_str;

    while (cin >> command) {
        // def
        if (command.compare("def") == 0) {
            string key;
            int value;
            cin >> key;
            cin >> value;
            // if key already in map, erase it so it can be updated
            if (str_to_int.find(key) != str_to_int.end()) {
                int old = str_to_int[key];
                str_to_int.erase(key);
                int_to_str.erase(old);
            }
            // add key value pair to map
            str_to_int[key] = value;
            int_to_str[value] = key;
        }
        // calc
        else if (command.compare("calc") == 0) {
            string line, key;
            char c;
            int sum = 0;
            int multiplier = 1;
            string solution = "";

            getline(cin, line);
            // substring from 1 to end to get rid of extra whitespace
            istringstream iss(line.substr(1));

            while (iss >> key) {
                // if any key is not found, equation can't be calculated
                if (str_to_int.find(key) == str_to_int.end()) {
                    solution = "unknown";
                    break;
                }
                else {
                    sum += multiplier * str_to_int[key];
                }

                // get operator
                iss >> c;
                if (c == '+') {
                    multiplier = 1;
                }
                else if (c == '-') {
                    multiplier = -1;
                }
                // operator is '='
                else {
                    if (int_to_str.find(sum) != int_to_str.end()) {
                        solution = int_to_str[sum];
                    }
                    else {
                        solution = "unknown";
                    }
                    break;
                }
            }
            cout << line.substr(1) << " " << solution << '\n';
        }
        // clear
        else if (command.compare("clear") == 0) {
            str_to_int.clear();
            int_to_str.clear();
        }
    }
    return 0;
}
