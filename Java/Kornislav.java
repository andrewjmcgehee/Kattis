/*
Rating: ~ 1.3 / 10
Link: https://open.kattis.com/problems/kornislav
Complexity: O(N log(N)) for sorting
Memory: O(N)
*/

import java.util.*;

public class Kornislav {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    ArrayList<Integer> arr = new ArrayList<Integer>();
    while (in.hasNext()) {
      arr.add(in.nextInt());
    }
    // sort
    Collections.sort(arr);
    // max possible area is first and third value
    System.out.println(arr.get(0)*arr.get(2));
  }
}
