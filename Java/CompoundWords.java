/*
Rating: ~ 1.7 / 10
Link: https://open.kattis.com/problems/compoundwords
Complexity: O(N^2) due to pair-wise comparison of N terms
Memory: O(N) for N words
*/

import java.util.*;

public class CompoundWords {
  public static void main(String[] args) {
    Scanner in = new Scanner (System.in);
    // get all words
    ArrayList<String> arr = new ArrayList<String>();
    while (in.hasNext()) {
      arr.add(in.next());
    }
    // tree set stores items in sorted order
    TreeSet<String> compounds = new TreeSet<String>();
    // only consider pair-wise relationships
    for (int i = 0; i < arr.size(); i++) {
      for (int j = i+1; j < arr.size(); j++) {
        String s = arr.get(i) + arr.get(j);
        compounds.add(s);
      }
    }
    // since tree set is sorted, just iterate
    for (String s : compounds) {
      System.out.println(s);
    }
  }
}
