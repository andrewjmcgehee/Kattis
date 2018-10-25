/*
Rating: ~ 3.2 / 10
Link: https://open.kattis.com/problems/almostperfect
Complexity: O(sqrt(N) + K) where N is the number and K is the number of factors
Memory: O(PI(N)) where PI(N) is a function of number of prime factors
*/

import java.util.*;

public class almostperfect {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while (in.hasNext()) {
      int num = in.nextInt();
      // simple set to store all factors for a given number n
      HashSet<Integer> factors = new HashSet<Integer>();
      factors.add(1);

      // only need to iterate through square root of n to find all factors
      int root = (int) Math.floor(Math.sqrt(num));
      for (int i = 2; i <= root; i++) {
        if (num % i == 0) {
          // add factor
          factors.add(i);
          // add factor counterpart
          factors.add(num / i);
        }
      }

      long sum = 0;
      for (Integer i : factors) {
        sum += i;
      }
      // output
      if (sum == num) {
        System.out.println(num + " perfect");
      }
      else if (Math.abs(num - sum) <= 2) {
        System.out.println(num + " almost perfect");
      }
      else {
        System.out.println(num + " not perfect");
      }
    }
  }
}
