public class Composition{
	public static void main(String[] args) {
		AcademicTerm semester1 = new AcademicTerm("1st Semester");
		AcademicTerm semester2 = new AcademicTerm("2nd Semester");
		
		Subject name1 = new Subject("Data Structures and Algorithm","Monday, 9:00 AM - 12:00 PM || Thursday, 8:00 AM - 10:00 AM ",27);
		Subject name2 = new Subject("Algoritm and Complexity","Monday, 1:00 PM - 6:00 PM", 27);
		Subject name3 = new Subject("Intruduction to Artificial Intelligence", "Tuesday, 9:00 AM - 11:00 AM || Wednesday, 9:00 AM - 12:00 PM",27);
		Subject name4 = new Subject("Object Oriented Programming","Tuesday, 1:00 PM - 6:00 PM", 27);
		Subject name5 = new Subject("Discrete Structures 2","Wednesday, 1:00 PM - 2:30 PM || Thursday, 10:30 AM - 12:00 PM", 27);
		Subject name6 = new Subject("Operating System", "Saturday, 8:30 AM - 1:00 PM", 27);
		Subject name7 = new Subject("Not Available");

		System.out.println("-------------------------------------------------------------------------");
		semester1.print();
		System.out.println("-------------------------------------------------------------------------");
		System.out.println("-------------------------------------------------------------------------");
		name1.printAttrib();
		System.out.println("-------------------------------------------------------------------------");
		name2.printAttrib();
		System.out.println("-------------------------------------------------------------------------");
		name3.printAttrib();
		System.out.println("-------------------------------------------------------------------------");
		name4.printAttrib();
		System.out.println("-------------------------------------------------------------------------");
		name5.printAttrib();
		System.out.println("-------------------------------------------------------------------------");
		name6.printAttrib();
		System.out.println("-------------------------------------------------------------------------");
		semester2.print();
		System.out.println("-------------------------------------------------------------------------");
		System.out.println("-------------------------------------------------------------------------");
		name7.printAttrib();
		System.out.println("-------------------------------------------------------------------------");
		
	}
}