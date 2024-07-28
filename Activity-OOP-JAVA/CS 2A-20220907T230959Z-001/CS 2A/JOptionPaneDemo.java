// user interface
// string inputs only

import javax.swing.JOptionPane;

public class JOptionPaneDemo{
	public static void main(String[] args){
		String name = JOptionPane.showInputDialog("Enter a name: "); 

		String message = "Hi, " + name + "!";

		JOptionPane.showMessageDialog(null, message);

		String n1 = JOptionPane.showInputDialog("Enter 1st number: ");
		String n2 = JOptionPane.showInputDialog("Enter 2nd number: ");

		int num1 = Integer.parseInt(n1);                                 // parseDataType = change Data type 
		int num2 = Integer.parseInt(n2);

		int sum = num1 + num2;

		JOptionPane.showMessageDialog(null, sum);
	}
}