import java.util.ArrayList;
import java.util.List;
public class LearningMaterial{
	
    // Private Attributes
   private ArrayList<Subject> subjectName;
   private ArrayList<String> documentName, type;
   private ArrayList<Teacher> name;
   private ArrayList<AcademicTerm> academicTerm;


    // Constructors
   public LearningMaterial(){
   }

   public LearningMaterial(Subject subjectName, String documentName,  String type, AcademicTerm academicTerm, Teacher name){
   this.subjectName = subjectName;
   this.documentName = documentName;
   this.type = type;
   this.academicTerm = academicTerm;
   this.name = name;
   }
  
   public LearningMaterial(String documentName){
   this.documentName = documentName;
   }

   // Accessor Methods of the private attributes
   public Subject getSubjectName(){
   return subjectName;
   }
   public String getDocumentName(){
   return documentName;
   }
   public String getType(){
   return type;
   }
   public AcademicTerm getAcademicTerm(){
   return academicTerm;
   }
   public Teacher getName(){
   return name;
   }

   // Mutator Methods of the private attributes
   public void setSubjectName(Subject subjectName){
   this.subjectName = subjectName;
   }
   public void setDocumentName(String documentName){
   this.documentName = documentName;
   }
   public void setType(String type){
   this.type = type;
   }
   public void setAcademicTerm(AcademicTerm academicTerm){
   this.academicTerm = academicTerm;
   }
   public void setName(Teacher name){
   this.name = name;
   }



   // Named Method to print all attributes
  /* public void printAttrib(){
   System.out.println();
   System.out.println("Subject: " + subjectName);
   System.out.println("Document Name: " + documentName);
   System.out.println("Type: " + type);
   System.out.println("");
   }*/
   public void printAttributes() {
    System.out.printf("\n%-25.20s %-25.20s %-25.20s\n", "SUBJECT", "DOCUMENT NAME", "TYPE", "ACADEMIC TERM", "TEACHER");
    System.out.printf("%-25.20s %-25.20s %-25.20s ",subjectName, documentName, type, academicTerm, name);
  }

}