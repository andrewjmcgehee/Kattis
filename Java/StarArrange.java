/*
Rating: ~ 1.4 / 10
Link: https://open.kattis.com/problems/stararrangements
Complexity: O(N) for N stars
Memory: O(1)
*/

import java.util.Scanner;

public class StarArrange {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    // initial out
    System.out.println(n + ":");

    // only need to go through half of number
    for (int i = 1; i < (n / 2) + 1; i++) {
      // candidate for same size columns
      if (i != 1 && n % i == 0) {
        System.out.println(i + "," + i);
      }
      // candidate for alternating
      if (n % (2*i + 1) == 0 || n % (2*i + 1) == i + 1) {
        System.out.println(i+1 + "," + i);
      }
    }
  }
}
