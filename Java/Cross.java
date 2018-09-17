/*
Rating: ~ 3.6 / 10
Link: https://open.kattis.com/problems/cross
Complexity: O(N^4) due to an N^2 search for maximally N^2 spaces (N = 9 so this is acceptable)
Memory: O(N^2) where N = 9 spaces
*/

import java.util.*;

public class Cross {
  static class Square {
    int row;
    int col;

    public Square(int row, int col) {
      this.row = row;
      this.col = col;
    }
  }

  public static Square hatch(int[][] board, int target) {
    // sudoku board can be conceptualized as 9 rows, 9 cols, which comprise  9 3x3 squares
    HashSet<Integer> rows = new HashSet<Integer>();
    HashSet<Integer> cols = new HashSet<Integer>();
    HashSet<Integer> squares = new HashSet<Integer>();

    for (int i = 0; i < 9; i++) {
      rows.add(i);
      cols.add(i);
      squares.add(i);
    }

    // complete search of space
    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        // remove row and col and remove square by using row-major calculations
        if (board[i][j] == target) {
          rows.remove(i);
          cols.remove(j);
          squares.remove(3*(i / 3) + j / 3);
        }
      }
    }

    // if there is no row, there is also no column and no square, and vice versa
    if (rows.isEmpty() || cols.isEmpty()) {
      return null;
    }
    // check each space in each remaining square
    for (Integer s : squares) {
      ArrayList<Integer> squareRows = new ArrayList<Integer>();
      ArrayList<Integer> squareCols = new ArrayList<Integer>();
      ArrayList<Square> possible = new ArrayList<Square>();
      for (int i = 0; i < 3; i++) {
        // more row-major maths
        int sRow = 3*(s / 3) + i;
        int sCol = 3*(s % 3) + i;
        if (rows.contains(sRow)) {
          squareRows.add(sRow);
        }
        if (cols.contains(sCol)) {
          squareCols.add(sCol);
        }
      }
      // if no square row or square column exists, we've found an error
      if (squareRows.isEmpty() || squareCols.isEmpty()) {
        return new Square(-1, -1);
      }
      // add all possible spaces in the square
      for (Integer row : squareRows) {
        for (Integer col : squareCols) {
          if (board[row][col] == -1) {
            possible.add(new Square(row, col));
          }
        }
      }
      // if no spaces in the square are possible, we've found an error
      if (possible.isEmpty()) {
        return new Square(-1, -1);
      }
      // otherwise just return the first possible space
      if (possible.size() == 1) {
        return possible.get(0);
      }
    }
    return null;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int[][] board = new int[9][9];

    // get board
    for (int i = 0; i < 9; i++) {
      String s = in.nextLine();
      for (int j = 0; j < 9; j++) {
        char c = s.charAt(j);
        if (c == '.') {
          board[i][j] = -1;
        }
        else {
          board[i][j] = c - '0';
        }
      }
    }
    boolean done = false;
    boolean error = false;
    // fill in by hatching
    while (!done) {
      done = true;
      // try all 9 targets
      for (int target = 1; target <= 9; target++) {
        Square sq = hatch(board, target);
        // if we got back a square with -1, -1, we found an error
        if (sq != null && sq.row == -1) {
          error = true;
          done = true;
          break;
        }
        // if we got back a square not -1, -1, we found a good space to fill
        if (sq != null) {
          done = false;
          int row = sq.row;
          int col = sq.col;
          board[row][col] = target;
        }
      }
    }

    if (error) {
      System.out.println("ERROR");
    }
    else {
      for (int[] row : board) {
        for (int square : row) {
          if (square == -1) {
            System.out.print('.');
          }
          else {
            System.out.print(square);
          }
        }
        System.out.print('\n');
      }
    }
  }
}


