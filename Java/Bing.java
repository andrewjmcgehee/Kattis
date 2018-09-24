/*
Rating: ~ 3.9 / 10
Link: https://open.kattis.com/problems/bing
Complexity: O(N) for N total nodes in Trie
Memory: O(N) for N nodes
*/

import java.util.*;
import java.io.*;

public class Bing {
  // modified class to implement Trie that tracks frequency of each node
  static class TrieNode {
    char c;
    int freq;
    TrieNode[] children = new TrieNode[26];

    public TrieNode(char c, int freq) {
      this.c = c;
      this.freq = freq;
    }
  }

  public static void main(String[] args) throws IOException {
    // fastor I/O
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    // root node with a char not in the input char set
    TrieNode root = new TrieNode('A', 0);

    for (int i = 0; i < n; i++) {
      String word = br.readLine();
      TrieNode current = root;
      // add each word to Trie
      for (int j = 0; j < word.length(); j++) {
        char tmp = word.charAt(j);
        int index = tmp - 'a';
        if (current.children[index] != null) {
          current = current.children[index];
          current.freq++;
        }
        else {
          TrieNode child = new TrieNode(tmp, 0);
          current.children[index] = child;
          current = child;
        }
      }
      // current will point to the end of the current word
      System.out.println(current.freq);
    }
  }
}
