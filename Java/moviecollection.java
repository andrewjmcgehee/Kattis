/*
Rating: ~ 5.7 / 10
Link: https://open.kattis.com/problems/moviecollection
Complexity: O(K log(N)) for K queries to the fenwick tree
Memory: O(N) for N movies
*/

import java.util.*;
import java.io.*;

public class moviecollection {
  // fenwick tree to support efficient range updates
  static void update(int[] fenwickTree, int i, int val) {
    if (i >= fenwickTree.length) {
      return;
    }
    fenwickTree[i] += val;
    // gets children by adding least significant bit
    i += (-i & i);
    update(fenwickTree, i, val);
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    for (int t = 0; t < n; t++) {
      int m = in.nextInt();
      int r = in.nextInt();

      int[] movies = new int[m+1];
      int[] fenwickTree = new int[500000];

      // fenwickTree keeps track of number of movies above a given movie
      for (int i = 1; i <= m; i++) {
        update(fenwickTree, i, 1);
        movies[i] = m - i + 1;
      }

      int count = m;
      ArrayList<Integer> queries = new ArrayList<Integer>();
      for (int i = 0; i < r; i++) {
        queries.add(in.nextInt());
      }
      for (Integer i : queries) {
        count++;
        int total = 0;
        int index = movies[i];

        // traverse the fenwickTree adding the totals
        while (index > 0) {
          total += fenwickTree[index];
          index -= (-index & index);
        }

        // update movies in that range
        update(fenwickTree, movies[i], -1);
        movies[i] = count;
        update(fenwickTree, movies[i], 1);
        System.out.print(m - total + " ");
      }
      System.out.println();
    }
  }
}
