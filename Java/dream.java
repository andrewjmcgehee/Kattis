/*
Rating: ~ 5.9 / 10
Link: https://open.kattis.com/problems/dream
Complexity: O(N) where N is number of events in given query
Memory: O(N) where N is number of events
*/

import java.util.*;
import java.io.*;

public class dream {
  public static void main(String[] args) throws IOException {
    // I / O Optimization for Java
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());

    // Using array similarly to a stack by simply tracking an index
    String[] table = new String[50001];
    HashMap<String, Integer> map = new HashMap<String, Integer>();
    int index = 0;

    for (int i = 0; i < n; i++) {
      String[] line = br.readLine().split(" ");
      String type = line[0];
      // Get the event put it in the table and the map
      if (type.equals("E")) {
        String e = line[1];
        table[index] = e;
        map.put(e, index++);
      }
      // Pop items off of pseudo stack
      else if (type.equals("D")) {
        int range = Integer.parseInt(line[1]);
        for (int j = 0; j < range; j++) {
          index--;
          map.remove(table[index]);
        }
      }
      // Query if plot flaws exist
      else {
        int range = Integer.parseInt(line[1]);
        int dreamIndex = index;
        int realIndex = -1;
        // Tracks if plot flaw exists
        boolean error = false;

        for (int j = 0; j < range; j++) {
          // Events to check begin at index 2
          String s = line[2+j];
          if (s.charAt(0) == '!') {
            s = s.substring(1);
            if (map.containsKey(s) && map.get(s) < dreamIndex) {
              dreamIndex = map.get(s);
            }
          }
          else {
            if (!map.containsKey(s)) {
              error = true;
              break;
            }
            else {
              if (realIndex < map.get(s)) {
                realIndex = map.get(s);
              }
            }
          }
        }
        if (!error && dreamIndex == index) {
          System.out.println("Yes");
        }
        else if (dreamIndex <= realIndex || error) {
          System.out.println("Plot Error");
        }
        else {
          System.out.println((index - dreamIndex) + " Just A Dream");
        }
      }
    }
  }
}
