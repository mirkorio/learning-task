import java.io.*;

public class Student{
	private int id;
	private String name;
	private String address;
	private Department department;

	public Student(){
	}

	public Student(int id, String name, String address, Department department){
		this.id = id;
		this.name = name;
		this.address = address;
		this.department = department;
	}

	public int getId(){
		return id;
	}
	public String getName(){
		return name;
	}
	public String getAddress(){
		return address;
	}
	public Department getDepartment(){
		return department;
	}

	public void setId(int id){
		this.id = id;
	}
	public void setName(String name){
		this.name = name;
	}
	public void setAddress(String address){
		this.address = address;
	}
	public void setDepartment(Department department){
		this.department = department;
	}

	public void print(){
		System.out.println("Student ID: " + id);
		System.out.println("Student Name: " + name);
		System.out.println("Student Address: " + address);
		department.print();
	}

	public boolean add(){
		try{
			File file = new File("data/student.txt");
			if(!file.exists()){
				return false;
			}

			FileWriter fileWriter = new FileWriter(file, true);
			BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

			bufferedWriter.write(id + "\t");
			bufferedWriter.write(name + "\t");
			bufferedWriter.write(address + "\t");
			bufferedWriter.write(department.getId() + "\n");
			bufferedWriter.close();

			return true;
		}catch(IOException e){
			System.out.println("Error!");
		}
		return false;
	}

	public static Student get(int searchID){
		Student student = null;
		try{
			FileReader fileReader = new FileReader("data/student.txt");
			BufferedReader bufferedReader = new BufferedReader(fileReader);

			String line = "";
			while((line = bufferedReader.readLine()) != null){
				String[] data = line.split("\t");
				int id = Integer.parseInt(data[0]);
				if(searchID == id){
					int deptID = Integer.parseInt(data[3]);
					Department dept = Department.get(deptID);
					student = new Student(id, data[1], data[2], dept);
					break;
				}
			}
			bufferedReader.close();
		}catch(IOException e){
			System.out.println("Error!");
		}

		return student;
	}

	public static void viewAll(){
		System.out.printf("\n%-10s %-25.20s %-25.20s %-10s %-25.20s\n", "Student ID", "Student Name", "Address", "Dept ID", "Dept Name");
		try{
			FileReader fileReader = new FileReader("data/student.txt");
			BufferedReader bufferedReader = new BufferedReader(fileReader);

			String line = "";
			while((line = bufferedReader.readLine()) != null){
				String[] data = line.split("\t");
				int id = Integer.parseInt(data[0]);
				int deptID = Integer.parseInt(data[3]);
				Department dept = Department.get(deptID);
				Student student = new Student(id, data[1], data[2], dept);
				student.printRow();
				System.out.println();
			}
			bufferedReader.close();
		}catch(IOException e){
			System.out.println("Error!");
		}
	}

	public void printRow(){
		System.out.printf("%-10s %-25.20s %-25.20s ", id, name, address);
		department.printRow();
	}
}