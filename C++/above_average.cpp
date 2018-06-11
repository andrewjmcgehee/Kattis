#include <iostream>
using namespace std;

int main() {
    int num_tests;
    cin >> num_tests;
    for (int i = 0; i < num_tests; i++) {
        int num_grades;
        cin >> num_grades;
        int grades[num_grades];
        int sum = 0;

        // sum grades
        for (int j = 0; j < num_grades; j++) {
            cin >> grades[j];
            sum += grades[j];
        }

        // get average
        double average = double(sum) / num_grades;
        int num_above = 0;
        for (int j = 0; j < num_grades; j++) {
            // count num above that average
            if (grades[j] > average) {
                num_above += 1;
            }
        }

        // get percent of students above average
        double percent_above = double(num_above) / num_grades * 100;
        printf("%.3f%%\n", percent_above);
    }
    return 0;
}
