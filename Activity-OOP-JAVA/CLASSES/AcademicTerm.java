import java.util.ArrayList;
import java.util.List;

public class AcademicTerm {

    // Private Attributes
    private String academicTerm;

    // Constructors
    public AcademicTerm() {
        academicTerm = "";
    }

    public AcademicTerm(String academicTerm) {
        this.academicTerm = academicTerm;
    }

    // Accessor Methods
    public String getAcademicTerm() {
        return academicTerm;
    }

    // Mutator Methods 
    public void setAcademicTerm(String academicTerm) {
        this.academicTerm = academicTerm;
    }

    // Named Method
    public void print() {
        System.out.println("Academic Term: " + academicTerm);
        System.out.println();
    }

}