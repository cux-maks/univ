public class Box {

	private int width, height;
	private char fillChar;
	
	public Box() {
		width = 10;
		height = 1;
		fillChar = '.';
	}
	
	public Box(int width, int height) {
		this.width = width;
		this.height = height;
	}
	
	public void draw() {
		for(int i = 0; i < height; i++) {
			for(int j = 0; j < width; j++) {
				System.out.print(fillChar);
			}
			System.out.println();
		}
	}
	
	public void fill(char c) { fillChar = c; }
	
	public static void main(String[] args) {
		
		Box a = new Box();
		Box b = new Box(20, 3);
		Box c = new Box();
		
		a.fill('*');
		b.fill('%');
		
		a.draw();
		b.draw();
		c.draw();
		
	}
	
}
