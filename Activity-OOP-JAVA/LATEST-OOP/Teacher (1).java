import java.io.*;

public class Teacher{
	private String name, subject;
	private int id;
	private Department department;
	private Subject subjectName;

	public Teacher(){
	}

	public Teacher(int id, String name, Subject subjectName, Depaertment department){
        this.id = id;
        this.name = name;
        this.subjectName =  subjectName;
        this.department = department;
    }

    public String getName(){
    	return name;
    }

    public Subject getSubjectName(){
    	return getSubjectName;
    }

    public int getId(){
    	return id;
    }

    public department getDepartment(){
    	return department;
    }

    public void printT(){
    	System.out.println("Name: " + name); 
    	System.out.println("Teacher ID: " + id);
        System.out.println("Subject : " + getSubjectName);
        System.out.println("Department : " + department);
        System.out.println();
    }
    public boolean add(){
		try{
			File file = new File("data/Teacher.txt");
			if(!file.exists()){
				return false;
			}

			FileWriter fileWriter = new FileWriter(file, true);
			BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

			bufferedWriter.write(id + "\t");
			bufferedWriter.write(name + "\t");
			bufferedWriter.write(getSubjectName + "\t");
			bufferedWriter.write(department + "\n");
			bufferedWriter.close();

			return true;
		}catch(IOException e){
			System.out.println("Error!");
		}
		return false;
	}

	public static Teacher get(int searchID){
		Teacher d = null;
		try{
			FileReader fileReader = new FileReader("data/Teacher.txt");
			BufferedReader bufferedReader = new BufferedReader(fileReader);

			String line = "";
			while((line = bufferedReader.readLine()) != null){
				String[] data = line.split("\t");
				int id = Integer.parseInt(data[0]);
				if(searchID == id){
					d = new Teacher(id, data[1], data[2], data[3]);
					break;
				}
			}
			bufferedReader.close();
		}catch(IOException e){
			System.out.println("Error!");
		}

		return d;
	}

	public static void viewAll(){
		System.out.printf("\n%-10s %-25.20s %-25.20s %-20s\n", "Teacher ID", "Teacher Name", "Subject", "Department");
		try{
			FileReader fileReader = new FileReader("data/Teacher.txt");
			BufferedReader bufferedReader = new BufferedReader(fileReader);

			String line = "";
			while((line = bufferedReader.readLine()) != null){
				String[] data = line.split("\t");
				int id = Integer.parseInt(data[0]);
				Teacher d = new Teacher(id, data[1], data[2], data[3]);
				d.printRow();
				System.out.println();
			}
			bufferedReader.close();
		}catch(IOException e){
			System.out.println("Error!");
		}
	}

	public void printRow(){
		System.out.printf("%-10s %-25.20s %-25.20s %-20s", id, name, getSubjectName, department);
	}

    
}