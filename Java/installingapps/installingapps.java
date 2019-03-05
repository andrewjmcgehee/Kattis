/*
Rating: ~ 6.7 / 10
Link: https://open.kattis.com/problems/installingapps
Complexity: O(NK) for N apps and K sizes
Memory: O(NK) for N apps and K sizes
*/

import java.io.*;
import java.util.*;

class App implements Comparable<App> {
  int index;
  // download size
  int download;
  // storage size
  int storage;
  // max of download and storage
  int size;

  public App(int index, int download, int storage) {
    this.index = index;
    this.download = download;
    this.storage = storage;
    this.size = (download > storage) ? download : storage;
  }

  // comparator to sort by difference of storage and download size
  // can be imagined as a vector which represents how the app
  // "changes" once installed
  @Override
  public int compareTo(App o) {
    if (storage - download > o.storage - o.download) return -1;
    else if (storage - download == o.storage - o.download) return 0;
    return 1;
  }
}

public class installingapps {
  // could be made faster with buffered reader
  static Scanner in = new Scanner(System.in);

  public static void main(String[] args) {
    // set to these dimensions for ease of indexing
    // access app by index i and size by literal size

    // rows represent using a subset of the first i apps
    // columns represent having a phone with capacity j
    // each cell stores the best possible number of apps installed
    int[][] memo = new int[500][10001];
    boolean[][] used = new boolean[500][10001];

    int N = in.nextInt();
    int C = in.nextInt();
    ArrayList<App> apps = new ArrayList<App>();
    for (int i = 0; i < N; i++) {
      int d = in.nextInt();
      int s = in.nextInt();
      // compensate for 1 indexing for printing later
      apps.add(new App(i+1, d, s));
    }
    Collections.sort(apps);

    // for the first app, we can either include or not include
    // so size i can only hold maximum of 1 app if the phone has
    // >= i megabytes

    // dont include
    for (int i = 0; i < apps.get(0).size; i++) {
      memo[0][i] = 0;
      used[0][i] = false;
    }
    // include
    for (int i = apps.get(0).size; i <= C; i++) {
      memo[0][i] = 1;
      used[0][i] = true;
    }
    // for the next N-1 apps we can either include or not include
    // them, taking the choice which results in more apps installed
    for (int i = 1; i < N; i++) {
      // whatever the new app size is, we can simply copy results
      // from previous row for all phones with smaller capacities
      for (int j = 0; j < apps.get(i).size; j++) {
        memo[i][j] = memo[i-1][j];
        used[i][j] = false;
      }
      // either include the app or dont, whichever is better
      for (int j = apps.get(i).size; j <= C; j++) {
        // include by checking previous row at a size which would
        // allow for installing and adding 1 for the newly added
        // app
        if (memo[i-1][j-apps.get(i).storage] + 1 > memo[i-1][j]) {
          memo[i][j] = memo[i-1][j-apps.get(i).storage] + 1;
          used[i][j] = true;
        }
        // dont include and copy previous row
        else {
          memo[i][j] = memo[i-1][j];
          used[i][j] = false;
        }
      }
    }
    // result will be stored here
    System.out.printf("%d\n", memo[N-1][C]);
    // no apps could be installed
    if (memo[N-1][C] == 0) return;
    for (int i = N-1; i > -1; i--) {
      if (used[i][C]) {
        // subtract the storage of the app
        System.out.printf("%d ", apps.get(i).index);
        C -= apps.get(i).storage;
      }
    }
    System.out.printf("\n");
  }
}

