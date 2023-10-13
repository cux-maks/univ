
public class Circle {
	
	int radius;
	String name;
	
	public Circle() { radius = 1; name = ""; }
	public Circle(int r, String n) { radius = r; name = n; }
	public double getArea() { return 3.14*radius*radius; }
	
	
	public static void main(String[] args) {
		
		Circle pizza;
		pizza = new Circle();
		pizza.radius = 10;
		pizza.name = "자바피자";
		double Area = pizza.getArea();
		System.out.println(pizza.name + "의 면적은 " + Area);
		
		Circle donut = new Circle();
		donut.radius = 2;
		donut.name = "자바도넛";
		Area = donut.getArea();
		System.out.println(donut.name + "의 면적은 " + Area);
		
		Circle pizza2 = new Circle(10, "자바피자2");
		Area = pizza2.getArea();
		System.out.println(pizza2.name + "의 면적은 " + Area);		
		
		Circle donut2 = new Circle();
		donut2.name = "자바도넛2";
		Area = donut2.getArea();
		System.out.println(donut2.name + "의 면적은 " + Area);
		
	}

}
