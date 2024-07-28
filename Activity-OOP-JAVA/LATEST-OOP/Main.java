import java.io.*;
import java.util.Scanner;

public class Main{
	static Scanner input = new Scanner(System.in);
	static Scanner s1 = new Scanner(System.in);

	public static void menu(){
		System.out.println("\nMenu:");
		System.out.println("[0] Exit Program");
		System.out.println("[1] Add Department");
		System.out.println("[2] View Department");
		System.out.println("[3] View All Departments");
		System.out.println("[4] Add Teacher");
		System.out.println("[5] View Teacher");
		System.out.println("[6] View All Teacher");
		System.out.println("[7] Add Subject");
		System.out.println("[8] View Subject");
		System.out.println("[9] View All Subject");
		System.out.println("[10] Add  Learning Material");
		System.out.println("[11] View Learning Material");
		System.out.println("[12] View All Learning Material");
		System.out.println("[13] Add  Academic Term");
		System.out.println("[14] View Academic Term");
		System.out.println("[15] View All Academic Term");
		System.out.print("Enter Command: ");
	}

	public static void addDepartment(){
		System.out.print("\nEnter Department ID: ");
		int id = input.nextInt();
		System.out.print("Enter Department Name: ");
		String name = s1.nextLine();
		System.out.print("Enter Department Dean: ");
		String name1 = s1.nextLine();

		Department dept = new Department(id, name, name1);

		if(dept.add()){
			System.out.println("\nSuccessfully added!");
		}else{
			System.out.println("\nError");
		}
	}

	public static void viewDepartment(){
		System.out.print("Enter Department ID: ");
		int id = input.nextInt();

		Department vDept = Department.get(id);

		if(vDept != null){
			System.out.println();
			vDept.printDept();
		}
	}

	public static void addTeacher(){
		System.out.print("\nEnter Teacher ID: ");
		int id = input.nextInt();
		System.out.print("Enter Teacher Name: ");
		String name = s1.nextLine();
		System.out.print("Enter Subject: ");
		String subjectName = s1.nextLine();
		System.out.print("Enter Department: ");
		String department = s1.nextLine();

		Teacher teacher = new Teacher(id, name, subjectName, department);

		if(teacher.add()){
			System.out.println("\nSuccessfully added!");
		}else{
			System.out.println("\nError");
		}
	}

	public static void viewTeacher(){
		System.out.print("Enter Teacher ID: ");
		int id = input.nextInt();

		Teacher vteacher = Teacher.get(id);

		if(vteacher != null){
			System.out.println();
			vteacher.printT();
		}
	}

	public static void main(String[] args){
		int choice = -1;

		do{
			menu();
			choice = input.nextInt();
			switch(choice){
				case 1: 
					ADepartment();
					break;
				case 2:
					VDepartment();
					break;
				case 3:
					Department.viewAll();
				case 4:
					ATeacher();
				case 5:
					VTeacher();
				case 6:
					Teacher.viewAll();
			}
		}while(choice != 0);
	}
}