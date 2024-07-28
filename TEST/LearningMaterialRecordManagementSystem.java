import java.util.ArrayList;

public class LearningMaterialRecordManagementSystem {
  // Class for department
  public static class Department {
    private String departmentName;

    public Department(String departmentName) {
      this.departmentName = departmentName;
    }

    public String getDepartmentName() {
      return departmentName;
    }

    public void setDepartmentName(String departmentName) {
      this.departmentName = departmentName;
    }
  }

  // Class for academic term
  public static class AcademicTerm {
    private String aTerm;

    public AcademicTerm(String aTerm) {
      this.aTerm = aTerm;
    }

    public String getAcademicTerm() {
      return aTerm;
    }

    public void setAcademicTerm(String aTerm) {
      this.aTerm = aTerm;
    }
  }

  // Class for teacher
  public static class Teacher {
    private String teacherName;
    private LearningMaterial lmName;

    public Teacher(String teacherName) {
      this.teacherName = teacherName;
    }

    public String getTeacherName() {
      return teacherName;
    }

    public void setTeacherName(String teacherName) {
      this.teacherName = teacherName;
    }
  }

  // Class for subjec
  public static class Subject {
    private String subjectName;

    public Subject(String subjectName) {
      this.subjectName = subjectName;
    }

    public String getSubjectName() {
      return subjectName;
    }

    public void setSubjectName(String subjectName) {
      this.subjectName = subjectName;
    }
  }

  // Class for learning material
  public static class LearningMaterial {
    private String lmName;

    public LearningMaterial(String lmName) {
      this.lmName = lmName;
    }

    public String getLearningMaterialName() {
      return lmName;
    }

    public void setLearningMaterialName(String lmName) {
      this.lmName = lmName;
    }
  }
}