public class Teacher{
    // Attributes
	// private variable
	private String name;
	private int age;
	private String subjectTeaching;
	private String position;
    private int documentReleased;
    private int documentNotReleased;

    // Methods
    //Constructor

	// static variable
	public static int teacherCount;

	public Teacher(){
		name = " ";
		age = 0;
		subjectTeaching = " ";
		position = " ";
        documentReleased = 0;
        documentNotReleased = 0;
	}
	public Teacher(String name, int age,String subjectTeaching,String position, int documentReleased, int documentNotReleased){
        this.name = name;
        this.age = age;
        this.subjectTeaching = subjectTeaching;
        this.position =  position;
        this.documentReleased = documentReleased;
        this.documentNotReleased = documentNotReleased;
    }

    public void Teacher(String n, int a,String sT,String p, int r, int nr){
        name = n;
        age = a;
        subjectTeaching = sT;
        position =  p;
        documentReleased = r;
        documentNotReleased = nr;
    }
    // Accessor method

   	public String getName(){
        return name;
    }
    public int getAge(){
        return age;
    }
    public String getSubjectTeaching(){
        return subjectTeaching;
    }
    public String getPosition(){
        return position;
    }
    public int getDocumentReleased(){
        return documentReleased;
    }
    public int getDocumentNotReleased(){
        return documentNotReleased;
    }

    // -> Mutator Methods

    public void setName(String name){
        this.name = name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public void setSubjectTeaching(String subjectTeaching){
        this.subjectTeaching = subjectTeaching;
    }
    public void setPosition(String position){
        this.position = position;
    }
    public void setDocumentReleased(int documentReleased){
        this.documentReleased = documentReleased;
    }
    public void setDocumentNotReleased(int documentNotReleased){
        this.documentNotReleased = documentNotReleased;
    }

    public void printInfo(){
    	System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Subject teaching: " + subjectTeaching);
        System.out.println("Position: "+ position);
        System.out.println("Number of document released: " + documentReleased); 
        System.out.println("Number of document not yet released: " + documentNotReleased);
        System.out.println(); 
	}
    // named method to calculate the total number of documents will be given by the teacher
    public int getTotalDocuments(){
        int totalDocuments = documentReleased + documentNotReleased;
        return totalDocuments;
    }
}
