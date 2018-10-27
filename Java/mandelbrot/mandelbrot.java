/*
Rating: ~ 2.9 / 10
Link: https://open.kattis.com/problems/mandelbrot
Complexity: O(N) for N calculations
Memory: O(1)
*/

import java.util.*;

public class mandelbrot {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    // since we are dealing with square roots of negative numbers, we make our own class
    // to represent negative numbers
    class Complex {
      double real;
      double imaginary;

      public Complex() {
        this.real = 0;
        this.imaginary = 0;
      }

      public Complex(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
      }

      double modulus() {
        return Math.sqrt(real*real + imaginary*imaginary);
      }

      Complex add(Complex other) {
        Complex c = new Complex();
        c.real = real + other.real;
        c.imaginary = imaginary + other.imaginary;
        return c;
      }

      Complex multiply(Complex other) {
        Complex c = new Complex();
        c.real = real * other.real - imaginary * other.imaginary;
        c.imaginary = real * other.imaginary + imaginary * other.real;
        return c;
      }

    }

    for (int test = 1; in.hasNext(); test++) {
      // get the real part and the imaginary part
      Complex constant = new Complex(in.nextDouble(), in.nextDouble());

      // starts at 0 + 0i which is just 0
      Complex current = new Complex();

      int range = in.nextInt();
      boolean divergent = false;
      String output = "Case " + test + ": ";

      for (int i = 0; i < range; i++) {
        // apply the given formula by squaring the current and adding the constant
        current = (current.multiply(current)).add(constant);

        // apply the given modulus formula
        if (current.modulus() > 2) {
          divergent = true;
          break;
        }
      }
      System.out.println(output + (divergent ? "OUT" : "IN"));
    }
  }
}
