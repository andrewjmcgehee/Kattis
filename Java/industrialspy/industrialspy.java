/*
Rating: ~ 3.2 / 10
Link: https://open.kattis.com/problems/industrialspy
Complexity: O(N! + sqrt(K)) where K is maximum number to run sieve on and N is number of digits to permute
Memory: O(PI(K)) where K is maximum number and PI(K) is a function representing number of primes < K
*/

import java.util.*;
import java.io.*;

public class industrialspy {

  static int[] sieve(int n) {
    // approximation for maximum number of primes
    int numPrimes = (int)(1.25506 * n / Math.log(n));
    int[] primes = new int[numPrimes];
    int sqrt = (int) Math.sqrt(n) + 1;
    int index = 0;

    boolean[] isComposite = new boolean[n];
    for (int i = 2; i < sqrt; i ++) {
      if (!isComposite[i]) {
        primes[index++] = i;
        for (int j = i*i; j < n; j += i) {
          isComposite[j] = true;
        }
      }
    }
    for (int i = sqrt; i < n; i += 2) {
      if (!isComposite[i]) {
        primes[index++] = i;
      }
    }
    return Arrays.copyOf(primes, index);
  }

  // faster way to compute permutations as opposed to generating all of them
  // just generate the next one
  private static int[] nextPermutation(int[] arr) {
    int a = getFirst(arr);
    if (a == -1) {
      return null;
    }
    int b = arr.length - 1;
    while (arr[a] >= arr[b]) {
      b--;
    }
    swap(arr, a, b);
    a += 1;
    b = arr.length - 1;
    while (a < b) {
      swap(arr, a++, b--);
    }
    return arr;
  }

  // helper for nextPermutation that gets the location of the first swap
  private static int getFirst(int[] arr) {
    int i = arr.length - 2;
    while (i >= 0) {
      if (arr[i] < arr[i+1]) {
        return i;
      }
      i--;
    }
    return -1;
  }

  // helper for nextPermutation that swaps two digits
  private static void swap(int[] arr, int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
  }

  public static void main(String[] args) throws IOException {
    // fast I/O
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int numCases = Integer.valueOf(br.readLine());
    // get all primes
    int[] primes = sieve(10000000);
    for (int t = 0; t < numCases; t++) {
      HashSet<Integer> visited = new HashSet<Integer>();
      String num = br.readLine();
      // maximally 7 digit number
      int[] digits = new int[8];
      for (int i = 0; i < num.length(); i++) {
        digits[i] = num.charAt(i) - '0';
      }
      // pad the end with -1s
      for (int i = num.length(); i < 8; i++) {
        digits[i] = -1;
      }

      // check primality of each permutation, sorted order is guaranteed smaller permutation
      Arrays.sort(digits);
      int count = 0;
      do {
        int p = 0;
        int multiplier = 1;
        for (int i = 7; i > 0; i--) {
          int digit = digits[i];
          if (digit == -1) {
            break;
          }
          p += digit * multiplier;
          multiplier *= 10;
        }

        if (!visited.contains(p) && Arrays.binarySearch(primes, p) >= 0) {
          visited.add(p);
          count++;
        }
        digits = nextPermutation(digits);
      } while (digits != null);

      System.out.println(count);
    }
  }
}
