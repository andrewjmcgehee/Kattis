/*
Rating: ~ 2.2 / 10
Link: https://open.kattis.com/problems/whatdoesthefoxsay
Complexity: O(N + K) for N definitions and K words in the sentence
Memory: O(N) for N definitions
*/

import java.util.*;

public class whatdoesthefoxsay {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int numCases = in.nextInt();
    in.nextLine();

    for (int i = 0; i < numCases; i++) {
      String[] arr = in.nextLine().split(" ");
      String info = in.nextLine();
      HashSet<String> sounds = new HashSet<String>();

      // put all defined sounds in a hash set
      while (!info.equalsIgnoreCase("what does the fox say?")) {
        String sound = info.split(" ")[2];
        sounds.add(sound.trim());
        info = in.nextLine();
      }

      // append unknown sounds to output string
      String output = "";
      for (int j = 0; j < arr.length; j++) {
        if (!sounds.contains(arr[j])) {
          output += arr[j];
          output += " ";
        }
      }
      System.out.println(output);
    }
  }
}
