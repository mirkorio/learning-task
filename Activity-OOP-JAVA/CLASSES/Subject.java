import java.util.ArrayList;
import java.util.List;

public class Subject{

    // Private Attributes
    private String subjectName;
    private AcademicTerm semester;

    // Constructors
    public Subject(){
    }

    public Subject(AcademicTerm semester, String subjectName){
    this.semester = semester;    
    this.subjectName = subjectName;

    }

    // Accessor Methods of the private attributes
    public AcademicTerm getSemester(){
    return semester;
    }
    public String getSubjectName(){
    return subjectName;
    }


    // Mutator Methods of the private attributes
    public void setSemester(AcademicTerm semester){
    this.semester = semester;
    }
    public void setSubjectName(String subjectName){
    this.subjectName = subjectName;
    }

    // Named Method to print all attributes
    public void printAttrib(){
    System.out.println("Academic Term : " + semester);
    System.out.println("Subject : " + subjectName);

    System.out.println("");
    }
}
