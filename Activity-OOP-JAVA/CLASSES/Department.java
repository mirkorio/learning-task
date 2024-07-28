import java.util.ArrayList;
import java.util.List;

public class Department{
    private String departmentName;
    
    private List<LearningMaterial>learningMaterials;

    public Department(String departmentName){
        this.departmentName = departmentName;
        this.learningMaterials = new ArrayList<>();
    } 
   
    public String getDepartmentName(){
        return departmentName;
    }

    // Mutator Methods of the private attributes
    public void setDepartmentName(String departmentName){
    this.departmentName = departmentName;
    }
   
    public List<LearningMaterial> getDocumentName() {
    return learningMaterials;
    }

    public void setDocumentName(List<LearningMaterial> learningMaterials) {
    this.learningMaterials = learningMaterials;
    }

    public void addMember(LearningMaterial learningMaterial) {
    this.learningMaterials.add(learningMaterial);
    }
    
    // Named Method to print all attributes
    public void printAttrib(){
        System.out.println();
        System.out.println("Department: " + departmentName);
        System.out.println("Learning Materials:");
        for (LearningMaterial learningMaterial:learningMaterials){
            learningMaterial.printAttributes();
        }
    }
      public LearningMaterial searchLearningMaterial(String documentName) {
        for (LearningMaterial learningMaterial : learningMaterials) {
         if (learningMaterial.getDocumentName().equals(documentName)) {
         return learningMaterial;
         }
        }
        return null;
   } 
}