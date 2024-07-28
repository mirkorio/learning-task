import java.io.*;

public class Department{
	private String name;
	private int id;
	private String dean;

	public Department(){
	}

	public Department(int id,String name, String dean){
		this.name = name;
		this.id = id;
		this.dean = dean;
	}

	public String getName(){
		return name;
	}

	public int getID(){
		return id;
	}

	public String getDean(){
		return dean;
	}

	public void printDept(){
		System.out.println("===========================================");
		System.out.println("Department ID: " + id);
		System.out.println("Department Name: " + name);
		System.out.println("Dean: " + dean);
		System.out.println("===========================================");
	}

	public boolean add(){
		try{
			File file = new File("data/department.txt");
			if(!file.exists()){
				return false;
			}

			FileWriter fileWriter = new FileWriter(file, true);
			BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

			bufferedWriter.write(id + "\t");
			bufferedWriter.write(name + "\t");
			bufferedWriter.write(dean + "\n");
			bufferedWriter.close();

			return true;
		}catch(IOException e){
			System.out.println("Error!");
		}
		return false;
	}

	public static Department get(int searchID){
		Department dept = null;
		try{
			FileReader fileReader = new FileReader("data/department.txt");
			BufferedReader bufferedReader = new BufferedReader(fileReader);

			String line = "";
			while((line = bufferedReader.readLine()) != null){
				String[] data = line.split("\t");
				int id = Integer.parseInt(data[0]);
				if(searchID == id){
					dept = new Department(id, data[1], data[2]);
					break;
				}
			}
			bufferedReader.close();
		}catch(IOException e){
			System.out.println("Error!");
		}

		return dept;
	}

	public static void viewAll(){
		System.out.printf("\n%-10s %-25.20s %-27.20s\n", "Dept ID", "Dept Name", "Dept Dean");
		try{
			FileReader fileReader = new FileReader("data/department.txt");
			BufferedReader bufferedReader = new BufferedReader(fileReader);

			String line = "";
			while((line = bufferedReader.readLine()) != null){
				String[] data = line.split("\t");
				int id = Integer.parseInt(data[0]);
				Department dept = new Department(id, data[1], data[2]);
				dept.printRow();
				System.out.println();
			}
			bufferedReader.close();
		}catch(IOException e){
			System.out.println("Error!");
		}
	}

	public void printRow(){
		System.out.printf("%-10s %-25.20s %-25s", id, name, dean);
	}
}	