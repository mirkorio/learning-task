import java.util.Scanner;

public class StudentManagementSystem{
	static Scanner input = new Scanner(System.in);

	public static void displayMenu(){
		System.out.println("\nMenu:");
		System.out.println("[0] Exit Program");
		System.out.println("[1] Add Department");
		System.out.println("[2] View Department");
		System.out.println("[3] View All Departments");
		System.out.println("[4] Add Student");
		System.out.println("[5] View Student");
		System.out.println("[6] View All Students");
		System.out.print("Enter Command: ");
	}

	public static void addDepartmentMenu(){
		System.out.print("\nEnter ID: ");
		int id = input.nextInt();

		System.out.print("Enter Name: ");
		String name = input.nextLine();
		name = input.nextLine();

		Department newDept = new Department(id, name);

		if(newDept.add()){
			System.out.println("\nSuccessfully added!");
		}else{
			System.out.println("\nError. Try again!");
		}
	}

	public static void viewDepartmentMenu(){
		System.out.print("\nEnter ID: ");
		int id = input.nextInt();

		Department viewDept = Department.get(id);
		if(viewDept != null){
			System.out.println();
			viewDept.print();
		}else{
			System.out.println("Department does not exist!");
		}
	}

	public static void viewStudentMenu(){
		System.out.print("\nEnter ID: ");
		int id = input.nextInt();

		Student viewStudent = Student.get(id);
		if(viewStudent != null){
			System.out.println();
			viewStudent.print();
		}else{
			System.out.println("Student does not exist!");
		}
	}

	public static void addStudentMenu(){
		System.out.print("\nEnter ID: ");
		int id = input.nextInt();

		System.out.print("Enter Name: ");
		String name = input.nextLine();
		name = input.nextLine();

		System.out.print("Enter Address: ");
		String address = input.nextLine();

		System.out.print("Enter Department ID: ");
		int deptID = input.nextInt();

		Department dept = Department.get(deptID);
		if(dept != null){
			Student newStudent = new Student(id, name, address, dept);
			if(newStudent.add()){
				System.out.println("\nSuccessfully added!");
			}else{
				System.out.println("\nError. Try again!");
			}
		}else{
			System.out.println("Department does not exist.");
		}
	}

	public static void main(String[] args) {
		int command = -1;

		do{
			displayMenu();
			command = input.nextInt();

			switch(command){
				case 1:
					addDepartmentMenu();
					break;
				case 2:
					viewDepartmentMenu();
					break;
				case 3:
					Department.viewAll();
					break;
				case 4:
					addStudentMenu();
					break;
				case 5:
					viewStudentMenu();
					break;
				case 6:
					Student.viewAll();
			}
		}while(command != 0);
	}
}