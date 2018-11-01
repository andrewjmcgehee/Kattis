/*
Rating: ~ 5.0 / 10
Link: https://open.kattis.com/problems/erraticants
Complexity: O(V) for V vertices in graph - also can be expressed as NK for N rows and K cols
Memory: O(V) for V vertices in graph - also can be expressed as NK for N rows and K cols
*/

import java.io.*;
import java.util.*;

public class erraticants {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  // can only move maximum 60 moves in either direction
  static final int MAX_MOVES = 121;
  static final int START = MAX_MOVES / 2;
  // in the final dimension, 0 denotes N, 1 denotes S, 2 denotes E, 3 denotes W
  static boolean[][][] edges = new boolean[MAX_MOVES][MAX_MOVES][4];
  // 2D visited array
  static boolean[][] visited = new boolean[MAX_MOVES][MAX_MOVES];

  public static int bfs(int row0, int col0, int rowF, int colF) {
    // basically java way of keeping queue of tuples
    Queue<Integer> rowQ = new LinkedList<Integer>();
    Queue<Integer> colQ = new LinkedList<Integer>();
    // put on initial items
    rowQ.offer(row0);
    colQ.offer(col0);
    // sentinel value for tracking depth of BFS
    rowQ.offer(null);

    int depth = 0;
    while (true) {
      // if we hit a null, we have processed all values of a certain level
      if (rowQ.peek() == null) {
        rowQ.offer(rowQ.poll());
        depth++;
      }
      else {
        // get next items
        int row = rowQ.poll();
        int col = colQ.poll();
        // found the target
        if (row == rowF && col == colF) return depth;
        // try all four directions
        for (int dir = 0; dir < 4; dir++) {
          // check edge existence
          if (edges[row][col][dir]) {
            // get change in row and col
            int nextRow = row + getRow(dir);
            int nextCol = col + getCol(dir);
            // check visited
            if (!visited[nextRow][nextCol]) {
              rowQ.offer(nextRow);
              colQ.offer(nextCol);
              // visiting here is smart, but can be done other places too
              visited[nextRow][nextCol] = true;
            }
          }
        }
      }
    }
  }

  // helper for returning change in row based on numeric direction
  public static int getRow(int direction) {
    if (direction == 0) return -1;
    if (direction == 1) return 1;
    return 0;
  }

  // helper for returning change in col based on numeric direction
  public static int getCol(int direction) {
    if (direction == 2) return 1;
    if (direction == 3) return -1;
    return 0;
  }

  // reset visited and edge arrays
  public static void clear() {
    for (int i = 0; i < MAX_MOVES; i++) {
      Arrays.fill(visited[i], false);
      for (int j = 0; j < MAX_MOVES; j++) {
        Arrays.fill(edges[i][j], false);
      }
    }
  }

  public static void main(String[] args) throws IOException {
    int t = Integer.parseInt(br.readLine());
    for (int test = 0; test < t; test++) {
      // white space
      br.readLine();
      // num moves
      int moves = Integer.parseInt(br.readLine());
      int row = START;
      int col = START;
      clear();
      for (int i = 0; i < moves; i++) {
        char dir = br.readLine().charAt(0);
        switch (dir) {
          // we can N from here and S from there
          case 'N':
            edges[row][col][0] = true;
            edges[row-1][col][1] = true;
            row--;
            break;
          // we can S from here and N from there
          case 'S':
            edges[row][col][1] = true;
            edges[row+1][col][0] = true;
            row++;
            break;
          // we can E from here and W from there
          case 'E':
            edges[row][col][2] = true;
            edges[row][col+1][3] = true;
            col++;
            break;
          // we can W from here and E from there
          case 'W':
            edges[row][col][3] = true;
            edges[row][col-1][2] = true;
            col--;
            break;
        }
      }
      // do bfs
      System.out.println(bfs(START, START, row, col));
    }
  }
}
