/*
Rating: ~ 1.9 / 10
Link: https://open.kattis.com/problems/babelfish
Complexity: O(N) where N is number of words to be translated
Memory: O(N) where N is number of translations
*/

import java.util.*;
import java.io.*;

public class babelfish {
  // faster I/O - honestly unnecessary
  static class Reader {
    BufferedReader br;
    StringTokenizer st;

    public Reader() {
      br = new BufferedReader(new InputStreamReader(System.in));
    }

    String nextLine() {
      String s = null;
      try {
        s = br.readLine();
      }
      catch (IOException e) {
        return s;
      }
      return s;
    }
  }

  public static void main(String[] args) {
    Reader in = new Reader();
    String[] arr = in.nextLine().split(" ");
    String s;
    HashMap<String, String> map = new HashMap<String, String>();

    // map pig latin to translation
    while (arr.length != 1) {
      map.put(arr[1], arr[0]);
      arr = in.nextLine().split(" ");
    }

    s = in.nextLine();
    while (s != null) {
      // check if in map
      if (map.containsKey(s)) {
        System.out.println(map.get(s));
      }
      // print eh
      else {
        System.out.println("eh");
      }
      s = in.nextLine();
    }
  }
}
