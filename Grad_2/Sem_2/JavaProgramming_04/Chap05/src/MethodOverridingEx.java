class Shape { // 도형의 슈퍼 클래스
	public void draw() {
		System.out.println("Shape");
	}
}

class Line extends Shape {
	public void draw() { // 메소드 오버라이딩
		System.out.println("Line");
	}
}

class Rect extends Shape {
	public void draw() { // 메소드 오버라이딩
		System.out.println("Rect");
	}
}

class Circle extends Shape {
	public void draw() { // 메소드 오버라이딩
		System.out.println("Circle");
	}
}

public class MethodOverridingEx {

	static void paint(Shape p) {
		p.draw();
	}
	
	public static void main(String[] args) {
		
		Line line = new Line();
		paint(line);
		
		paint(new Shape());
		paint(new Line());
		paint(new Rect());
		paint(new Circle());

	}

}
