/*
Rating: ~ 1.4 / 10
Link: https://open.kattis.com/problems/detaileddifferences
Complexity: O(N) for N characters
Memory: O(1)
*/


import java.util.*;

public class detaileddifferences {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int numTests = in.nextInt();
    in.nextLine();
    for (int i = 0; i < numTests; i++) {
      String s1 = in.nextLine();
      String s2 = in.nextLine();
      String output = "";
      // compare character by character
      for (int j = 0; j < s1.length(); j++) {
        if (s1.charAt(j) == s2.charAt(j)) {
          output += ".";
        }
        else {
          output += "*";
        }
      }
      // Note: the performance of this could be vastly improved by using
      // a StringBuilder due to string concatenation in Java
      System.out.println(s1);
      System.out.println(s2);
      System.out.println(output);
      System.out.println();
    }
  }
}
