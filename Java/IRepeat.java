/*
Rating: ~ 2.3 / 10
Link: https://open.kattis.com/problems/irepeatmyself
Complexity: O(N^2) where N is the size of the input string
Memory: O(N / K) where N is the size of the input string and K is the division size
*/

import java.util.*;

public class IRepeat {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int numCases = in.nextInt();
    in.nextLine();

    for (int i = 0; i < numCases; i++) {
      String s = in.nextLine();
      String prefix = "";

      for (int j = 0; j < s.length(); j++) {
        // try each prefix
        char c = s.charAt(j);
        prefix += c;
        int division = prefix.length();

        // get all the sub strings that are the same length as the prefix
        // by int dividing, we avoid getting the tail end
        HashSet<String> parts = new HashSet<String>();
        for (int k = 0; k < s.length() / division; k++) {
          String sub = s.substring(k*division, (k+1)*division);
          parts.add(sub);
        }

        // mod is the index the tail begins on
        int mod = s.length() % prefix.length();
        String tail = s.substring(s.length() - mod);

        // parts can't hold duplicates so if their are any unique values
        // other than just a single value, our prefix size is too small
        // also note, the prefix must start with the tail
        if (parts.size() == 1 && prefix.startsWith(tail)) {
          System.out.println(division);
          break;
        }
      }
    }
  }
}
