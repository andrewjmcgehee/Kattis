/*
Rating: ~ 2.4 / 10
Link: https://open.kattis.com/problems/character
Complexity: O(1)
Memory: O(1)
*/

import java.util.*;
import java.io.*;

public class character {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    // Just math. There exist 2^n subsets of a set.
    // Subtract 1 for the empty set and subtract n
    // for the universal set
    System.out.println((int) Math.pow(2, n) - n - 1);
  }
}
