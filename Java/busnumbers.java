/*
Rating: ~ 2.6 / 10
Link: https://open.kattis.com/problems/busnumbers
Complexity: O(N) where N is range of lowest stop to highest
Memory: O(N) where N is max number of stops
*/

import java.util.*;

public class busnumbers {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    // visited array for bus stops
    boolean[] nums = new boolean[1001];
    for (int i = 0; i < n; i++) {
      int k = in.nextInt();
      nums[k] = true;
    }
    String output = "";
    int lo = -1;
    int hi = -1;
    int numStops = 0;
    for (int i = 0; i < 1001; i++) {
      // beginning of possible stop "range"
      if (nums[i]) {
        lo = i;
        while (i < nums.length && nums[i]) {
          hi = i;
          i++;
          numStops++;
        }
        // only have a range if 3 or more numbers are included
        if (numStops > 2) {
          output += Integer.toString(lo) + "-";
          output += Integer.toString(hi) + " ";
        }
        else if (numStops == 2) {
          output += Integer.toString(lo) + " ";
          output += Integer.toString(hi) + " ";
        }
        else {
          output += Integer.toString(lo) + " ";
        }
        numStops = 0;
      }
    }
    System.out.println(output);
  }
}
