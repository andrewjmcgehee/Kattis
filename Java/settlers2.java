/*
Rating: ~ 4.0 / 10
Link: https://open.kattis.com/problems/settlers2
Complexity: O(N) for N hexagonal board tiles
Memory: O(N) for N board tiles
*/

import java.util.*;
import java.io.*;

public class settlers2 {

  static final int RINGS = 60;
  static int[][] grid = new int[2*RINGS-1][2*RINGS-1];
  static int row = RINGS-1;
  static int col = RINGS-1;
  // contains the order of the resources as visited in the spiral
  static int[] solution = new int[11000];

  // each index stores the count of the material with that number
  static int[] resources = new int[6];

  // movements
  static void NE() {
    row--;
  }
  static void N() {
    row--;
    col--;
  }
  static void NW() {
    col--;
  }
  static void SW() {
    row++;
  }
  static void S() {
    row++;
    col++;
  }
  static void SE() {
    col++;
  }

  // build the hexagonal board
  static void createBoard() {
    int ring = 1;
    int index = 1;
    while (ring < 60) {
      NE();
      int r = getResource(row, col);
      solution[index++] = r;
      // need to go up (ring level - 1) times
      for (int i = 0; i < ring-1; i++) {
        N();
        r = getResource(row, col);
        solution[index++] = r;
      }
      // all other motions happen (ring level) times
      for (int i = 0; i < ring; i++) {
        NW();
        r = getResource(row, col);
        solution[index++] = r;
      }
      for (int i = 0; i < ring; i++) {
        SW();
        r = getResource(row, col);
        solution[index++] = r;
      }
      for (int i = 0; i < ring; i++) {
        S();
        r = getResource(row, col);
        solution[index++] = r;
      }
      for (int i = 0; i < ring; i++) {
        SE();
        r = getResource(row, col);
        solution[index++] = r;
      }
      for (int i = 0; i < ring; i++) {
        NE();
        r = getResource(row, col);
        solution[index++] = r;
      }
      // next ring
      ring += 1;
    }
  }

  // helper function to determine which resources are legal
  static int getResource(int row, int col) {
    HashSet<Integer> neighbors = new HashSet<Integer>();

    // bounds checking - should probably be cleaned up and put
    // in a helper method
    neighbors.add(grid[row][col]);
    if (row > 0) {
      neighbors.add(grid[row-1][col]);
      if (col > 0) {
        neighbors.add(grid[row-1][col-1]);
      }
    }
    if (col > 0) {
      neighbors.add(grid[row][col-1]);
    }
    if (row < grid.length - 2) {
      neighbors.add(grid[row+1][col]);
      if (col < grid.length - 2) {
        neighbors.add(grid[row+1][col+1]);
      }
    }
    if (col < grid.length - 2) {
      neighbors.add(grid[row][col+1]);
    }

    // get legal resources
    ArrayList<Integer> choices = new ArrayList<Integer>();
    for (int i = 1; i <= 5; i++) {
      if (!neighbors.contains(i)) {
        choices.add(i);
      }
    }

    // if only one choice allowed
    if (choices.size() == 1) {
      int r = choices.get(0);
      grid[row][col] = r;
      resources[r]++;
      return r;
    }
    else {
      int r = choices.get(0);
      // get least used resource
      for (Integer i : choices) {
        if (resources[i] < resources[r]) {
          r = i;
        }
      }
      grid[row][col] = r;
      resources[r]++;
      return r;
    }
  }

  public static void main(String[] args) throws IOException {
    // fast I/O
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // initialize grid with starting resource
    grid[row][col] = 1;
    solution[0] = 1;
    resources[1]++;
    createBoard();
    int numCases = Integer.parseInt(br.readLine());
    for (int t = 0; t < numCases; t++) {
      int n = Integer.parseInt(br.readLine());
      // compensate for 0 indexing
      System.out.println(solution[n-1]);
    }
  }
}
