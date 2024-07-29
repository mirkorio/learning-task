// Method Overloading - same name, different parameters
public class Overload{
	// attributes

	public static void add(int a, int b){
		int sum = a + b;
		System.out.println(sum);
	}

	public static void add(double a, double b){
		double sum = a + b;
		System.out.println(sum);
	}

	public static void add(int x, int y, int z){
		int sum = x + y + z;
		System.out.println(sum);
	}

	public static void add(double x, int y){
		double sum = x + y;
		System.out.println(sum);
	}

	public static void add(String a, String b){
		String sum = a + b;
		System.out.println(sum);
	}
}