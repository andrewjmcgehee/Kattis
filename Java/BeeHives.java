/*
Rating: ~ 1.9 / 10
Link: https://open.kattis.com/problems/beehives
Complexity: O(N^2) where N is number of hives
Memory: O(N) where N is number of hives
*/

import java.util.*;

public class BeeHives {
  static class Node {
    double x;
    double y;
    boolean isSour = false;

    public Node(double x, double y) {
      this.x = x;
      this.y = y;
    }

    public double getDistance(Node other) {
      return Math.sqrt(Math.pow((this.x - other.x), 2)
                     + Math.pow((this.y - other.y), 2));
    }
  }
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double d = in.nextDouble();
    int n = in.nextInt();
    while (n != 0) {
      in.nextLine();
      // build nodes
      ArrayList<Node> arr = new ArrayList<Node>();
      for (int i = 0; i < n; i++) {
        double x = in.nextDouble();
        double y = in.nextDouble();
        in.nextLine();

        Node node = new Node(x, y);
        arr.add(node);
      }
      // calculate pair wise distances and set hives to sour
      for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
          Node n1 = arr.get(i);
          Node n2 = arr.get(j);
          double dist = n1.getDistance(n2);
          if (dist <= d) {
            n1.isSour = true;
            n2.isSour = true;
          }
        }
      }
      int numSour = 0;
      int numSweet = 0;
      for (Node node : arr) {
        if (node.isSour) {
          numSour++;
        }
        else {
          numSweet++;
        }
      }
      System.out.println(numSour + " sour, " + numSweet + " sweet");
      d = in.nextDouble();
      n = in.nextInt();
    }
  }
}
