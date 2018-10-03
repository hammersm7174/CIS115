// CIS 115
// M1LAB
// Name and age conversation
// Plan:
// Ask user Name
// Say it back
// Ask age
// Add 1 to it
// Say next age
// Done

//add imports
import java.util.Scanner; // for input

class Main {
  public static void main(String[] args) {
      Scanner s = new Scanner ( System.in);
      System.out.print("Enter your name: ");
      String name=s.next();
      System.out.println("Hello: " + name);
      System.out.print("Enter your age: ");
      int age.s.nextInt();
      int sum = age + 1;
      System.out.println("Your age next year will be " + sum);
  }
}