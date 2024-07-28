import java.io.*;
public class LearningMaterial{
	
    // Private Attributes
   private String documentName, date, type;


    // Constructors
   public LearningMaterial(){
   documentName = "";
   date = "";
   type = "";
   }

   public LearningMaterial(String documentName, String date, String type){
   this.documentName = documentName;
   this.date = date;
   this.type = type;

   }

   public void LearningMaterial(String dn, String d, String t){
   documentName = dn;
   date = d;
   type = t;

   }

   // Accessor Methods of the private attributes
   public String getDocumentName(){
   return documentName;
   }
   public String getDate(){
   return date;
   }
   public String getType(){
   return type;
   }

   // Mutator Methods of the private attributes
   public void setDocumentName(String documentName){
   this.documentName = documentName;
   }
   public void setDate(String date){
   this.date = date;
   }
   public void setType(String type){
   this.type = type;
   }

   // Named Method to print all attributes
   public void printAttrib(){
   System.out.println();
   System.out.println("Learning Material Name: " + documentName);
   System.out.println("Date: " + date);
   System.out.println("Type: " + type);
   System.out.println("");
   }

}