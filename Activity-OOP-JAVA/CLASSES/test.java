import java.io.*;
//import java.io.file;
//import java.io.fileNotFoundException;
import java.util.Scanner;


public class test{
	public static void OpenFile(String myFile)throws IOException{
		File myObj = new File(myFile);
		try{
			/*Scanner myReader = new Scanner(myObj);
			System.out.println("==== File Content =====");
			while (myReader.hasNextLine()){
				String data=myReader.nextLine();
				System.out.print(data);
			}*/
			BufferedReader myReader = new BufferedReader(new FileReader(myObj));
			String data;
			System.out.println("==== File Content =====");
			while((data = myReader. readLine()) != null){
				System.out.println(data);
			}
			System.out.println("==== File Info =====");
			if(myObj.exists()){
				System.out.println("file name: "+myObj.getName());
				System.out.println("Absolute path: "+myObj.getAbsolutePath());
				System.out.println("Writable:"+ myObj.canWrite());
				System.out.println("Readable:"+ myObj.canRead());
				System.out.println("File Size in Byte:"+ myObj.length());
			}
		}
		catch (FileNotFoundException e){
			System.out.print("File not Found");
		}
	}
	public static void main(String[]args)throws IOException{
		Scanner sc= new Scanner(System.in);
		System.out.print("what File you want to Open?");
		String myFile=sc.next();
		OpenFile(myFile);
	}
}