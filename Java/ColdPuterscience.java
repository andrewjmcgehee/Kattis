/*
Rating: ~ 1.2 / 10
Link: https://open.kattis.com/problems/cold
Complexity: O(N) for N temperatures
Memory: O(1)
*/

import java.util.*;

public class ColdPuterScience {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int temps = in.nextInt();
    // simple scan
    int lessThanZero = 0;
    for (int i = 0; i < temps; i++) {
      int currentTemp = in.nextInt();
      if (currentTemp < 0) {
        lessThanZero++;
      }
    }
    System.out.println(lessThanZero);
  }
}
