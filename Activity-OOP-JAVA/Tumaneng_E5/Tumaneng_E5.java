//MARC CHRISTIAN D. TUMANENG
//BSCS_2A
//CS214
//E5: Price List

import java.util.Scanner;// import Scanner class

public class Tumaneng_E5{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);// create Scanner object

		// Instantiation and Initialization of array
		 int [] itemCode = {113, 208, 222, 264, 268, 281, 362, 368, 375, 430, 656, 803, 818, 983, 993};
		 float[] priceList = {1522, 1971, 1431, 905, 261, 1885, 406, 133, 540, 1652, 506, 1555, 859, 266, 467};
		// Prints all elements of the array
		System.out.println("\nItem Code" + "  " + "Price List\n");
		for (int i = 0, j = 0; i<itemCode.length && j<priceList.length; i++, j++){
		 		System.out. printf(itemCode[i] +"         "+"Php "+"%,.2f\n",priceList[j]);					  		
		}
		// Ask for the user's chosen Item code
		System.out.print("\nEnter Item Code: ");
		int givenCode = input.nextInt();
		//check the chosen/input item code if it is present in the array itemCode
		boolean present = false;
		int index = -1;

		for(int n:itemCode){
			if(n == givenCode){
				present = true;
				break;
				}
			}
		//find or identifies the index of the selected item code of user
		for (int i = 0; (i < itemCode.length) && (index == -1); i++){
        if (itemCode[i] == givenCode){
            index = i;
        		}
   			}
   		/*if the selected item code of user is present or valid, display the message, “Item is available.” 
   			and print its price.if the item code is invalid, display “Item not found.”*/
   		if(present){
			System.out.println("\nItem is available.");
			System.out.printf("The price of Item Code "+itemCode[index]+" is Php "+"%,.2f",priceList[index]);
		}else
			System.out.println("\nItem not found.");		
	}			
}