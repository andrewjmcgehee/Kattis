/*
Rating: ~ 3.2 / 10
Link: https://open.kattis.com/problems/froshweek2
Complexity: O(N log(N) + M log(M)) due to sorting and where N and M are array sizes
Memory: O(N + M) where N and M are array sizes
*/

import java.util.*;

public class Frosh2 {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int m = in.nextInt();
    ArrayList<Integer> tasks = new ArrayList<Integer>();
    ArrayList<Integer> times = new ArrayList<Integer>();

    // create arrays
    for (int i = 0; i < n; i++) {
      tasks.add(in.nextInt());
    }
    for (int i = 0; i < m; i++) {
      times.add(in.nextInt());
    }

    // sort them
    Collections.sort(tasks);
    Collections.sort(times);

    int i = 0;
    int j = 0;
    int numComplete = 0;
    while (i < tasks.size() && j < times.size()) {
      int task = tasks.get(i);
      int time = times.get(j);

      // if we have enough time, we can complete only 1 task
      // get next task and next time
      if (task <= time) {
        numComplete++;
        i++;
        j++;
      }
      // otherwise we need more time
      // get next time but try same task
      else {
        j++;
      }
    }
    System.out.println(numComplete);
  }
}
