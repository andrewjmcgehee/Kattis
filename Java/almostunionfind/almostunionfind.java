/*
Rating: ~ 7.1 / 10
Link: https://open.kattis.com/problems/almostunionfind
Complexity: O(N log N) for union find
Memory: O(N) for N nodes
*/

import java.util.*;
import java.io.*;

public class almostunionfind {

  // faster I/O
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) {
    try {
      while (true) {
        String[] line = br.readLine().split(" ");
        int n = Integer.valueOf(line[0]);
        int m = Integer.valueOf(line[1]);

        // union find array of Nodes
        Node[] nodes = new Node[n+1];
        for (int i = 1; i <= n; i++) {
          nodes[i] = new Node(i);
        }
        // get commands
        for (int i = 0; i < m; i++) {
          line = br.readLine().split(" ");
          int command = Integer.valueOf(line[0]);
          int p = Integer.valueOf(line[1]);
          int q;

          // union set with p and set with q
          if (command == 1) {
            q = Integer.valueOf(line[2]);
            nodes[p].union(nodes[q]);
          }
          // move p to set with q
          else if (command == 2) {
            q = Integer.valueOf(line[2]);
            nodes[p] = nodes[p].move(nodes[q]);
          }
          // print size of set containing p and sum of all elements
          else {
            Node root = nodes[p].find();
            System.out.println(root.size + " " + root.sum);
          }
        }
      }
    } catch (Exception e) {}
  }
}

class Node {
  // stores parent, component size, sum of children, and its own value
  Node parent = null;
  long size = 1;
  long sum;
  long value;

  public Node(long val) {
    sum = val;
    value = val;
  }

  // recursively find parent node
  public Node find() {
    if (parent != null) return parent.find();
    return this;
  }

  // move node x to set containing node y
  // not necesarry to actually remove the node from the tree.
  // only need to make the node not effect sum by making its value 0
  // and updating all upstream nodes
  public Node move(Node y) {
    Node xRoot = find();
    Node yRoot = y.find();
    // already in same set
    if (xRoot == yRoot) return this;
    // union brand new node with same value
    Node n = new Node(value);
    n.union(yRoot);
    // update upstream nodes
    subtract(value);
    // make this node useless
    value = 0;
    return n;
  }

  // decrease value of all upstream nodes by a value
  public void subtract(long val) {
    sum -= val;
    size--;
    if (parent != null) parent.subtract(val);
  }

  // union by rank to keep tree somewhat balanced
  public void union(Node y) {
    Node xRoot = find();
    Node yRoot = y.find();
    // already in same set
    if (xRoot == yRoot) return;

    Node n;
    if (xRoot.size < yRoot.size) {
      xRoot.parent = yRoot;
      n = yRoot;
    }
    else {
      yRoot.parent = xRoot;
      n = xRoot;
    }
    // component size is sum of both sub component sizes
    // sum is sum of both sub sums
    n.size = xRoot.size + yRoot.size;
    n.sum = xRoot.sum + yRoot.sum;
  }
}
