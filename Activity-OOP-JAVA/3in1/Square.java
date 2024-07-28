public class Square extends Shape{
	public final int numCorners = 4;
	protected double side;

	public Square(){

	}
	public Square(double side){
		this.side = side;
	}
	public Square(String color, double side){
		super.color = color;
		this.side = side;
	}

	public double getSide(){
		return side;
	}
	public void setSide(double side){
		this.side = side;
	}

	public final double getArea(){
		return side * side;
	}

	public final double getPerimeter(){
		return (side * 4);
	}

	public void print(){
		System.out.println("Color: " + super.color);
		System.out.println("Side: " + side);
		System.out.println("No. of Corners: " + numCorners);
		System.out.println("Area: " + getArea());
		System.out.println("Perimeter: " + getPerimeter());
	}
}