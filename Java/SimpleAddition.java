/*
Rating: ~ 2.2 / 10
Link: https://open.kattis.com/problems/simpleaddition
Complexity: O(N) for N characters in big int
Memory: O(N) for N characters in big int
*/

import java.util.*;
import java.io.*;

public class simpleaddition {
  public static void main(String[] args) throws IOException {
    // fast I/O
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String x = br.readLine().trim();
    String y = br.readLine().trim();

    // get longer and shorter string
    String big = (x.length() > y.length()) ? x : y;
    String small = (x.length() <= y.length()) ? x : y;

    // track the carry if two numbers greater than 10
    int carry = 0;
    // using string concatenation but could be faster with StringBuilder
    String sum = "";
    // iterate through shorter numbers digits
    for (int i = 1; i <= small.length(); i++) {
      int a = small.charAt(small.length() - i) - '0';
      int b = big.charAt(big.length() - i) - '0';

      // sum of two digits and carry
      int c = a + b + carry;
      carry = c / 10;

      // 48 is ascii for '0'
      char digit = (char) (c % 10 + 48);
      sum = digit + sum;
    }

    // process remaining numbers in bigger number, if any
    int index = big.length() - small.length() - 1;
    while (index != -1) {
      int a = big.charAt(index) - '0';
      int b = carry + a;
      carry = b / 10;
      char digit = (char) (b % 10 + 48);
      sum = digit + sum;
      index--;
    }
    // process final carry, if one
    if (carry != 0) {
      sum = '1' + sum;
    }
    System.out.println(sum);
  }
}
