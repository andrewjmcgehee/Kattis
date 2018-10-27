/*
Rating: ~ 4.0 / 10
Link: https://open.kattis.com/problems/classy
Complexity: O(N log(N)) due to sorting N people
Memory: O(N) where N is number of people
*/

import java.util.*;

public class classy {
  // to complete this problem we must create our own comparable class
  // upper adds a 0, middle adds a 1, and lower adds a 2
  static class Person implements Comparable<Person> {
    String name;
    String rank;
    public Person(String name, String[] rank) {
      char[] temp = new char[10];
      for (int i = 0; i < rank.length; i++) {
        // get first char of each word
        switch(rank[rank.length - i - 1].charAt(0)) {
          case 'u':
            temp[i] = '0';
            break;
          case 'm':
            temp[i] = '1';
            break;
          case 'l':
            temp[i] = '2';
            break;
        }
      }
      // pad remaining spaces with 1's (middle) as it won't change anything
      for (int i = rank.length; i < 10; i++) {
        temp[i] = '1';
      }
      this.name = name;
      this.rank = new String(temp);
    }

    // compare by rank, if rank is equal, compare by name
    public int compareTo(Person other) {
      int comp = this.rank.compareTo(other.rank);
      return (comp == 0) ? this.name.compareTo(other.name) : comp;
    }
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int numCase = in.nextInt();
    for (int i = 0; i < numCase; i++) {
      int numPeople = in.nextInt();
      in.nextLine();
      Person[] people = new Person[numPeople];
      for (int j = 0; j < numPeople; j++) {
        String name = in.next();
        // get rid of : character
        name = name.substring(0, name.length() - 1);
        people[j] = new Person(name, in.next().split("-"));
        in.nextLine();
      }

      // since we have a comparable class, we can sort
      Arrays.sort(people);
      for (Person p : people) {
        System.out.println(p.name);
      }
      System.out.println("==============================");
    }
  }
}
