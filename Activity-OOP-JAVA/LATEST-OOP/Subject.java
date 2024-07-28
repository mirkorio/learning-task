import java.io.*;
public class Subject{

    // Private Attributes
    private String subjectName, schedule;
    private int students;

    // Constructors

    public Subject(){
    subjectName = "";
    schedule = "";
    students = 0;

    }
    public Subject(String subjectName){
        this.subjectName = subjectName;
    }

    public Subject( String subjectName, String schedule, int students){
    this.subjectName = subjectName;
    this.schedule = schedule;
    this.students = students;
    }

    // Accessor Methods of the private attributes
    public String getSubjectName(){
    return subjectName;
    }
    public String getSchedule(){
    return schedule;
    }
    public int getStudents(){
    return students;
    }

    // Mutator Methods of the private attributes
    public void setSubjectName(String subjectName){
    this.subjectName = subjectName;
    }
    public void setSchedule(String schedule){
    this.schedule = schedule;
    }
    public void setLearners(int students){
    this.students = students;
    }

    // Named Method to print all attributes
    public void printAttrib(){
    System.out.println("Subject : " + subjectName);
    System.out.println("Schedule: " + schedule);
    System.out.println("Students: " + students);
    System.out.println("");
    }
}
