import java.io.*;

public class Department{
	private int id;
	private String name;

	public Department(){
	}

	public Department(int id, String name){
		this.id = id;
		this.name = name;
	}

	public int getId(){
		return id;
	}
	public String getName(){
		return name;
	}

	public void setId(int id){
		this.id = id;
	}
	public void setName(String name){
		this.name = name;
	}

	public void print(){
		System.out.println("Department ID: " + id);
		System.out.println("Department Name: " + name);
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
			bufferedWriter.write(name + "\n");
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
					dept = new Department(id, data[1]);
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
		System.out.printf("\n%-10s %-25.20s\n", "Dept ID", "Dept Name");
		try{
			FileReader fileReader = new FileReader("data/department.txt");
			BufferedReader bufferedReader = new BufferedReader(fileReader);

			String line = "";
			while((line = bufferedReader.readLine()) != null){
				String[] data = line.split("\t");
				int id = Integer.parseInt(data[0]);
				Department dept = new Department(id, data[1]);
				dept.printRow();
				System.out.println();
			}
			bufferedReader.close();
		}catch(IOException e){
			System.out.println("Error!");
		}
	}

	public void printRow(){
		System.out.printf("%-10s %-25.20s", id, name);
	}
}