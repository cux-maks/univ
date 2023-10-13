import java.util.Scanner;

public class Rectangle {
	
	int width;
	int height;
	
	public int getArea() { return width * height; }
	public int getRound() { return (width + height) * 2; } // 교재 없는거 내가 추가한거 ㅇ.ㅇ

	public static void main(String[] args) {
		
		Rectangle rect = new Rectangle();
		Scanner scanner = new Scanner(System.in);
		
		System.out.print(">> ");
		rect.width = scanner.nextInt();
		System.out.print(">> ");
		rect.height = scanner.nextInt();
		
		System.out.println("사각형의 면적은 " + rect.getArea());
		System.out.println("사각형의 둘레는 " + rect.getRound());
		scanner.close();

	}

}