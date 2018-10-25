/*
Rating: ~ 3.2 / 10
Link: https://open.kattis.com/problems/stockbroker
Complexity: O(N) for N prices
Memory: O(1)
*/

import java.util.*;

public class stockbroker {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    // previous is higher than any initial value could be
    long previous = 1000;
    long money = 100;
    for (int i = 0; i < n; i++) {
      int current = in.nextInt();
      // we only need to worry about selling stocks when it is profitable, we could
      // simulate buying, but it really doesn't serve a purpose

      // note that you cannot have more than 100000 shares at a time, so we can only
      // profit a maximum of 100000 shares worth.
      if (current > previous) {
        money += Math.min((money / previous), 100000) * (current - previous);
      }
      previous = current;
    }
    System.out.println(money);
  }
}
