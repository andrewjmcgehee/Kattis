/*
Rating: ~ 1.2 / 10
Link: https://open.kattis.com/problems/quadrant
Complexity: O(1)
Memory: O(1)
*/

import java.util.Scanner;

public class quadrant {
  public static void main(String[] args) {
    Scanner io = new Scanner(System.in);
    int x = io.nextInt();
    int y = io.nextInt();

    // simple ad hoc problem
    if (x > 0) {
      if (y > 0) {
        System.out.println("1");
      }
      else {
        System.out.println("4");
      }
    }
    else {
      if (y > 0) {
        System.out.println("2");
      }
      else {
        System.out.println("3");
      }
    }
  }
}
