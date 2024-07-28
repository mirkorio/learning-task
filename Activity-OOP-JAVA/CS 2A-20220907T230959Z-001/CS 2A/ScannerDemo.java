import java.util.Scanner;

public class ScannerDemo{
	public static void main (String[] args){
		// <ClassName> <objName> = new <ClassName>();
		Scanner input = new Scanner (System.in);

		System.out.print("Enter a number: ");				   // int = <objName>.nextDatatype();
		int number = input.nextInt();

		System.out.print("Enter a floating point: ");
		double floating = input.nextDouble();                  // float = <objName>.nextDatatype(); 

		System.out.print("Enter a boolean: ");
		boolean result = input.nextBoolean();				   // boolean = <objName>.nextDatatype(); 

		System.out.print("Enter a letter: ");				   // character = <objName>.next().charAt(0);
		char letter = input.next().charAt(0);

		System.out.print("Enter a word: "); 				   // String = input.next();  
		String word = input.next();

		System.out.print("Enter a text: "); 				   // String = input.nextln();  
		input.nextLine();                                      // obtain "enter"
		String text = input.nextLine();



		System.out.println("\nNumber = " + number);
		System.out.println("Floating point = " + floating);
		System.out.println("Boolean = " + result);
		System.out.println("Letter = " + letter);
		System.out.println("Word = " + word);
		System.out.println("Text = " + text);

	}
}