/*
Rating: ~ 1.8 / 10
Link: https://open.kattis.com/problems/tetration
Complexity: O(1)
Memory: O(1)
*/

import java.util.Scanner;

public class tetration {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double x = in.nextDouble();
    // infinite tetration can be solved to be N^(1/N)
    System.out.println(Math.pow(x, (1.0 / x)));
  }
}
