import java.util.Scanner;

public class main {
	
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		String str = input.nextLine();
		
		switch(str) {
		case "true AND true":
		case "false OR true":
		case "true OR false":
		case "true OR true":
			System.out.print("true");
			break;
		case "true AND false":
		case "false AND false":
		case "false AND true":
		case "false OR false":
			System.out.print("false");
			break;
		
		}
		
	}

}
