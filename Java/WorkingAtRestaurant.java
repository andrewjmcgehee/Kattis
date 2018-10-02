/*
Rating: ~ 5.0 / 10
Link: https://open.kattis.com/problems/restaurant
Complexity: O(K) where K is the number of queries
Memory: O(K) where K is the number of queries
*/

import java.util.*;
import java.io.*;

public class WorkingAtRestaurant {
  public static void main(String[] args) throws IOException {
    // fast I/O
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    while (true) {
      int n = Integer.parseInt(br.readLine());
      if (n == 0) {
        break;
      }

      ArrayDeque<String> commands = new ArrayDeque<String>();
      ArrayDeque<Integer> quantities = new ArrayDeque<Integer>();

      for (int i = 0; i < n; i++) {
        String[] line = br.readLine().split(" ");
        String c = line[0];
        int q = Integer.parseInt(line[1]);
        commands.add(c);
        quantities.add(q);
      }

      int p1 = 0;
      int p2 = 0;

      while (!commands.isEmpty()) {
        String c = commands.remove();
        int q = quantities.remove();

        // always drop plates onto stack 2
        if (c.equals("DROP")) {
          System.out.println("DROP 2 " + q);
          p2 += q;
        }
        else if (c.equals("TAKE")) {
          // if stack 1 has enough plates, take from them
          if (p1 >= q) {
            System.out.println("TAKE 1 " + q);
            p1 -= q;
          }
          else {
            // if stack 1 not empty, empty it first
            if (p1 != 0) {
              System.out.println("TAKE 1 " + p1);
              q -= p1;
              p1 = 0;
            }
            // move all plates from stack 2 to stack 1
            System.out.println("MOVE 2->1 " + p2);
            System.out.println("TAKE 1 " + q);
            p1 = p2 - q;
            p2 = 0;
          }
        }
      }
      System.out.println();
    }
  }
}
