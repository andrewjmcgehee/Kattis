#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int num_polygons;
    cin >> num_polygons;
    for (int poly = 0; poly < num_polygons; poly++) {
        int num_points;
        cin >> num_points;

        // need n + 1 space to repeat first point at end of array
        int points[num_points+1][2];

        for (int i = 0; i < num_points; i++) {
            int x;
            int y;
            cin >> x;
            cin >> y;
            points[i][0] = x;
            points[i][1] = y;
        }

        // last point is duplicate of first
        points[num_points][0] = points[0][0];
        points[num_points][1] = points[0][1];


        // area of convex polygon can be calculated from 0.5 * cross product of
        // array of points as long as points are visited in either clockwise
        // or counterclockwise order and if first point is repeated at end
        // this essentially calculates sum of area of all triangles in polygon
        int first_term = 0;
        int second_term = 0;

        for (int i = 0; i < num_points; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[i+1][0];
            int y2 = points[i+1][1];

            first_term += x1 * y2;
            second_term += x2 * y1;
        }
        double total_area = 0.5 * (first_term - second_term);
        cout << total_area << '\n';
    }
}
