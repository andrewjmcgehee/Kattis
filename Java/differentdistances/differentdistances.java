/*
Rating: ~ 1.5 / 10
Link: https://open.kattis.com/problems/differentdistances
Complexity: O(1)
Memory: O(1)
*/

import java.util.*;

public class differentdistances {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    // just math
    double x1 = in.nextDouble();
    while (x1 != 0) {
      double y1 = in.nextDouble();
      double x2 = in.nextDouble();
      double y2 = in.nextDouble();
      double p = in.nextDouble();

      double xDist = Math.abs(x1 - x2);
      double yDist = Math.abs(y1 - y2);

      double radicand = Math.pow(xDist, p) + Math.pow(yDist, p);
      System.out.println(Math.pow(radicand, 1/p));
      x1 = in.nextDouble();
    }
  }
}
