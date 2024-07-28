import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main{
	private static List<Department>departments;
	static Scanner input = new Scanner(System.in);

	public static void main(String[] args){
		departments = new ArrayList<>();
		Scanner scanner = new Scanner(System.in);

		Department d1 = new Department("CCS");
		Department d2 = new Department("CAS");

		departments.add(d1);
		departments.add(d2);

		LearningMaterial lm1 = new LearningMaterial("OOP","Module1",".pdf","Mid-term","Sir.Jayvee Sias");
		LearningMaterial lm2 = new LearningMaterial("OS","Module1",".pdf","Mid-term","Sir.Ralf Spencer Talagtag");
		LearningMaterial lm3 = new LearningMaterial("PE2","Module1",".pdf","Mid-term","Sir.Salthiel Al Roncesvalles");
		LearningMaterial lm4 = new LearningMaterial("PE3","Module1",".pdf","Mid-term","Sir.Salthiel Al Roncesvalles");

		d1.addLearningMaterial(lm1);
		d1.addLearningMaterial(lm2);
		d2.addLearningMaterial(lm3);
		d2.addLearningMaterial(lm4);

		System.out.println("====================================================");
		System.out.println("LEARNING MATERIAL DOCUMENT RECORDS MANAGEMENT SYSTEM");
		System.out.println("====================================================");
		while(true){
		System.out.println("[1] Add Department");
		System.out.println("[2] Add Learning Material");
		System.out.println("[3] View Department");
		System.out.println("[4] View Learning Material");
		System.out.println("[5] View all Learning Material and Department");
		System.out.println("[0] Exit Program");
		System.out.println("----------------------------------------------------");
		System.out.print("Enter Command: ");
		int choice = scanner.nextInt();
      	scanner.nextLine();
      
      switch(main){
      		case 1:
      			System.out.print("Enter department name: ");
      			String departmentName = scanner.nextLine();
				Department department = new Department(departmentName);
				departments.add(department);
				break;
			case 2:
				System.out.print("Enter department name: ");
      			departmentName = scanner.nextLine();
      			department = searchDepartmanet(departmentName);
      			if(department == null){
				System.out.println("Department not found.");
				break;
				}
				System.out.print("\nEnter subject: ");
				String subjectName = scanner.nextLine();
				System.out.print("\nEnter Document Name: ");
				String documentName = scanner.nextLine();
				System.out.print("\nEnter Document type: ");
				String type = type.nextLine();
				System.out.print("\nEnter Academic Term: ");
				String academicTerm = scanner.nextLine();
				System.out.print("\nEnter Teacher: ");
				String name = scanner.nextLine();
				LearningMaterial learningMaterial = new LearningMaterial(subjectName, documentName, type, academicTerm, name);
				department.addLearningMaterial(learningMaterial);
				break;
			case 3:
				System.out.print("Enter department name: ");
				departmentName = scanner.nextLine();
      			department = searchDepartmanet(departmentName);	
      			if(department == null){
				System.out.println("Department not found.");
				break;
				}
				department.printAttributes();
				break;
			case 4:	
				System.out.print("Enter Document name: ");
				documentName = scanner.nextLine();
				LearningMaterial searchedLearningMaterial = searchLearningMaterial(documentName);
				 if(searchedLearningMaterial == null){
				 	System.out.println("Document not found.");
            		break;
				 }
				 searchedLearningMaterial.printAttributes();
				 break;
			case 5:
				printAllDepartmentAndLearningMaterials();
				break;
			case 6:	 
				System.out.println("Exiting program.");
          		return;
        	default:
          		System.out.println("Invalid choice.");
          		break;
      		}
		}	
	}
	private static Department searchDepartmanet(String departmentName) {
   	 	for (Department department : departments) {
     	 if (department.getDepartmentName().equals(departmentName)) {
        	return department;
      	}
      }
   	  return null;
  	}

  	private static LearningMaterial searchLearningMaterial(String documentName) {
    	for (Department department : departments) {
     	   LearningMaterial learningMaterial = department.searchLearningMaterial(documentName);
      	   if (learningMaterial != null) {
        	return learningMaterial;
      	}
    }
    return null;
 	}

  	private static void printAllDepartmentAndLearningMaterials() {
   		 for (Department department : departments) {
     		 department.printAttributes();
    	}
  	}	

}

