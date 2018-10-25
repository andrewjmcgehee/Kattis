/*
Rating: ~ 3.6 / 10
Link: https://open.kattis.com/problems/pathtracing
Complexity: O(NK) for N rows and K cols
MemorY: O(NK) for N rows and K cols
*/
import java.util.*;

public class pathtracing {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int maxPosX = 0;
    int minNegX = 0;
    int maxPosY = 0;
    int minNegY = 0;
    int x = 0;
    int y = 0;

    ArrayList<Character> steps = new ArrayList<Character>();
    while (in.hasNext()) {
      char command = in.next().charAt(0);
      steps.add(command);

      // keep track of the extrema
      switch (command) {
        case 'u':
          y++;
          maxPosY = Math.max(maxPosY, y);
          break;
        case 'r':
          x++;
          maxPosX = Math.max(maxPosX, x);
          break;
        case 'd':
          y--;
          minNegY = Math.min(minNegY, y);
          break;
        case 'l':
          x--;
          minNegX = Math.min(minNegX, x);
          break;
      }
    }

    // create map with specified bounds
    int rowRange = maxPosY + Math.abs(minNegY) + 1;
    int colRange = maxPosX + Math.abs(minNegX) + 1;
    char[][] map = new char[rowRange][colRange];
    int row = maxPosY;
    int col = Math.abs(minNegX);
    // start point
    map[row][col] = 'S';

    // navigate the defined path
    for (int i = 0; i < steps.size(); i++) {
      char c = steps.get(i);
      switch (c) {
        case 'u':
          row--;
          break;
        case 'r':
          col++;
          break;
        case 'd':
          row++;
          break;
        case 'l':
          col--;
          break;
      }
      // at end
      if (i == steps.size() - 1) {
        map[row][col] = 'E';
      }
      // don't overwrite start
      else if (map[row][col] != 'S') {
        map[row][col] = '*';
      }
    }
    // initial upper border
    for (int i = 0; i < colRange + 2; i++) {
      System.out.print("#");
    }
    System.out.print("\n");

    // interior cells
    for (int i = 0; i < rowRange; i++) {
      System.out.print("#");
      for (int j = 0; j < colRange; j++) {
        char c = map[i][j];
        if (c == 'S' || c == 'E' || c == '*') {
          System.out.print(c);
        }
        else {
          System.out.print(" ");
        }
      }
      System.out.print("#\n");
    }

    // lower border
    for (int i = 0; i < colRange + 2; i++) {
      System.out.print("#");
    }
    System.out.print("\n");
  }
}
