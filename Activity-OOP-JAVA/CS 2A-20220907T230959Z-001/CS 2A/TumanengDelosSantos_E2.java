// Venn P. Delos Santos, Marc Christian Tumaneng 
// BSCS 2-A
// CS 214
// 09/ 6/ 2022


import java.util.Scanner;

public class TumanengDelosSantos_E2{
	public static void main (String[] args){
		// <ClassName> <objName> = new <ClassName>();
		Scanner input = new Scanner (System.in);

		// Functions that ask for user inputs
		System.out.print("Enter Student ID: ");				   
		String studentID = input.nextLine();

		System.out.print("Enter Student Name: "); 				                                        
		String studentName = input.nextLine();

		System.out.print("Enter Age: ");				   
		int age = input.nextInt();

		System.out.print("Enter Gender: ");				   
		char gender = input.next().charAt(0);

		System.out.print("Enter Year Level: ");				   
		int yearLevel = input.nextInt();

		System.out.print("Enter College Degree: "); 				  
		input.nextLine();                                      
		String degree = input.nextLine();

		System.out.print("Enter Amount Paid: ");
		double tuition = input.nextDouble();                  

		System.out.print("Enter GWA: ");
		double gwa = input.nextDouble();                  

		System.out.print("Enter Remark of GWA: ");
		boolean result = input.nextBoolean();				   

		System.out.print("Enter Current Year Enrolled: ");	   
		int schoolYear = input.nextInt();

		//Displays user's inputs
		System.out.println("\nStudent ID: " + studentID);
		System.out.println("Name:  " + studentName);
		System.out.println("Age " + age);
		System.out.println("Gender: " + gender);
		System.out.println("Year Level: " + yearLevel);
		System.out.println("College Degree: " + degree);
		System.out.println("Amount Paid: " + tuition);
		System.out.println("General Weighted Average: " + gwa);
		System.out.println("Remark of GWA: " + result);
		System.out.println("Current Year Enrolled: " + schoolYear);


	}
}