/*
Rating: ~ 2.0 / 10
Link: https://open.kattis.com/problems/fbiuniversal
Complexity: O(N) for N characters
Memory: O(1)
*/

import java.util.*;

public class fbiuniversal {
  // number is BASE 27
  static int BASE = 27;
  static HashMap<Character, Integer> toInt = new HashMap<Character, Integer>();
  static HashMap<Integer, Character> toChar = new HashMap<Integer, Character>();

  private static void buildMap() {
    for (int i = 0; i < 10; i++) {
      toInt.put('0' + i, i);
      toChar.put(i, '0' + i);
    }
    // building map is a bit of a pain because of omitted chars
    // char to num
    toInt.put('A', 10);
    toInt.put('C', 11);
    toInt.put('D', 12);
    toInt.put('E', 13);
    toInt.put('F', 14);
    toInt.put('H', 15);
    toInt.put('J', 16);
    toInt.put('K', 17);
    toInt.put('L', 18);
    toInt.put('M', 19);
    toInt.put('N', 20);
    toInt.put('P', 21);
    toInt.put('R', 22);
    toInt.put('T', 23);
    toInt.put('V', 24);
    toInt.put('W', 25);
    toInt.put('X', 26);
    // num to char
    toChar.put(10, 'A');
    toChar.put(11, 'C');
    toChar.put(12, 'D');
    toChar.put(13, 'E');
    toChar.put(14, 'F');
    toChar.put(15, 'H');
    toChar.put(16, 'J');
    toChar.put(17, 'K');
    toChar.put(18, 'L');
    toChar.put(19, 'M');
    toChar.put(20, 'N');
    toChar.put(21, 'P');
    toChar.put(22, 'R');
    toChar.put(23, 'T');
    toChar.put(24, 'V');
    toChar.put(25, 'W');
    toChar.put(26, 'X');
  }

  // check final character as defined in the problem statement
  private static char checkChar(String s) {
    int check = 0;
    check += 2*toInt.get(s.charAt(0));
    check += 4*toInt.get(s.charAt(1));
    check += 5*toInt.get(s.charAt(2));
    check += 7*toInt.get(s.charAt(3));
    check += 8*toInt.get(s.charAt(4));
    check += 10*toInt.get(s.charAt(5));
    check += 11*toInt.get(s.charAt(6));
    check += 13*toInt.get(s.charAt(7));
    check = check % 27;
    char c = toChar.get(check);
    return c;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    buildMap();
    int t = in.nextInt();
    for (int i = 0; i < t; i++) {
      int k = in.nextInt();
      // process as string for ease
      String s = in.next().trim();
      char check = checkChar(s);
      // if check character doesn't work, no extra work needed
      if (check != s.charAt(8)) {
        System.out.println(k + " Invalid");
        continue;
      }

      // 27^8 - 1 is larger than an int
      long num = 0;
      // start at right most - least significant power
      for (int j = 7; j >= 0; j--) {
        Character c = s.charAt(j);
        // number of multiples of 27^j
        int mult = toInt.get(c);
        // cast Math.pow to long - returns double normally
        num += mult * (long) Math.pow(BASE, 7-j);
      }
      System.out.println(k + " " + num);
    }
  }
}
