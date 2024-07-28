public class MyTeacher{
  public static void main(String[] args){

    System.out.println("--------------------------------------------------------------");
    System.out.println("----------------List of Teachers/Instructors------------------");
    System.out.println("--------------------------------------------------------------");
    //Object 1
    Teacher t1 = new Teacher("Roberto Bayos", 25,"Object Oriented Programming","Assistant Professor 1", 5, 5);

    //Access Accessor Method:
    System.out.println(t1.getName());
    System.out.println(t1.getAge());
    System.out.println(t1.getSubjectTeaching());
    System.out.println(t1.getPosition());
    t1.printInfo();

    //Access Mutator Method
    t1.setDocumentReleased(3);
    t1.setDocumentNotReleased(2);
    t1.printInfo();

    System.out.println("The number of documents that is released is " + t1.getDocumentReleased());
    System.out.println("The number of documents that is not yet released is " + t1.getDocumentNotReleased());
    System.out.println("The total number of documents that will be released is " + t1.getTotalDocuments());
    System.out.println("--------------------------------------------------------------");
    System.out.println("--------------------------------------------------------------");

    // Object 2
    Teacher t2 = new Teacher("Jerome Llaban", 25, "Introduction to AI", "Professor 1", 4, 6);
    System.out.println("");

    //Access Instance Variable
    System.out.println(t2.getName());
    System.out.println(t2.getAge());
    System.out.println(t2.getSubjectTeaching());
    System.out.println(t2.getPosition());

    t2.printInfo();
    System.out.println("The number of documents that is released is " + t2.getDocumentReleased());
    System.out.println("The number of documents that is not yet released is " + t2.getDocumentNotReleased());
    System.out.println("The total number of documents that will be released is " + t2.getTotalDocuments());
    System.out.println("--------------------------------------------------------------");
    System.out.println("--------------------------------------------------------------");

    // Object 3
    Teacher t3 = new Teacher("Marc Christian Tumaneng", 25, "Operating System", "Instructor 1", 3, 7);
    System.out.println("");

    //Access Instance Variable
    System.out.println(t3.getName());
    System.out.println(t3.getAge());
    System.out.println(t3.getSubjectTeaching());
    System.out.println(t3.getPosition());

    t3.printInfo();
    System.out.println("The number of documents that is released is " + t3.getDocumentReleased());
    System.out.println("The number of documents that is not yet released is " + t3.getDocumentNotReleased());
    System.out.println("The total number of documents that will be released is " + t3.getTotalDocuments());
    System.out.println("--------------------------------------------------------------");
    System.out.println("--------------------------------------------------------------");

    // Access Static Variable:
    System.out.println("Teacher Count: " + Teacher.teacherCount);
    // Static variables can be accessed also using the object name
    t1.teacherCount = 3;

    System.out.println("T1 Teacher Count: " + t1.teacherCount);
    System.out.println("T2 Teacher Count: " + t2.teacherCount);
    System.out.println("T3 Teacher Count: " + t3.teacherCount);
    System.out.println("Teacher Count: " + Teacher.teacherCount);
    
  }
}
