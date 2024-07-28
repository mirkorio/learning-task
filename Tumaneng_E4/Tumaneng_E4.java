// Tumaneng, Marc Christian D. -BSCS 2A
// CS214
// 09-27-22

import java.util.Scanner;
class Tumaneng_E4{
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);

      System.out.print("\n");  
      System.out.print("Enter 1st number: ");//enter user input for the 1st number
      int num1=scanner.nextInt();
      System.out.print("Enter 1st char: ");//enter user input for 1st character
      char char1=scanner.next().charAt(0);

      System.out.print("Enter 2nd number: ");//enter user input for the 2nd number
      int num2=scanner.nextInt();
      System.out.print("Enter 2nd char: ");//enter user input for 2nd character
      char char2=scanner.next().charAt(0);


      for(int i=1;i<=100;i++) {// for loop to display number 1-100 
         System.out.print(i);
         if(i % num1 == 0) //if-else statement to identify the multiples of 1st number & put the designated charter
            System.out.print(char1);
         else if(i % num2 == 0)//if-else statement to identify the multiples of 2nd number & put the designated charter
            System.out.print(char2);
         System.out.print("\n");           
      }  
   }
}


