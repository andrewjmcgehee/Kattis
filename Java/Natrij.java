/*
Rating: ~ 2.7 / 10
Link: https://open.kattis.com/problems/natrij
Complexity: O(1)
Memory: O(1)
*/

import java.util.*;
import java.text.DecimalFormat;

public class Natrij {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    DecimalFormat df = new DecimalFormat("00");
    String[] now = in.nextLine().split(":");
    String[] then = in.nextLine().split(":");

    int nowHour = Integer.parseInt(now[0]);
    int nowMin = Integer.parseInt(now[1]);
    int nowSec = Integer.parseInt(now[2]);

    int thenHour = Integer.parseInt(then[0]);
    int thenMin = Integer.parseInt(then[1]);
    int thenSec = Integer.parseInt(then[2]);

    // get deltas
    int sec = thenSec - nowSec;
    int min = thenMin - nowMin;
    int hour = thenHour - nowHour;

    // borrow seconds from a minute
    if (sec < 0) {
      sec += 60;
      min -= 1;
    }
    // borrow minutes from an hour
    if (min < 0) {
      min += 60;
      hour -= 1;
    }
    // borrow hours from a day
    if (hour < 0) {
      hour += 24;
    }
    // a full day has passed
    if (hour == 0 && min == 0 && sec == 0) {
      hour = 24;
    }
    String output = df.format(hour) + ":" + df.format(min);
    output += ":" + df.format(sec);
    System.out.println(output);
  }
}
