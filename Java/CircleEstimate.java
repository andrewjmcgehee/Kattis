/*
Rating: ~ 1.4 / 10
Link: https://open.kattis.com/problems/estimatingtheareaofacircle
Complexity: O(1)
Memory: O(1)
*/

import java.util.*;

public class CircleEstimate {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double r = in.nextDouble();
    // total dots in square
    double m = in.nextDouble();
    // dots in circle
    double c = in.nextDouble();
    while (r != 0 && m != 0 && c != 0) {
      double realArea = Math.PI * Math.pow(r, 2);
      // generating a smaller square relative to larger square
      double estimate = c / m * Math.pow(2 * r, 2);
      System.out.println(realArea + " " + estimate);

      r  = in.nextDouble();
      m = in.nextDouble();
      c = in.nextDouble();
    }
  }
}
