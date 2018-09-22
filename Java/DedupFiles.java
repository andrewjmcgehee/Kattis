/*
Rating: ~ 4.5 / 10
Link: https://open.kattis.com/problems/deduplicatingfiles
Complexity: O(N^2) where N is number of files due to pair-wise comparison
Memory: O(N) where N is number of files
*/


import java.util.*;
import java.io.*;

public class DedupFiles {
  // hash function as described in problem
  static char getHash(String s) {
    char c = (char) 0;
    for (int i = 0; i < s.length(); i++) {
      c ^= s.charAt(i);
    }
    return c;
  }

  public static void main(String[] args) throws IOException {
    // faster I/O
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    while (true) {
      int n = Integer.parseInt(br.readLine());
      if (n == 0) {
        break;
      }

      // map to count number of occurences of a string
      HashMap<String, Integer> map = new HashMap<String, Integer>();
      for (int i = 0; i < n; i++) {
        String s = br.readLine();

        if (!map.containsKey(s)) {
          map.put(s, 0);
        }
        map.put(s, map.get(s) + 1);
      }

      // consider all pair-wise relationships, including identity pairs
      int collisions = 0;
      for (String f1 : map.keySet()) {
        char h1 = getHash(f1);
        for (String f2 : map.keySet()) {
          if (!f1.equals(f2)) {
            char h2 = getHash(f2);
            if (h1 == h2) {
              // add the product of the numbers as the pair wise
              // collision happens with all duplicates as well
              // (think length * width)
              collisions += map.get(f1)*map.get(f2);
            }
          }
        }
      }
      // collisions can be int divided by 2 because the pairwise
      // relationships can be modeled as an adjacency matrix thats
      // symmetrical all identity pairs collide (the diagonal of the matrix)
      // and if a collides with b then b also collides with a and so far
      // we have counted both of these, but only need 1
      System.out.println(map.size() + " " + collisions / 2);
    }
    br.close();
  }
}
