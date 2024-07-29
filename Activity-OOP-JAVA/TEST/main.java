import java.util.ArrayList;
import java.util.Scanner;

public class main{
  public static void main(String[] args) {

    // Create an ArrayList to store the departments
    ArrayList<LearningMaterialRecordManagementSystem.Department> departments = new ArrayList<>();

    // Create an ArrayList to store the AcademicTerm
    ArrayList<LearningMaterialRecordManagementSystem.AcademicTerm> academicterms = new ArrayList<>();

    // Create an ArrayList to store the learning materials
    ArrayList<LearningMaterialRecordManagementSystem.LearningMaterial> learningMaterials = new ArrayList<>();

    // Create an ArrayList to store the teachers
    ArrayList<LearningMaterialRecordManagementSystem.Teacher> teachers = new ArrayList<>();

    // Create an ArrayList to store the subjects
    ArrayList<LearningMaterialRecordManagementSystem.Subject> subjects = new ArrayList<>();

    // Create a Scanner to read input from the user
    Scanner scanner = new Scanner(System.in);

    while (true) {
      // Display menu

      System.out.println("");
      System.out.println("====================================================");
      System.out.println("====LEARNING MATERIAL RECORDS MANAGEMENT SYSTEM=====");
      System.out.println("====================================================");
      System.out.println("[1] Add learning material");
      System.out.println("[2] View learning materials");
      System.out.println("[3] Delete learning material");
      System.out.println("[4] Exit");
      System.out.println("----------------------------------------------------");
      System.out.print("Enter a choice: ");
      System.out.print(" ");

      // Read the user's choice
      int choice = scanner.nextInt();

      if (choice == 1) {
        // Add data for learning materials
        //add departments
        System.out.println("====================================================");
        System.out.println("Add:");
        System.out.println("====================================================");
        System.out.print("Enter Department: ");
        String departmentName = scanner.next();
        departments.add(new LearningMaterialRecordManagementSystem.Department(departmentName));
        //add academic term
        System.out.print("Enter Academic Term: ");
        String aTerm = scanner.next();
        academicterms.add(new LearningMaterialRecordManagementSystem.AcademicTerm(aTerm));
        ////add teachers
        System.out.print("Enter Teacher: ");
        String teacherName = scanner.next();
        teachers.add(new LearningMaterialRecordManagementSystem.Teacher(teacherName));
        //add subjects
        System.out.print("Enter Subject: ");
        String subjectName = scanner.next();
        subjects.add(new LearningMaterialRecordManagementSystem.Subject(subjectName));
        //add learning material
        System.out.print("Enter the name of the learning material: ");
        String lmName = scanner.next();
        learningMaterials.add(new LearningMaterialRecordManagementSystem.LearningMaterial(lmName));

      } else if (choice == 2) {
        // View the data of the learning materials
        System.out.println("====================================================================================================================");
        System.out.println("View Learning Materials:");
        System.out.println("====================================================================================================================");
        for (int i = 0; i < learningMaterials.size(); i++) {
        // Get the current learning material
        LearningMaterialRecordManagementSystem.LearningMaterial learningMaterial = learningMaterials.get(i);

        // Get the associated department, academic term, teacher, and subject
        LearningMaterialRecordManagementSystem.Department department = departments.get(i);
        LearningMaterialRecordManagementSystem.AcademicTerm academicTerm = academicterms.get(i);
        LearningMaterialRecordManagementSystem.Teacher teacher = teachers.get(i);
        LearningMaterialRecordManagementSystem.Subject subject = subjects.get(i);

        // Display the learning material along with its associated classes
        System.out.println(learningMaterial.getLearningMaterialName() + " - Subject: " + subject.getSubjectName() + " | Teacher: " + teacher.getTeacherName() + " | Academic Term: " + academicTerm.getAcademicTerm() + " | Department: " + department.getDepartmentName());
        }
      } else if (choice == 3) {
        // Delete a learning material
        System.out.println("====================================================");
        System.out.println("Delete:");
        System.out.println("====================================================");
        System.out.print("Enter the name of the learning material: ");
        String lmName = scanner.next();
        for (int i = 0; i < learningMaterials.size(); i++) {
          if (learningMaterials.get(i).getLearningMaterialName().equals(lmName)) {
            learningMaterials.remove(i);
            break;
          }
        }
      } else if (choice == 4) {
        // Exit the program
        break;
      }
    }

    // Close the scanner
    scanner.close();
  }
}
