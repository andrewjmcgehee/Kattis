/*
Rating: ~ 2.1 / 20
Link: https://open.kattis.com/problems/permutedarithmeticsequence
Complexity: O(N log(N)) for N values to sort them
Memory: O(N) for N values
*/

import java.util.*;

public class permutedarithmeticsequence {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    // test cases
    int n = in.nextInt();
    in.nextLine();

    for (int i = 0; i < n; i++) {
      // arr size
      int m = in.nextInt();
      int[] seq = new int[m];
      for (int j = 0; j < m; j++) {
        seq[j] = in.nextInt();
      }

      // all differences must equivalent for sequence to be arithmetic
      int diff = seq[1] - seq[0];
      boolean sortedArithmetic = true;
      for (int j = 1; j < m-1; j++) {
        if (seq[j+1] - seq[j] != diff) {
          sortedArithmetic = false;
          break;
        }
      }

      // to check for permuted arithmetic sort and do same check
      Arrays.sort(seq);
      boolean permutedArithmetic = true;
      diff = seq[1] - seq[0];
      for (int j = 1; j < m-1; j++) {
        if (seq[j+1] - seq[j] != diff) {
          permutedArithmetic = false;
          break;
        }
      }
      // print result
      if (sortedArithmetic) {
        System.out.println("arithmetic");
      }
      else if (permutedArithmetic) {
        System.out.println("permuted arithmetic");
      }
      else {
        System.out.println("non-arithmetic");
      }
    }
  }
}
