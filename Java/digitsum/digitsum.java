/*
Rating: ~ 6.0 / 10
Link: https://open.kattis.com/problems/digitsum
Complexity: O(N + K) where N and K are lengths of strings not including building memo array
Memory: O(1) because the memo array is not dependent on size of N
*/

import java.util.Scanner;

public class digitsum {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int numCases = in.nextInt();

    // create powers of 10 array
    long[] power = new long[16];
    power[0] = 1;
    for (int i = 1; i < 16; i++) {
      power[i] = power[i-1] * 10;
    }

    // create memo array. row represents power of 10 and column represents a
    // digit 1 through 9
    long[][] memo = new long[16][11];
    memo[0][1] = 1;

    // each digit sum is the previous digit sum plus the first value in that
    // row plus (the previous column digit times the power of ten of the row)
    for (int i = 0; i < 16; i++) {
      for (int j = 2; j < 11; j++) {
        memo[i][j] = memo[i][j-1] + memo[i][1] + (j-1) * power[i];
      }

      // for convenience the array contains a column at 10. the sum at this
      // column will always be 9 too large. but this value will be the
      // value of the next row at column 1
      memo[i][10] -= 9;

      // if the power is 15 then we have completely filled the array and
      // dont need to copy the value from column 10 of the previous row
      if (i < 15) {
        memo[i+1][1] = memo[i][10];
      }
    }

    for (int test = 0; test < numCases; test++) {
      long input1 = in.nextLong();
      long input2 = in.nextLong();

      // input1 is decremented by 1 so that its sum is not subtracted from
      // input2 twice
      if (input1 > 0) {
        input1--;
      }

      // convert to string so power of 10 can be compared to length minus 1
      String str1 = Long.toString(input1);
      String str2 = Long.toString(input2);

      long sum1 = 0;
      int index = 0;
      for (int i = str1.length() - 1; i >= 0; i--) {
        // using ascii value of char to get digit value of column in memo
        // array
        int digit = str1.charAt(index++) - '0';
        // i represents length of str minus 1 which equals power of 10
        sum1 += memo[i][digit];
        // add (modulus of current power of ten * current digit)
        sum1 += (long) digit * (input1 % power[i]);
      }

      long sum2 = 0;
      index = 0;
      for (int i = str2.length() - 1; i >= 0; i--) {
        int digit = str2.charAt(index++) - '0';
        sum2 += memo[i][digit];
        sum2 += (long) digit * (input2 % power[i]);
      }
      System.out.println(sum2 - sum1);
    }
  }
}
