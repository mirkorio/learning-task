import java.util.ArrayList;
import java.util.List;

public class Teacher{
    // Attributes
	// private variable
	private String name;
    private Subject subjectName;
    	
    // Methods
    //Constructor

	public Teacher(){
	}

	public Teacher(String name, Subject subjectName ){
        this.name = name;
        this.subjectName = subjectName;   
    }

    // Accessor method

   	public String getName(){
        return name;
    }

    public Subject getSubjectName(){
        return subjectName;
    }
  
    //Mutator Methods

    public void setName(String name){
        this.name = name;
    }

    public void setSubjectName(Subject subjectName){
        this.subjectName = subjectName;
    }

    public void printInfo(){
    	System.out.println("Name: " + name); 
        System.out.println("Subject teaching: " + subjectName);
        System.out.println(); 
	}


}   


