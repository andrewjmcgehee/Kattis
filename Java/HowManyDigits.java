/*
Rating: ~ 3.7 / 10
Link: https://open.kattis.com/problems/howmanydigits
Complexity: O(1)
Memory: O(1)
*/

import java.util.Scanner;

// uses Stirling's approximation
public class HowManyDigits {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while (in.hasNext()) {
      double n = in.nextInt();
      in.nextLine();
      // formula for stirling's approximation
      double approx = Math.sqrt(2*Math.PI*n) * Math.pow(n/Math.E, n);
      // convert to string
      String a = Long.toString((long) approx);
      System.out.println(a.length());
    }
  }
}
