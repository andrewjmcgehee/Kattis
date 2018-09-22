/*
Rating: ~ 6.4 / 10
Link: https://open.kattis.com/problems/dartscoring
Compexity: O(N log(N)) for the initial sort of points in graham scan
Memory: O(N) for N points
*/

import java.util.*;

public class DartScoring {
  // simple point class
  static class Point {
    double x;
    double y;
    public Point(double x, double y) {
      this.x = x;
      this.y = y;
    }

    public String toString() {
      return this.x + " " + this.y;
    }
  }
  // we must be able to compare points by polar angle for graham scan
  static class PolarComparator implements Comparator<Point> {
    Point p0;
    public PolarComparator(Point p0) {
      this.p0 = p0;
    }

    public int compare(Point p1, Point p2) {
      double theta1 = Math.atan2((p1.y - p0.y), (p1.x - p0.x));
      double theta2 = Math.atan2((p2.y - p0.y), (p2.x - p0.x));
      if (theta1 - theta2 < 0) {
        return -1;
      }
      else if (theta1 == theta2) {
        return 0;
      }
      else {
        return 1;
      }
    }
  }

  // cross product can tell us about rotation of angle created by 2 vectors
  // If positive p0->p1->p2 rotate counter-clockwise if visited in that
  // order, if negative clockwise, if 0 they are colinear.
  public static int crossProduct(Point p0, Point p1, Point p2) {
    double rotation = (p1.x - p0.x) * (p2.y - p0.y)
                    - (p2.x - p0.x) * (p1.y - p0.y);
    if (rotation < 0) {
      return -1;
    }
    else if (rotation == 0) {
      return 0;
    }
    else {
      return 1;
    }
  }

  // helper function for euclidean distance
  public static double getDistance(Point a, Point b) {
    double deltaX = a.x - b.x;
    double deltaY = a.y - b.y;
    return Math.sqrt(Math.pow(deltaX, 2) + Math.pow(deltaY, 2));
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while (in.hasNext()) {
      String[] coords = in.nextLine().split(" ");
      ArrayList<Point> darts = new ArrayList<Point>();
      // start will be point with lowest y and left most x, so we
      // initially set it to a point higher and further right than possible
      Point start = new Point(100, 100);

      for (int i = 0; i < coords.length; i += 2) {
        // get pairs to create points
        double x = Double.parseDouble(coords[i]);
        double y = Double.parseDouble(coords[i+1]);
        Point p = new Point(x, y);
        if (p.y < start.y) {
          start = p;
        }
        else if (p.y == start.y) {
          if (p.x < start.x) {
            start = p;
          }
        }
        darts.add(p);
      }

      // score is calculated by 100 * numDarts / (1 + length of convex hull)
      double perimeter = 0;
      double numDarts = darts.size();
      double score = 0;
      // 1 dart gives score of 100
      if (numDarts == 1) {
        score = 100.0;
        System.out.println(score);
      }
      // 2 darts gives score of 100 * 2 / (1 + 2 * euclidean distance between them (there and back))
      else if (numDarts == 2) {
        perimeter += getDistance(darts.get(0), darts.get(1));
        score = 100 * 2 / (1 + 2*perimeter);
        System.out.println(score);
      }
      // otherwise calculate score as normal
      else {
        // sort by polar angles with lowest and left most point
        Collections.sort(darts, new PolarComparator(start));
        Stack<Point> stack = new Stack<Point>();
        // push on first 3 darts and visit in order (counter clockwise)
        stack.push(darts.get(0));
        stack.push(darts.get(1));
        stack.push(darts.get(2));
        // accept or reject points for convex hull
        for (int i = 3; i < darts.size(); i++) {
          Point top = stack.peek();
          Point next = stack.get(stack.size() - 2);
          int rotation = crossProduct(next, top, darts.get(i));

          // eliminate downstream clockwise rotations
          while (rotation <= 0 && stack.size() >= 3) {
            stack.pop();
            top = stack.peek();
            next = stack.get(stack.size() - 2);
            rotation = crossProduct(next, top, darts.get(i));
          }
          stack.push(darts.get(i));
        }
        // get perimeter, stack can be referenced by index like ArrayList
        for (int i = 0; i < stack.size() - 1; i++) {
          Point p1 = stack.get(i);
          Point p2 = stack.get(i+1);
          perimeter += getDistance(p1, p2);
        }
        // connect final point and initial point
        Point p1 = stack.get(stack.size() - 1);
        Point p2 = stack.get(0);
        perimeter += getDistance(p1, p2);
        // calculate and print
        score = 100 * darts.size() / (1 + perimeter);
        System.out.println(score);
      }
    }
  }
}
