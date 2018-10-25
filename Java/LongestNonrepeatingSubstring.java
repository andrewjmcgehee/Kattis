/*
Note: This is not a solution to a kattis problem.

This is a solution to the common DP problem for finding
the longest non-repeating substring within a string.
*/

public class logestnonrepeatingsubstring {
  public int longestNonrepeating(String s) {
    int SIZE_OF_ALPHABET = 256;
    int[] lastSeen = new int[SIZE_OF_ALPHABET];

    // initialize all to -1 to indicate not yet seen
    for (int i = 0; i < SIZE_OF_ALPHABET; i++) {
        lastSeen[i] = -1;
    }

    int longest = -1;
    int previous = -1;
    int currentSize = 0;
    for (int i = 0; i < s.length(); i++) {
      previous = lastSeen[s.charAt(i)];
      /*
      * if previous is -1 we have never seen the character so its always safe
      * to increment size, if i (our current location) minus the current size
      * of our subsequence is strictly greater than the index of the previous
      * occurence, then we know that the previous occurence isn't in the current
      * subsequence and we can also safely incremement the size
      */
      if (previous == -1 || i - currentSize > previous) {
          currentSize++;
      }
      else {
          /*
          * the new size of the current subsequence is i (our current location)
          * minus the previous occurence of the character. this is the same as
          * setting the start point of the subsequence to the index directly
          * after the previous occurence
          */
          longest = Math.max(longest, currentSize);
          currentSize = i - previous;
      }
      // track the last occurence of a given char
      lastSeen[s.charAt(i)] = i;
    }
    longest = Math.max(longest, currentSize);
    return longest;
  }
}
