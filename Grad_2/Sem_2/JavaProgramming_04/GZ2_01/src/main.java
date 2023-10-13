import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		
		char n = in.next().charAt(0);
		
		    for(int i = 0; i <= n - 97; i++) {
			for(int j = 97 + i; j <= n; j++) {
				System.out.print((char)j);
			}
			System.out.println();
		}
			
	}

}