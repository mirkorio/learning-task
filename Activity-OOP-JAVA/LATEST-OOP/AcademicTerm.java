import java.io.*;
public class AcademicTerm{
	
	// Private Attributes
	private String semester;
	// Constructors
	public AcademicTerm(){
		semester = "";
	}

	public AcademicTerm(String semester){
		this.semester = semester;
	}
	// Accessor Methods
	public String getSemester(){
		return semester;
	}
	// Mutator Methods 
	public void setSemester(String semester){
	this.semester = semester;
	}
	// Named Method
	public void print(){
		System.out.println("Semester: " + semester);
		System.out.println();
	}
}