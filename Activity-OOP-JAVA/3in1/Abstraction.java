public class Abstraction{
	public static void main(String[] args) {
		Square square1 = new Square(10.0);
		System.out.println("Area: " + square1.getArea());
		System.out.println("Perimeter: " + square1.getPerimeter());
		System.out.println();

		Square square2 = new Square("Red", 12.3);
		square2.print();
		System.out.println();

		SquareChild cs = new SquareChild("Green", 12.3);
		cs.print();
	}
}